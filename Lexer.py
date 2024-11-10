import ply.lex as lex
import Logs as loger
import re

reserved = {
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NULL',
}

tokens = (
    'STRING',
    'VARIABLE_GLOBAL',
    'VARIABLE_CONSTANTE',
    'VARIABLE_CLASE',
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCIA',
    'COMA',
    'LBRACKET',
    'RBRACKET',
    'HASHROCKET',
    'COLON',
) + tuple(reserved.values())

t_COMA = r'\,'
t_LBRACKET = r'{'
t_RBRACKET = r'\}'
t_HASHROCKET = r'=>'
t_COLON = r'\:'

def t_STRING(t):
    r'\'[A-Za-z0-9_]*\'|\"[A-Za-z0-9_]*\"'
    t.value = str(t.value)
    return t

def t_VARIABLE_GLOBAL(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_GLOBAL')
    return t

def t_VARIABLE_CLASE(t):
    r'@@[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_CLASE')
    return t


def t_VARIABLE_INSTANCIA(t):
    r'@[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_INSTANCIA')
    return t

def t_VARIABLE_CONSTANTE(t):
    r'[A-Z][A-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_CONSTANTE')
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t


error_list = []

def t_error(t):
    # Guarda el error en la lista
    error_message = f"Illegal character '{t.value[0]}' at line {t.lineno}"
    error_list.append(error_message)
    print(error_message)  # También lo muestra en la consola
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

lexer = lex.lex()

data = '''
    { name: "Alina", age: 25, city: "Guayaquil" }
    'string'
    true
    $global_var 
    $total_count 
    $user_name 
    $MAX_LIMIT 
    $is_active 
    
    $$global_var   
    $global_var@name 
    $global var 
    $-name 
    $$MAX_VALUE

@@class_var 
@@total_count
@@is_enabled
@@user_list 
@@MAX_LIMIT 

@@@class_var  
@@1class  
@@ total_count 
@@is-active 
@@ClassVar 

'''

loger.create_log(lexer,"alicarpio",data, error_list)
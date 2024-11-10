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
    'GT',
    'LT',
    'GE',
    'LE',
    'EQ',
    'NE',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULE',
    'POWER',
    'INTEGER',
    'FLOAT'
) + tuple(reserved.values())

t_COMA = r'\,'
t_LBRACKET = r'{'
t_RBRACKET = r'\}'
t_HASHROCKET = r'=>'
t_COLON = r'\:'
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULE = r'%'
t_POWER = r'\*\*'

def t_FLOAT(t):
    r'-?(?:0\.?[0-9]+|[1-9][0-9]*\.?[0-9]*|\.?[0-9]+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'-?\b\d+\b'
    t.value = int(t.value)
    return t

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
3.14
-0.5
.678
-123.456
    { name: "Alina", age: 25, city: "Guayaquil" }
    
    5 > 3       
    10 < 20      
    15 >= 15     
    8 <= 10        
    5 == 5         
    7 != 2  
    
    3 + 4        
10 - 2         
6 * 7          
20 / 5          
10 % 3          
2 ** 3        

3 + 4 * 2 > 7                   
(10 - 5) * 3 >= 15              
20 / 4 == 5 and 10 % 3 != 1     
2 ** 3 + 5 <= 13     
       

    
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
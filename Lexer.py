import ply.lex as lex
import Logs as loger
import re

reserved = {
    'true': 'TRUE',
    'false': 'FALSE',
    'nil': 'NULL',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'unless': 'UNLESS',
    'case': 'CASE',
    'when': 'WHEN',
    'while': 'WHILE',
    'until': 'UNTIL',
    'for': 'FOR',
    'do': 'DO',
    'def': 'DEF',
    'class': 'CLASS',
    'end': 'END'
}

tokens = (
    'SYMBOL',
    'LSQBRACKET',
    'RSQBRACKET',
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
    'AND_OP',
    'OR_OP',
    'NOT_OP',
    'POWER',
    'INTEGER',
    'FLOAT'
) + tuple(reserved.values())

t_COMA = r'\,'
t_LBRACKET = r'{'
t_RBRACKET = r'\}'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
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
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_NOT_OP = r'!'

def t_SYMBOL(t):
    r'\:[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_FLOAT(t):
    r'-?(?:0\.?[0-9]+|[1-9][0-9]*\.?[0-9]*|\.?[0-9]+)'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'-?\b\d+\b'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'([^\'\\]*(\\.[^\'\\]*)*)\'|\"([^\"\\]*(\\.[^\"\\]*)*)\"'
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

:algo
:algo_09
:99_algo
:_algo


[1, 2, 3, :symbol, "string", true, false, nil]
[10 + 20, 30 * 4, 50 - 6]
[[1, 2], [3, 4]]


true && false
10 > 5 || 5 < 3
!true
!false

if true && false
  while x < 10
    do_something
  end
else
  for i in [1, 2, 3]
    puts i
  end
end

def my_method
  puts "Hello, World!"
end

class MyClass
end
'''

loger.create_log(lexer,"bryanestrada003",data, error_list)
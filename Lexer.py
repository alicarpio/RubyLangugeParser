import ply.lex as lex
import Logs as loger

reserved = {}

tokens = (
   'VARIABLE_GLOBAL',
    'VARIABLE_CONSTANTE',
    'VARIABLE_CLASE',
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCIA',
) + tuple(reserved.values())

def t_VARIABLE_CONSTANTE(t):
    r'^[A-Z][A-Z]*$'
    t.type = reserved.get(t.value, 'VARIABLE_CONSTANTE')
    return t

def t_VARIABLE_CLASE(t):
    r'^\@\@[a-zA-Z_]\w*$'
    t.type = reserved.get(t.value, 'VARIABLE_CLASE')
    return t

def t_VARIABLE_GLOBAL(t):
    r'^\$[a-zA-Z_]\w*$'
    t.type = reserved.get(t.value, 'VARIABLE_GLOBAL')
    return t

def t_VARIABLE_INSTANCIA(t):
    r'^\@[a-zA-Z_]\w*$'
    t.type = reserved.get(t.value, 'VARIABLE_INSTANCIA')
    return t

def t_VARIABLE_LOCAL(t):
    r'^([a-z]|_[a-zA-Z0-9_])([a-zA-Z0-9_]\w*)?$'
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
VARIABLE_CONSTANTE

OTRA_CONSTANTE

initials

@@class_variable

@engineer

@@class_variable

TYPES
'''

loger.create_log(lexer,"alicarpio",data, error_list)
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
    'class': 'CLASS',
    'def': 'DEF',
    'initialize': 'INITIALIZE',
    'end': 'END',
    'puts': 'PUTS',
    'new': 'NEW'
}

tokens = (
    'SYMBOL',
    'STRING',
    'VARIABLE_GLOBAL',
    'VARIABLE_CONSTANTE',
    'VARIABLE_CLASE',
    'VARIABLE_LOCAL',
    'VARIABLE_INSTANCIA',
    'COMA',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'LSQBRACKET',
    'RSQBRACKET',
    'HASHROCKET',
    'COLON',
    'SEMICOLON',
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
    'FLOAT',
    'COMMENT',
    'CLASS_NAME',
    'METHOD_NAME',
    'VARIABLE_NAME',
    'EQUALS',
    'DOT'
) + tuple(reserved.values())

t_COMA = r'\,'
t_LBRACKET = r'{'
t_RBRACKET = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'
t_SEMICOLON = r';'
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
t_EQUALS = r'='
t_DOT = r'\.'

def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar comentarios o, si quieres, podrías registrarlos en el log

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

# Constantes y nombres de clase en Ruby (empiezan con una letra mayúscula)
def t_CLASS_NAME(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

# Nombres de métodos y variables locales
def t_METHOD_NAME(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'METHOD_NAME')  # Si es una palabra reservada, cambia el tipo
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
class MyClass
  def initialize(name)
    @name = name
  end

  def greet
    puts "Hello, #{@name}"
  end
end

obj = MyClass.new("Ruby")
obj.greet
'''

loger.create_log(lexer,"bryanestrada003",data, error_list)
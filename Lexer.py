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
    'new': 'NEW',
    'each': 'EACH'
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
    'DOT',
    'PIPE'
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
t_PIPE = r'\|'
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
    pass

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
    r'\$[a-zA-Z]*[^\$][a-zA-Z0-9_]*'
    t.type = 'VARIABLE_GLOBAL'
    return t

def t_VARIABLE_CLASE(t):
    r'\@{2}[a-z]*[a-zA-Z0-9_]*'
    if re.search(r'[@\s-]', t.value) or re.match(r'@@@', t.value) or re.match(r'@@[0-9]', t.value):
        error_message = f"Illegal class variable '{t.value}' at line {t.lineno}"
        error_list.append(error_message)
        print(error_message)
        return None
    t.type = 'VARIABLE_CLASE'
    return t

def t_VARIABLE_INSTANCIA(t):
    r'\@[a-zA-Z_][a-zA-Z0-9_]*'
    # Detecta patrones ilegales para variables de instancia
    if re.search(r'[@\s-]', t.value):
        error_message = f"Illegal instance variable '{t.value}' at line {t.lineno}"
        error_list.append(error_message)
        print(error_message)
        return None
    t.type = 'VARIABLE_INSTANCIA'
    return t

def t_VARIABLE_CONSTANTE(t):
    r'[A-Z][A-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_CONSTANTE')
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_LOCAL')
    return t

def t_CLASS_NAME(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

def t_METHOD_NAME(t):
    r'\.?[a-z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'METHOD_NAME')
    return t

error_list = []

def t_error(t):
    char = t.value[0]
    if char == '$':
        error_message = f"Illegal global variable usage with '{char}' at line {t.lineno}"
    elif char == '@':
        error_message = f"Illegal instance or class variable usage with '{char}' at line {t.lineno}"
    else:
        error_message = f"Illegal character '{char}' at line {t.lineno}"

    error_list.append(error_message)
    print(error_message)
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

lexer = lex.lex()

data = '''
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

# Definición de un método de evaluación
def evaluar_numero(n)
  if n > 10
    return "Mayor que 10"
  elsif n == 10
    return "Es igual a 10"
  else
    return "Menor que 10"
  end
end

# Declaración de un hash
persona = {
  "nombre" => "Juan",
  "edad" => 25,
  :pais => "México",
  :activo => true
}

# Usamos el método y almacenamos el resultado
resultado = evaluar_numero(12)

# Iteración sobre el hash
persona.each do |clave, valor|
  if clave.is_a?(String)
    puts "Clave (String): #{clave} => Valor: #{valor}"
  else
    puts "Clave (Symbol): #{clave} => Valor: #{valor}"
  end
end

# Uso de operador lógico
edad_valida = persona["edad"] >= 18 && persona["activo"] == true

puts "Edad válida y activo: #{edad_valida}"
'''
loger.create_log(lexer, "bryanestrada003", data, error_list)

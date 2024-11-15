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
    'CLASS_NAME',
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
    pass  # No guardamos comentarios; se ignoran

def t_SYMBOL(t):
    r'\:[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
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
    return t

# Detecta variables de clase
def t_VARIABLE_CLASE(t):
    r'\@{2}[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_VARIABLE_INSTANCIA(t):
    r'\@[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_CLASS_NAME(t):
    r'[A-Z][a-zA-Z0-9_]*'
    return t

def t_VARIABLE_CONSTANTE(t):
    r'[A-Z][A-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIABLE_CONSTANTE')
    return t

def t_METHOD_NAME(t):
    r'\.?[a-z_][a-zA-Z0-9_]*\(?\.*'
    t.type = reserved.get(t.value.lstrip('.'), 'METHOD_NAME')
    return t

def t_VARIABLE_LOCAL(t):
    r'[a-z_][a-zA-Z0-9_]*'
    if t.value not in reserved:
        t.type = 'VARIABLE_LOCAL'
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
class Estudiante
  attr_accessor :nombre, :edad, :promedio, :materias

  def initialize(nombre, edad, promedio, materias)
    @nombre = nombre               # String
    @edad = edad                   # Integer
    @promedio = promedio           # Float
    @materias = materias           # Array de strings
  end

  # Método para obtener información del estudiante
  def mostrar_informacion
    puts "Nombre: #{@nombre}"
    puts "Edad: #{@edad}"
    puts "Promedio: #{@promedio}"
    puts "Materias: #{@materias.join(', ')}"
  end
end

# Hash para almacenar estudiantes por su ID (como clave)
estudiantes = {}

# Creación de dos estudiantes y almacenamiento en el hash
estudiantes[:est1] = Estudiante.new("Ana", 20, 8.5, ["Matemáticas", "Historia", "Ciencias"])
estudiantes[:est2] = Estudiante.new("Juan", 22, 9.0, ["Inglés", "Arte", "Física"])

# Método para calcular el promedio general de todos los estudiantes
def calcular_promedio_general(estudiantes)
  total = 0.0
  estudiantes.each do |clave, estudiante|
    total += estudiante.promedio
  end
  promedio_general = total / estudiantes.size
  puts "Promedio general de la clase: #{promedio_general}"
end

# Muestra la información de cada estudiante
estudiantes.each do |id, estudiante|
  puts "ID del Estudiante: #{id}"
  estudiante.mostrar_informacion
  puts "-------------------------"
end

# Llamada al método para calcular el promedio general
calcular_promedio_general(estudiantes)

'''
loger.create_log(lexer, "alicarpio", data, error_list)

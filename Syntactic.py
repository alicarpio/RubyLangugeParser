import ply.yacc as yacc
from Lexer import tokens
from Lexer import data
import Logs as loger
from Lexer import lexer

errores = ""

# Reglas de la gramática
def p_program(p):
    'program : code_list'

def p_code_list(p):
    '''code_list : code
                 | code code_list'''


def p_code(p):
    '''code : asignacion
            | impresion
            | solicitud_entrada
            | if_statement
            | function_definition
            | while_statement'''


# Reglas de la gramática
def p_asignacion(p):
    '''asignacion : NAME EQUALS valor
                  | VARIABLE_GLOBAL EQUALS valor
                  | VARIABLE_CLASE EQUALS valor
                  | VARIABLE_INSTANCIA EQUALS valor
                  | VARIABLE_LOCAL EQUALS valor
    '''


def p_impresion(p):
    'impresion : PUTS argumentos_opt'

def p_solicitud_entrada(p):
    '''solicitud_entrada : PUTS STRING
                         | NAME EQUALS GETS DOT CHOMP
    '''

def p_argumentos_opt(p):
    '''argumentos_opt : argumentos
                      | empty'''

def p_argumentos(p):
    '''argumentos : valor
                  | valor COMA argumentos'''

def p_valor(p):
    '''valor : operand
             | STRING
             | NULL
             | SYMBOL
             | boolean
             | lists
             | operation
             | condition
             | expression
             | hash
    '''

def p_expression(p):
    '''expression : expression operatorArithm operand
                  | operand'''

def p_operand(p):
    '''operand : INTEGER
               | FLOAT
               | NAME'''
    p[0] = p[1]

def p_operatorArithm(p):
    '''operatorArithm : PLUS
                | MINUS
                | MULTIPLY
                | DIVIDE
                | MODULE
                '''
    p[0] = p[1]

def p_power_op(p):
    '''power_op : INTEGER POWER INTEGER'''

def p_lists(p):
    '''lists : LBRACKET argumentos RBRACKET
             | LSQBRACKET argumentos RSQBRACKET'''

def p_hash(p):
    '''hash : LBRACKET pares_hash RBRACKET
            | LBRACKET empty RBRACKET'''

def p_pares_hash(p):
    '''pares_hash : par_hash
                  | par_hash COMA pares_hash'''

def p_par_hash(p):
    '''par_hash : clave HASHROCKET valor
                | clave COLON valor'''


# Las claves pueden ser símbolos o strings
def p_clave(p):
    '''clave : SYMBOL
             | STRING'''


def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''


def p_operation(p):
    '''operation : operand operatorArithm operand
                 | operand operatorArithm operation'''


def p_if_statement(p):
    '''
    if_statement : IF condition block END
                 | IF condition block ELSE block END
                 | IF condition block ELSIF condition block END
                 | IF condition block ELSIF condition block ELSE block END'''
    p[0] = p[1]

def p_while_statement(p):
    '''while_statement : WHILE condition block END'''

def p_comparison(p):
    '''comparison : valor comparator valor'''

def p_block(p):
    ''' block : statement
              | statement block'''

def p_statement(p):
    ''' statement : impresion
                  | asignacion'''

def p_condition(p):
    '''condition : comparison
                 | boolean
                 | NOT_OP comparison
                 | comparison operatorCond comparison
                 | LPAREN condition RPAREN'''

def p_operatorCond(p):
    '''operatorCond : AND_OP
                    | OR_OP'''

def p_cond(p):
    '''cond : valor comparator valor
            | LPAREN comparison RPAREN'''


def p_comparator(p):
    '''comparator : EQ
                  | NE
                  | LT
                  | LE
                  | GT
                  | GE'''

def p_empty(p):
    'empty :'
    p[0] = None

def p_function_definition(p):
    '''
    function_definition : DEF NAME LPAREN parameters RPAREN body END
    '''

def p_parameters(p):
    '''
    parameters : NAME
               | NAME COMA parameters
               | empty
    '''

def p_body(p):
    '''
    body : statement
         | statement body
    '''


def p_error(p):
    global errores
    error_message = "Error de sintaxis en la entrada en el token '{}'\n".format(p.value)
    error_message += "Tipo del token: {}\n".format(p.type)
    error_message += "Ubicacion del error - Linea {}, Posicion {}\n".format(p.lineno, p.lexpos)
    errores += error_message


def analysing(input_string):
    global errores
    errores = ""  # Reinicia la cadena de errores antes de cada análisis
    parser.parse(input_string)
    return errores


# Build the parser
parser = yacc.yacc()

# Algoritmo Michael Estrada
ruby_code_1 = '''# Definición de un método de evaluación\n
def evaluar_numero(n)\n
  if n > 10\n
    return "Mayor que 10"\n
  elsif n == 10\n
    return "Es igual a 10"\n
  else\n
    return "Menor que 10"\n
  end\n
end\n\n

# Declaración de un hash\n
persona = {\n
  "nombre" => "Juan",\n
  "edad" => 25,\n
  :pais => "México",\n
  :activo => true\n
}\n\n

# Usamos el método y almacenamos el resultado\n
resultado = evaluar_numero(12)  # Evaluando si el número es mayor que 10\n\n

# Iteración sobre el hash\n
persona.each do |clave, valor|\n
  if clave.class == String\n
      puts "Clave (String): #{clave} => Valor: #{valor}"\n
    else\n
    puts "Clave (Symbol): #{clave} => Valor: #{valor}"\n
  end\n
end\n\n

# Llamada a método de comparación\n
puts resultado  # Imprime "Mayor que 10"\n\n

# Uso de operador lógico\n
edad_valida = persona["edad"] >= 18 && persona["activo"] == true  # Verificando que la persona sea mayor de edad y activa\n\n

puts "Edad válida y activo: #{edad_valida}"\n
'''


# Algoritmo Alina Carpio
ruby_code_2 = '''# Clase Estudiante que contiene información básica de cada estudiante\n
class Estudiante\n
  attr_accessor :nombre, :edad, :promedio, :materias\n\n

  def initialize(nombre, edad, promedio, materias)\n
    @nombre = nombre               # String\n
    @edad = edad                   # Integer\n
    @promedio = promedio           # Float\n
    @materias = materias           # Array de strings\n
  end\n\n

  # Método para obtener información del estudiante\n
  def mostrar_informacion\n
    puts "Nombre: #{@nombre}"\n
    puts "Edad: #{@edad}"\n
    puts "Promedio: #{@promedio}"\n
    puts "Materias: #{@materias.join(', ')}"\n
  end\n
end\n\n

# Hash para almacenar estudiantes por su ID (como clave)\n
estudiantes = {}\n\n

# Creación de dos estudiantes y almacenamiento en el hash\n
estudiantes[:est1] = Estudiante.new("Ana", 20, 8.5, ["Matemáticas", "Historia", "Ciencias"])\n
estudiantes[:est2] = Estudiante.new("Juan", 22, 9.0, ["Inglés", "Arte", "Física"])\n\n

# Método para calcular el promedio general de todos los estudiantes\n
def calcular_promedio_general(estudiantes)\n
  total = 0.0\n
  estudiantes.each do |key, estudiante|\n
    total += estudiante.promedio\n
  end\n
  promedio_general = total / estudiantes.size\n
  puts "Promedio general de la clase: #{promedio_general}"\n
end\n\n

# Muestra la información de cada estudiante\n
estudiantes.each do |id, estudiante|\n
  puts "ID del Estudiante: #{id}"\n
  estudiante.mostrar_informacion\n
  puts "-------------------------"\n
end\n\n

# Llamada al método para calcular el promedio general\n
calcular_promedio_general(estudiantes)\n
'''

result = parser.parse(ruby_code_2)
if result == None :
     print('PASS')

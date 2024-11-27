import ply.yacc as yacc
from Lexer import tokens
from Lexer import data
import Logs as loger
import Lexer as lx
from Lexer import lexer


# Reglas de la gramática
def p_program(p):
    'program : code_list'

def p_code_list(p):
    '''code_list : code
                 | code code_list'''


def p_code(p):
    '''code : asignacion
            | impresion
            | if_statement
            | while_statement
            | instantiation
            | solicitud_entrada
            | function_definition
            | class_definition'''


# Reglas de la gramática
def p_asignacion(p):
    '''asignacion : NAME EQUALS valor
                  | VARIABLE_GLOBAL EQUALS valor
                  | VARIABLE_INSTANCIA EQUALS valor
                  | VARIABLE_LOCAL EQUALS valor'''

def p_func_call(p):
    '''func_call : NAME LPAREN argumentos_opt RPAREN'''

def p_impresion(p):
    '''impresion : PUTS argumentos_opt'''

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
             | func_call
             | method_call'''

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

#def p_comparison_integer(p):
#    '''comparison_integer : valor comparator valor'''

def p_comparison_integer(p):
    '''comparison_integer : INTEGER comparator INTEGER'''

def p_block(p):
    ''' block : statement
              | statement block'''

def p_statement(p):
    ''' statement : asignacion
                  | impresion
                  | if_statement
                  | while_statement
                  | instantiation
                  | return'''

def p_return(p):
    '''return : RETURN argumentos'''

def p_condition(p):
    '''condition : comparison_integer
                 | boolean
                 | NOT_OP comparison_integer
                 | comparison_integer operatorCond comparison_integer'''

def p_operatorCond(p):
    '''operatorCond : AND_OP
                    | OR_OP'''



def p_class_definition(p):
    '''class_definition : CLASS CLASS_NAME class_body END'''

def p_function_definition(p):
    '''function_definition : DEF NAME LPAREN argumentos_opt RPAREN body END'''

# Regla para el cuerpo de la clase
def p_class_body(p):
    '''class_body : empty
                  | constructor_definition
                  | class_body_element_list'''

def p_constructor_definition(p):
    '''constructor_definition : DEF INITIALIZE LPAREN parameters RPAREN body END'''


# Lista de elementos dentro de la clase
def p_class_body_element_list(p):
    '''class_body_element_list : class_body_element
                               | class_body_element class_body_element_list'''

# Elementos permitidos dentro de una clase
def p_class_body_element(p):
    '''class_body_element : asignacion
                          | function_definition
                          | function_def_no_params'''

def p_function_def_no_params(p):
    '''function_def_no_params : DEF NAME body END'''

def p_method_call(p):
    '''method_call : NAME DOT NAME LPAREN argumentos_opt RPAREN
                   | NAME DOT NAME'''

def p_instantiation(p):
    '''
    instantiation : CLASS_NAME NEW LPAREN argumentos RPAREN
    '''

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

# Manejo de errores
error_list = []
def p_error(p):
    if p:
        error_message = f"Syntax error: unexpected token '{p.value}' at line {p.lineno}"
    else:
        error_message = "Syntax error: unexpected end of input."
    error_list.append(error_message)
    print(error_message)

def analysing(input_string):
    error_list.clear()
    result = parser.parse(input_string)
    return error_list if error_list else result

# Construcción del parser
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


# Llamada a método de comparación\n
puts resultado  # Imprime "Mayor que 10"\n\n

# Uso de operador lógico\n
edad_valida = true # Verificando que la persona sea mayor de edad y activa\n\n

puts "Edad válida y activo: #{edad_valida}"\n
'''


# Algoritmo Alina Carpio
ruby_code_2 = '''# Clase Estudiante que contiene información básica de cada estudiante\n
class Estudiante\n
  # Constructor para inicializar los atributos de la clase\n
  def initialize(nombre, edad, promedio, materias)\n
    @nombre = nombre               # String\n
    @edad = edad                   # Integer\n
    @promedio = promedio           # Float\n
    @materias = materias           # Array de strings\n
  end\n

  # Método para obtener información del estudiante\n
  def mostrar_informacion\n
    puts "Nombre: #{@nombre}"\n
    puts "Edad: #{@edad}"\n
    puts "Promedio: #{@promedio}"\n
  end\n
end\n

# Hash para almacenar estudiantes por su ID (como clave)\n
estudiantes = {}\n

# Método para calcular el promedio general de todos los estudiantes\n
def calcular_promedio_general(estudiantes)\n
  total = 0\n

  promedio_general = total / estudiantes.size\n
  puts "Promedio general de la clase: #{promedio_general}"\n
end\n

# Llamada al método para calcular el promedio general\n
calcular_promedio_general(estudiantes)\n
'''

code_3 = '''
@@@cualquiercosa
'''

result = analysing(code_3)
loger.create_log(lexer, "bryanestrada003", code_3, lx.error_list)
loger.create_syntactic_log(parser, "bryanestrada003", code_3, error_list)
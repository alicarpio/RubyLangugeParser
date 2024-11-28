import ply.yacc as yacc
from Lexer import tokens
from Lexer import data
import Logs as loger
import Lexer as lx
from Lexer import lexer
import Logs as loger

declared_variables = set()
error_list = []


def p_program(p):
    'program : code_list'

def p_code_list(p):
    '''code_list : code
                 | code code_list'''

def p_code(p):
    '''code : variable_assignment
            | impresion
            | if_statement
            | while_statement
            | for_statement
            | until_statement
            | solicitud_entrada
            | call_expression
            | function_definition'''

def p_variable_assignment(p):
    '''variable_assignment : NAME EQUALS valor
                           | VARIABLE_GLOBAL EQUALS valor
                           | VARIABLE_INSTANCIA EQUALS valor
                           | VARIABLE_LOCAL EQUALS valor
                           | VARIABLE_CONSTANTE EQUALS STRING'''
    variable_name = p[1]
    declared_variables.add(variable_name)

def p_call_expresion(p):
    '''call_expression : NAME LPAREN arguments_opt RPAREN
                       | NAME DOT NAME LPAREN arguments_opt RPAREN
                       | NAME DOT NAME'''

def p_impresion(p):
    '''impresion : PUTS arguments_opt'''

def p_solicitud_entrada(p):
    '''solicitud_entrada : PUTS STRING
                         | NAME EQUALS GETS DOT CHOMP
    '''

def p_arguments_opt(p):
    '''arguments_opt : argumentos
                      | empty'''

def p_argumentos(p):
    '''argumentos : valor
                  | valor COMA argumentos'''

def p_arguments_opt_func(p):
    '''arguments_opt_func : arg_func
                         | empty'''

def p_arg_func(p):
    '''arg_func : NAME
                | NAME COMA arg_func'''

def p_valor(p):
    '''valor : operand
             | STRING
             | NULL
             | SYMBOL
             | boolean
             | lists
             | operation
             | condition
             | concatenar_strings
             | hash
             | call_expression'''


def p_operand(p):
    '''operand : INTEGER
               | FLOAT
               | NAME'''

    if isinstance(p[1], str):  # Verificar si es una variable (nombre)
        variable_name = p[1]

        # Validar que la variable haya sido declarada
        if variable_name not in declared_variables:
            error_list.append(f"Error: Uso de variable no declarada {variable_name}")


def p_operatorArithm(p):
    '''operatorArithm : MULTIPLY
                | DIVIDE
                | MODULE'''

def p_power_op(p):
    '''power_op : INTEGER POWER INTEGER'''

def p_concatenar_strings(p):
    '''concatenar_strings : STRING PLUS STRING'''

def p_sum_of_integers(p):
    '''sum_of_integers : INTEGER PLUS INTEGER'''

def p_subtraction_of_integers(p):
    '''subtraction_of_integers : INTEGER MINUS INTEGER'''

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
                 | sum_of_integers
                 | subtraction_of_integers
                 | operand operatorArithm operation'''


def p_if_statement(p):
    '''
    if_statement : IF condition statement_block END
                 | IF condition statement_block ELSE statement_block END
                 | IF condition statement_block ELSIF condition statement_block END
                 | IF condition statement_block ELSIF condition statement_block ELSE statement_block END'''

def p_while_statement(p):
    '''while_statement : WHILE condition statement_block END'''

def p_for_statement(p):
    '''for_statement : FOR NAME IN NAME DO statement_block END'''

def p_until_statement(p):
    '''until_statement : UNTIL condition DO statement_block END'''


def p_comparison_integer(p):
    '''comparison_integer : INTEGER comparator INTEGER'''


def p_statement_block(p):
    '''statement_block : statement
                       | statement statement_block'''


def p_statement(p):
    ''' statement : variable_assignment
                  | impresion
                  | if_statement
                  | while_statement
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

def p_function_definition(p):
    '''function_definition : DEF NAME LPAREN arguments_opt_func RPAREN body END'''

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

def p_body(p):
    '''
    body : statement
         | statement body
    '''

# Manejo de errores
error_list = []
def p_error(p):
    if p:
        error_message = f"Syntax error: '{p.value}' in line {p.lineno}"
    else:
        error_message = "Syntactic: Unexpected end of input"
    error_list.append(error_message)
    print(error_message)

def analysing(input_string):
    error_list.clear()
    result = parser.parse(input_string)
    return error_list if error_list else result

# Construcción del parser
parser = yacc.yacc()

# Algoritmo Michael Estrada

code_1 = '''
# Declaración de variables
x = 10
y = 20
result = 0

# Condicional
if x < y
  result = x + y
elsif x == y
  result = x * y
else
  result = x - y
end

# Impresión del resultado
puts "Resultado: #{result}"

# Bucle 'while'
counter = 0
while counter < 5
  puts "Contador: #{counter}"
  counter += 1
end

numeros = [1, 2, 3, 4, 5]

for numero in numeros do
  puts "Número: #{numero}"
end
'''

code_2 = '''
# Definición de una función
def calcular_promedio(numeros)
  suma = 0
  promedio = suma / numeros.length
  return promedio
end

# Declaración de un arreglo
numeros = [10, 20, 30, 40, 50]

# Uso de la función
promedio = calcular_promedio(numeros)
puts "El promedio es: #{promedio}"

# Declaración de un hash
persona = { nombre: "Juan", edad: 30, profesion: "Ingeniero" }
puts "Información de la persona:"

until index < 0
  puts "Número invertido: #{numeros[index]}"
  index = index - 1
end
'''

result = analysing(code_2)
loger.create_log(lexer, "alicarpio", code_2, lx.error_list)
loger.create_syntactic_log(parser, "alicarpio", code_2, error_list)
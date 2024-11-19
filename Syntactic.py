import ply.yacc as yacc
from Lexer import tokens
from Lexer import data
import Logs as loger
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

error_list = []
def p_error(p):
    if p:
        error_message = f"Syntax error: unexpected token '{p.value}' at line {p.lineno}"
    else:
        error_message = "Syntax error: unexpected end of input."
    error_list.append(error_message)
    print(error_message)

# Construcción del parser
parser = yacc.yacc()
ex1 = '''
var = 5
'''
# Ciclo interactivo para probar entradas
while True:
    try:
        s = input('ruby > ')
    except EOFError:
        break
    if not s:
        continue
    error_list.clear()
    result = parser.parse(s)
    print(result)

    loger.create_syntactic_log(parser,"bryanestrada003",s,error_list)

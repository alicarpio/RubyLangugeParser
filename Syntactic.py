import ply.yacc as yacc
from Lexer import tokens

def p_asignacion(p):
    'asignacion : VARIABLE_LOCAL EQUALS valor'

def p_valor(p):
    '''valor : STRING
             | INTEGER
             | FLOAT
             | VARIABLE_LOCAL'''

# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis :c")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('ruby > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

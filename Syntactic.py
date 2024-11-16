import ply.yacc as yacc
from Lexer import tokens

def p_asignacion(p):
    'asignacion : VARIABLE_LOCAL EQUALS valor'
    p[0] = (p[1], p[2], p[3])  # Ejemplo de acción semántica para esta regla

def p_valor(p):
    '''valor : STRING
             | INTEGER
             | FLOAT
             | VARIABLE_LOCAL'''
    p[0] = p[1]  # Asignar el valor reconocido al elemento de la pila semántica

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

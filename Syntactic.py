import ply.yacc as yacc
from Lexer import tokens
from Lexer import data
import Logs as loger
from Lexer import lexer

# Reglas de la gramática
def p_program(p):
    '''program : code
               | code program'''

def p_code(p):
    '''code : asignacion
            | impresion'''

# Reglas de la gramática
def p_asignacion(p):
    'asignacion : NAME EQUALS valor'

def p_impresion(p):
    'impresion : PUTS argumentos_opt'

def p_argumentos_opt(p):
    '''argumentos_opt : argumentos
                      | empty'''

def p_argumentos(p):
    '''argumentos : valor
                  | valor COMA argumentos'''

def p_valor(p):
    '''valor : STRING
             | INTEGER
             | FLOAT
             | NULL
             | NAME
             | boolean
             | lists
             | operation
             | condition'''

def p_lists(p):
    '''lists : LBRACKET argumentos RBRACKET
             | LSQBRACKET argumentos RSQBRACKET'''

def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''

def p_operation(p):
    '''operation : operand operatorArithm operand
                 | operand operatorArithm operation'''

def p_operand(p):
    '''operand : INTEGER
               | FLOAT'''

def p_operatorArithm(p):
    '''operatorArithm : PLUS
                | MINUS
                | MULTIPLY'''

def p_condition(p):
    '''condition : cond
                 | NOT_OP cond
                 | cond operatorCond cond
                 | cond operatorCond condition'''

def p_operatorCond(p):
    '''operatorCond : AND_OP
                    | OR_OP'''

def p_cond(p):
    '''cond : valor comparator valor'''

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
resultado = evaluar_numero(12)  # Evaluando si el número es mayor que 10

# Iteración sobre el hash
persona.each do |clave, valor|
  if clave.is_a?(String)
    puts "Clave (String): #{clave} => Valor: #{valor}"
  else
    puts "Clave (Symbol): #{clave} => Valor: #{valor}"
  end
end

# Llamada a método de comparación
puts resultado  # Imprime "Mayor que 10"

# Uso de operador lógico
edad_valida = persona["edad"] >= 18 && persona["activo"] == true  # Verificando que la persona sea mayor de edad y activa

puts "Edad válida y activo: #{edad_valida}"

# Intento de una operación lógica mal formada (error sintáctico)
# puts "Resultado: " && "Error en el operador lógico" (Esto generaría un error porque el operador && no tiene sentido aquí)
'''
# Ciclo interactivo para probar entradas
while True:
    try:
        s = input('ruby > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)

loger.create_log(parser, "bryanestrada003", data, error_list, "sintactico")

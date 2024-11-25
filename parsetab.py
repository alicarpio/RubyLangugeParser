
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND_OP CASE CHOMP CLASS CLASS_NAME COLON COMA COMMENT DEF DIVIDE DO DOT EACH ELSE ELSIF END EQ EQUALS FALSE FLOAT FOR GE GETS GT HASHROCKET IF INITIALIZE INTEGER LBRACKET LE LPAREN LSQBRACKET LT MINUS MODULE MULTIPLY NAME NE NEW NEWLINE NOT_OP NULL OR_OP PIPE PLUS POWER PUTS RBRACKET RETURN RPAREN RSQBRACKET SEMICOLON STRING SYMBOL TRUE UNLESS UNTIL VARIABLE_CLASE VARIABLE_CONSTANTE VARIABLE_GLOBAL VARIABLE_INSTANCIA VARIABLE_LOCAL WHEN WHILEprogram : code_listcode_list : code\n                 | code code_listcode : asignacion\n            | impresion\n            | if_statement\n            | while_statement\n            | instantiation\n            | solicitud_entrada\n            | function_definition\n            | class_definitionasignacion : NAME EQUALS valor\n                  | VARIABLE_GLOBAL EQUALS valor\n                  | VARIABLE_CLASE EQUALS valor\n                  | VARIABLE_INSTANCIA EQUALS valor\n                  | VARIABLE_LOCAL EQUALS valorfunc_call : NAME LPAREN argumentos_opt RPARENimpresion : PUTS argumentos_optsolicitud_entrada : PUTS STRING\n                         | NAME EQUALS GETS DOT CHOMP\n    argumentos_opt : argumentos\n                      | emptyargumentos : valor\n                  | valor COMA argumentosvalor : operand\n             | STRING\n             | NULL\n             | SYMBOL\n             | boolean\n             | lists\n             | operation\n             | condition\n             | expression\n             | hash\n             | func_call\n             | method_callexpression : expression operatorArithm operand\n                  | operandoperand : INTEGER\n               | FLOAT\n               | NAMEoperatorArithm : PLUS\n                | MINUS\n                | MULTIPLY\n                | DIVIDE\n                | MODULE\n                power_op : INTEGER POWER INTEGERlists : LBRACKET argumentos RBRACKET\n             | LSQBRACKET argumentos RSQBRACKEThash : LBRACKET pares_hash RBRACKET\n            | LBRACKET empty RBRACKETpares_hash : par_hash\n                  | par_hash COMA pares_hashpar_hash : clave HASHROCKET valor\n                | clave COLON valorclave : SYMBOL\n             | STRINGboolean : TRUE\n                | FALSEoperation : operand operatorArithm operand\n                 | operand operatorArithm operation\n    if_statement : IF condition block END\n                 | IF condition block ELSE block END\n                 | IF condition block ELSIF condition block END\n                 | IF condition block ELSIF condition block ELSE block ENDwhile_statement : WHILE condition block ENDcomparison : valor comparator valor block : statement\n              | statement block statement : asignacion\n                  | impresion\n                  | if_statement\n                  | while_statement\n                  | instantiation\n                  | returnreturn : RETURN argumentoscondition : comparison\n                 | boolean\n                 | NOT_OP comparison\n                 | comparison operatorCond comparisonoperatorCond : AND_OP\n                    | OR_OPcond : valor comparator valor\n            | LPAREN comparison RPARENclass_definition : CLASS CLASS_NAME class_body ENDclass_body : empty\n                  | constructor_definition\n                  | class_body_element_listconstructor_definition : DEF INITIALIZE LPAREN parameters RPAREN body ENDclass_body_element_list : class_body_element\n                               | class_body_element class_body_element_listclass_body_element : asignacion\n                          | function_definition\n                          | function_def_no_paramsfunction_definition : DEF NAME LPAREN parameters RPAREN body ENDfunction_def_no_params : DEF NAME body ENDmethod_call : NAME DOT NAME LPAREN argumentos_opt RPAREN\n                   | NAME DOT NAME\n    instantiation : CLASS_NAME NEW LPAREN argumentos RPAREN\n    comparator : EQ\n                  | NE\n                  | LT\n                  | LE\n                  | GT\n                  | GEempty :\n    parameters : NAME\n               | NAME COMA parameters\n               | empty\n    \n    body : statement\n         | statement body\n    '
    
_lr_action_items = {'NAME':([0,3,4,5,6,7,8,9,10,11,17,18,19,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,93,94,95,96,98,99,100,101,102,103,104,106,107,109,110,115,116,117,118,119,121,122,123,124,125,126,128,129,130,131,133,134,135,136,137,138,139,141,142,143,148,150,152,153,154,155,162,163,164,165,166,168,170,175,177,178,179,180,181,184,],[12,12,-4,-5,-6,-7,-8,-9,-10,-11,47,47,47,60,47,47,47,47,47,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,47,47,-77,47,105,-78,-26,105,105,-12,-13,-14,-15,-16,47,47,-100,-101,-102,-103,-104,-105,125,-42,-43,-44,-45,-46,125,47,128,47,-81,-82,-79,105,-70,-71,-72,-73,-74,-75,47,47,47,145,150,105,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,47,47,-49,-80,-62,105,47,47,-76,-66,-85,105,150,-20,-17,47,105,-99,145,105,145,105,-63,-96,-97,-64,105,-95,105,-65,]),'VARIABLE_GLOBAL':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,61,62,64,65,66,67,96,98,99,100,101,102,103,104,106,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,175,177,178,179,180,181,184,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,13,-78,-26,13,13,-12,-13,-14,-15,-16,-79,13,-70,-71,-72,-73,-74,-75,-106,13,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,13,-76,-66,-85,13,-20,-17,13,-99,13,13,-63,-96,-97,-64,13,-95,13,-65,]),'VARIABLE_CLASE':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,61,62,64,65,66,67,96,98,99,100,101,102,103,104,106,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,175,177,178,179,180,181,184,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,14,-78,-26,14,14,-12,-13,-14,-15,-16,-79,14,-70,-71,-72,-73,-74,-75,-106,14,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,14,-76,-66,-85,14,-20,-17,14,-99,14,14,-63,-96,-97,-64,14,-95,14,-65,]),'VARIABLE_INSTANCIA':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,61,62,64,65,66,67,96,98,99,100,101,102,103,104,106,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,175,177,178,179,180,181,184,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,15,-78,-26,15,15,-12,-13,-14,-15,-16,-79,15,-70,-71,-72,-73,-74,-75,-106,15,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,15,-76,-66,-85,15,-20,-17,15,-99,15,15,-63,-96,-97,-64,15,-95,15,-65,]),'VARIABLE_LOCAL':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,61,62,64,65,66,67,96,98,99,100,101,102,103,104,106,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,175,177,178,179,180,181,184,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,16,-78,-26,16,16,-12,-13,-14,-15,-16,-79,16,-70,-71,-72,-73,-74,-75,-106,16,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,16,-76,-66,-85,16,-20,-17,16,-99,16,16,-63,-96,-97,-64,16,-95,16,-65,]),'PUTS':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,62,64,65,66,67,96,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,177,178,179,180,181,184,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,106,-78,-26,106,-12,-13,-14,-15,-16,-79,106,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,106,-76,-66,-85,106,-20,-17,106,-99,106,106,-63,-97,-64,106,-95,106,-65,]),'IF':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,62,64,65,66,67,96,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,177,178,179,180,181,184,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,18,-78,-26,18,-12,-13,-14,-15,-16,-79,18,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,18,-76,-66,-85,18,-20,-17,18,-99,18,18,-63,-97,-64,18,-95,18,-65,]),'WHILE':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,62,64,65,66,67,96,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,177,178,179,180,181,184,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,19,-78,-26,19,-12,-13,-14,-15,-16,-79,19,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,19,-76,-66,-85,19,-20,-17,19,-99,19,19,-63,-97,-64,19,-95,19,-65,]),'CLASS_NAME':([0,3,4,5,6,7,8,9,10,11,17,22,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,62,64,65,66,67,96,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,148,150,153,154,162,163,165,168,170,177,178,179,180,181,184,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-106,61,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,20,-78,-26,20,-12,-13,-14,-15,-16,-79,20,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,20,-76,-66,-85,20,-20,-17,20,-99,20,20,-63,-97,-64,20,-95,20,-65,]),'DEF':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,61,62,64,65,66,67,96,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,143,148,153,154,163,170,175,177,178,180,184,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,115,-12,-13,-14,-15,-16,-79,152,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-66,-85,-20,-17,-99,-63,-96,-97,-64,-95,-65,]),'CLASS':([0,3,4,5,6,7,8,9,10,11,17,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,62,64,65,66,67,96,121,122,123,124,125,126,128,129,130,131,135,136,137,143,148,153,154,163,170,177,178,180,184,],[22,22,-4,-5,-6,-7,-8,-9,-10,-11,-106,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-12,-13,-14,-15,-16,-79,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-66,-85,-20,-17,-99,-63,-97,-64,-95,-65,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,17,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,62,64,65,66,67,96,121,122,123,124,125,126,128,129,130,131,135,136,137,143,148,153,154,163,170,177,178,180,184,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-106,-3,-18,-19,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-12,-13,-14,-15,-16,-79,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-66,-85,-20,-17,-99,-63,-97,-64,-95,-65,]),'EQUALS':([12,13,14,15,16,105,],[24,25,26,27,28,141,]),'STRING':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,132,133,134,139,141,155,],[30,57,57,57,57,57,57,57,89,57,57,57,57,-100,-101,-102,-103,-104,-105,57,57,-81,-82,57,57,57,158,57,57,57,57,57,]),'NULL':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[35,35,35,35,35,35,35,35,35,35,35,35,35,-100,-101,-102,-103,-104,-105,35,35,-81,-82,35,35,35,35,35,35,35,35,]),'SYMBOL':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,132,133,134,139,141,155,],[36,36,36,36,36,36,36,36,90,36,36,36,36,-100,-101,-102,-103,-104,-105,36,36,-81,-82,36,36,36,157,36,36,36,36,36,]),'INTEGER':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,106,107,109,133,134,139,141,155,],[45,45,45,45,45,45,45,45,45,45,45,45,45,-100,-101,-102,-103,-104,-105,45,-42,-43,-44,-45,-46,45,45,45,-81,-82,45,45,45,45,45,45,45,45,]),'FLOAT':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,93,94,95,106,107,109,133,134,139,141,155,],[46,46,46,46,46,46,46,46,46,46,46,46,46,-100,-101,-102,-103,-104,-105,46,-42,-43,-44,-45,-46,46,46,46,-81,-82,46,46,46,46,46,46,46,46,]),'TRUE':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[48,48,48,48,48,48,48,48,48,48,48,48,48,-100,-101,-102,-103,-104,-105,48,48,-81,-82,48,48,48,48,48,48,48,48,]),'FALSE':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[49,49,49,49,49,49,49,49,49,49,49,49,49,-100,-101,-102,-103,-104,-105,49,49,-81,-82,49,49,49,49,49,49,49,49,]),'LBRACKET':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[50,50,50,50,50,50,50,50,50,50,50,50,50,-100,-101,-102,-103,-104,-105,50,50,-81,-82,50,50,50,50,50,50,50,50,]),'LSQBRACKET':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[51,51,51,51,51,51,51,51,51,51,51,51,51,-100,-101,-102,-103,-104,-105,51,51,-81,-82,51,51,51,51,51,51,51,51,]),'NOT_OP':([17,18,19,24,25,26,27,28,50,51,53,68,69,70,71,72,73,74,75,83,93,94,95,106,107,109,133,134,139,141,155,],[53,53,53,53,53,53,53,53,53,53,53,53,53,-100,-101,-102,-103,-104,-105,53,53,-81,-82,53,53,53,53,53,53,53,53,]),'NEW':([20,],[59,]),'GETS':([24,],[63,]),'RETURN':([29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,57,58,62,64,65,66,67,96,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,138,142,143,150,154,162,163,165,168,170,177,178,179,181,184,],[-18,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,107,-78,-26,107,-12,-13,-14,-15,-16,-79,107,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,107,-76,-66,107,-17,107,-99,107,107,-63,-97,-64,107,107,-65,]),'END':([29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,61,62,64,65,66,67,96,97,98,99,100,101,102,103,104,106,108,111,112,113,114,116,117,118,119,121,122,123,124,125,126,128,129,130,131,135,136,137,140,142,143,151,154,161,163,167,168,170,171,173,175,176,177,178,180,182,183,184,185,],[-18,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-106,-12,-13,-14,-15,-16,-79,137,-68,-70,-71,-72,-73,-74,-75,-106,143,148,-86,-87,-88,-90,-92,-93,-94,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-69,-76,-66,-91,-17,170,-99,175,-110,-63,178,180,-96,-111,-97,-64,-95,184,185,-65,-89,]),'ELSE':([29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,62,64,65,66,67,96,97,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,140,142,143,154,163,170,171,177,178,184,],[-18,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-12,-13,-14,-15,-16,-79,138,-68,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-69,-76,-66,-17,-99,-63,179,-97,-64,-65,]),'ELSIF':([29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,62,64,65,66,67,96,97,98,99,100,101,102,103,104,106,121,122,123,124,125,126,128,129,130,131,135,136,137,140,142,143,154,163,170,177,178,184,],[-18,-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-12,-13,-14,-15,-16,-79,139,-68,-70,-71,-72,-73,-74,-75,-106,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-62,-69,-76,-66,-17,-99,-63,-97,-64,-65,]),'COMA':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,88,89,90,96,122,123,124,125,126,128,129,130,131,135,136,145,154,159,160,177,],[-26,68,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,132,-26,-28,-79,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,164,-17,-54,-55,-97,]),'EQ':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,70,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,70,-26,-32,70,70,70,70,70,-26,-28,-77,70,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,70,70,-32,-97,]),'NE':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,71,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,71,-26,-32,71,71,71,71,71,-26,-28,-77,71,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,71,71,-32,-97,]),'LT':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,72,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,72,-26,-32,72,72,72,72,72,-26,-28,-77,72,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,72,72,-32,-97,]),'LE':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,73,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,73,-26,-32,73,73,73,73,73,-26,-28,-77,73,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,73,73,-32,-97,]),'GT':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,74,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,74,-26,-32,74,74,74,74,74,-26,-28,-77,74,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,74,74,-32,-97,]),'GE':([30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,54,55,56,57,58,62,64,65,66,67,89,90,96,122,123,124,125,126,128,129,130,131,135,136,154,159,160,162,177,],[-26,75,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-32,-29,75,-26,-32,75,75,75,75,75,-26,-28,-77,75,-60,-61,-41,-37,-98,-48,-50,-51,-49,-77,-17,75,75,-32,-97,]),'RPAREN':([31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,83,96,110,121,122,123,124,125,126,127,128,129,130,131,135,136,144,145,146,147,154,155,164,166,169,172,174,177,],[-21,-22,-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,-106,-79,-106,-24,-67,-60,-61,-41,-37,154,-98,-48,-50,-51,-49,-80,163,-107,165,-109,-17,-106,-106,-106,177,-108,181,-97,]),'RBRACKET':([33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,57,85,86,87,88,89,90,96,121,122,123,124,125,126,128,129,130,131,135,136,154,156,159,160,177,],[-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-106,-77,-26,129,130,131,-52,-26,-28,-79,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-17,-53,-54,-55,-97,]),'RSQBRACKET':([33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,92,96,121,122,123,124,125,126,128,129,130,131,135,136,154,177,],[-23,-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,-77,-26,135,-79,-24,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,-80,-17,-97,]),'AND_OP':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,96,122,123,124,125,126,128,129,130,131,135,136,154,177,],[-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,94,-26,94,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,94,-17,-97,]),'OR_OP':([34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,52,57,96,122,123,124,125,126,128,129,130,131,135,136,154,177,],[-25,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-39,-40,-41,-58,-59,95,-26,95,-67,-60,-61,-41,-37,-98,-48,-50,-51,-49,95,-17,-97,]),'PLUS':([34,41,45,46,47,123,125,126,],[77,77,-39,-40,-41,77,-41,-37,]),'MINUS':([34,41,45,46,47,123,125,126,],[78,78,-39,-40,-41,78,-41,-37,]),'MULTIPLY':([34,41,45,46,47,123,125,126,],[79,79,-39,-40,-41,79,-41,-37,]),'DIVIDE':([34,41,45,46,47,123,125,126,],[80,80,-39,-40,-41,80,-41,-37,]),'MODULE':([34,41,45,46,47,123,125,126,],[81,81,-39,-40,-41,81,-41,-37,]),'LPAREN':([47,59,60,128,149,150,],[83,109,110,155,166,110,]),'DOT':([47,63,],[84,120,]),'HASHROCKET':([89,90,91,157,158,],[-57,-56,133,-56,-57,]),'COLON':([89,90,91,157,158,],[-57,-56,134,-56,-57,]),'INITIALIZE':([115,],[149,]),'CHOMP':([120,],[153,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'code_list':([0,3,],[2,23,]),'code':([0,3,],[3,3,]),'asignacion':([0,3,54,58,61,98,116,138,150,162,165,168,179,181,],[4,4,99,99,117,99,117,99,99,99,99,99,99,99,]),'impresion':([0,3,54,58,98,138,150,162,165,168,179,181,],[5,5,100,100,100,100,100,100,100,100,100,100,]),'if_statement':([0,3,54,58,98,138,150,162,165,168,179,181,],[6,6,101,101,101,101,101,101,101,101,101,101,]),'while_statement':([0,3,54,58,98,138,150,162,165,168,179,181,],[7,7,102,102,102,102,102,102,102,102,102,102,]),'instantiation':([0,3,54,58,98,138,150,162,165,168,179,181,],[8,8,103,103,103,103,103,103,103,103,103,103,]),'solicitud_entrada':([0,3,],[9,9,]),'function_definition':([0,3,61,116,],[10,10,118,118,]),'class_definition':([0,3,],[11,11,]),'argumentos_opt':([17,83,106,155,],[29,127,29,169,]),'argumentos':([17,50,51,68,83,106,107,109,155,],[31,85,92,121,31,31,142,144,31,]),'empty':([17,50,61,83,106,110,155,164,166,],[32,87,112,32,32,147,32,147,147,]),'valor':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[33,56,56,62,64,65,66,67,33,33,56,33,122,33,56,33,33,33,159,160,56,62,33,]),'operand':([17,18,19,24,25,26,27,28,50,51,53,68,69,76,82,83,93,106,107,109,133,134,139,141,155,],[34,34,34,34,34,34,34,34,34,34,34,34,34,123,126,34,34,34,34,34,34,34,34,34,34,]),'boolean':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[37,55,55,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,55,37,37,]),'lists':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'operation':([17,18,19,24,25,26,27,28,50,51,53,68,69,76,83,93,106,107,109,133,134,139,141,155,],[39,39,39,39,39,39,39,39,39,39,39,39,39,124,39,39,39,39,39,39,39,39,39,39,]),'condition':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[40,54,58,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,162,40,40,]),'expression':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'hash':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'func_call':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'method_call':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'comparison':([17,18,19,24,25,26,27,28,50,51,53,68,69,83,93,106,107,109,133,134,139,141,155,],[52,52,52,52,52,52,52,52,52,52,96,52,52,52,136,52,52,52,52,52,52,52,52,]),'comparator':([33,56,62,64,65,66,67,122,159,160,],[69,69,69,69,69,69,69,69,69,69,]),'operatorArithm':([34,41,123,],[76,82,76,]),'pares_hash':([50,132,],[86,156,]),'par_hash':([50,132,],[88,88,]),'clave':([50,132,],[91,91,]),'operatorCond':([52,96,136,],[93,93,93,]),'block':([54,58,98,138,162,179,],[97,108,140,161,171,182,]),'statement':([54,58,98,138,150,162,165,168,179,181,],[98,98,98,98,168,98,168,168,98,168,]),'return':([54,58,98,138,150,162,165,168,179,181,],[104,104,104,104,104,104,104,104,104,104,]),'class_body':([61,],[111,]),'constructor_definition':([61,],[113,]),'class_body_element_list':([61,116,],[114,151,]),'class_body_element':([61,116,],[116,116,]),'function_def_no_params':([61,116,],[119,119,]),'parameters':([110,164,166,],[146,172,174,]),'body':([150,165,168,181,],[167,173,176,183,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> code_list','program',1,'p_program','Syntactic.py',11),
  ('code_list -> code','code_list',1,'p_code_list','Syntactic.py',14),
  ('code_list -> code code_list','code_list',2,'p_code_list','Syntactic.py',15),
  ('code -> asignacion','code',1,'p_code','Syntactic.py',19),
  ('code -> impresion','code',1,'p_code','Syntactic.py',20),
  ('code -> if_statement','code',1,'p_code','Syntactic.py',21),
  ('code -> while_statement','code',1,'p_code','Syntactic.py',22),
  ('code -> instantiation','code',1,'p_code','Syntactic.py',23),
  ('code -> solicitud_entrada','code',1,'p_code','Syntactic.py',24),
  ('code -> function_definition','code',1,'p_code','Syntactic.py',25),
  ('code -> class_definition','code',1,'p_code','Syntactic.py',26),
  ('asignacion -> NAME EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',31),
  ('asignacion -> VARIABLE_GLOBAL EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',32),
  ('asignacion -> VARIABLE_CLASE EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',33),
  ('asignacion -> VARIABLE_INSTANCIA EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',34),
  ('asignacion -> VARIABLE_LOCAL EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',35),
  ('func_call -> NAME LPAREN argumentos_opt RPAREN','func_call',4,'p_func_call','Syntactic.py',38),
  ('impresion -> PUTS argumentos_opt','impresion',2,'p_impresion','Syntactic.py',41),
  ('solicitud_entrada -> PUTS STRING','solicitud_entrada',2,'p_solicitud_entrada','Syntactic.py',44),
  ('solicitud_entrada -> NAME EQUALS GETS DOT CHOMP','solicitud_entrada',5,'p_solicitud_entrada','Syntactic.py',45),
  ('argumentos_opt -> argumentos','argumentos_opt',1,'p_argumentos_opt','Syntactic.py',49),
  ('argumentos_opt -> empty','argumentos_opt',1,'p_argumentos_opt','Syntactic.py',50),
  ('argumentos -> valor','argumentos',1,'p_argumentos','Syntactic.py',53),
  ('argumentos -> valor COMA argumentos','argumentos',3,'p_argumentos','Syntactic.py',54),
  ('valor -> operand','valor',1,'p_valor','Syntactic.py',57),
  ('valor -> STRING','valor',1,'p_valor','Syntactic.py',58),
  ('valor -> NULL','valor',1,'p_valor','Syntactic.py',59),
  ('valor -> SYMBOL','valor',1,'p_valor','Syntactic.py',60),
  ('valor -> boolean','valor',1,'p_valor','Syntactic.py',61),
  ('valor -> lists','valor',1,'p_valor','Syntactic.py',62),
  ('valor -> operation','valor',1,'p_valor','Syntactic.py',63),
  ('valor -> condition','valor',1,'p_valor','Syntactic.py',64),
  ('valor -> expression','valor',1,'p_valor','Syntactic.py',65),
  ('valor -> hash','valor',1,'p_valor','Syntactic.py',66),
  ('valor -> func_call','valor',1,'p_valor','Syntactic.py',67),
  ('valor -> method_call','valor',1,'p_valor','Syntactic.py',68),
  ('expression -> expression operatorArithm operand','expression',3,'p_expression','Syntactic.py',71),
  ('expression -> operand','expression',1,'p_expression','Syntactic.py',72),
  ('operand -> INTEGER','operand',1,'p_operand','Syntactic.py',75),
  ('operand -> FLOAT','operand',1,'p_operand','Syntactic.py',76),
  ('operand -> NAME','operand',1,'p_operand','Syntactic.py',77),
  ('operatorArithm -> PLUS','operatorArithm',1,'p_operatorArithm','Syntactic.py',81),
  ('operatorArithm -> MINUS','operatorArithm',1,'p_operatorArithm','Syntactic.py',82),
  ('operatorArithm -> MULTIPLY','operatorArithm',1,'p_operatorArithm','Syntactic.py',83),
  ('operatorArithm -> DIVIDE','operatorArithm',1,'p_operatorArithm','Syntactic.py',84),
  ('operatorArithm -> MODULE','operatorArithm',1,'p_operatorArithm','Syntactic.py',85),
  ('power_op -> INTEGER POWER INTEGER','power_op',3,'p_power_op','Syntactic.py',90),
  ('lists -> LBRACKET argumentos RBRACKET','lists',3,'p_lists','Syntactic.py',93),
  ('lists -> LSQBRACKET argumentos RSQBRACKET','lists',3,'p_lists','Syntactic.py',94),
  ('hash -> LBRACKET pares_hash RBRACKET','hash',3,'p_hash','Syntactic.py',97),
  ('hash -> LBRACKET empty RBRACKET','hash',3,'p_hash','Syntactic.py',98),
  ('pares_hash -> par_hash','pares_hash',1,'p_pares_hash','Syntactic.py',101),
  ('pares_hash -> par_hash COMA pares_hash','pares_hash',3,'p_pares_hash','Syntactic.py',102),
  ('par_hash -> clave HASHROCKET valor','par_hash',3,'p_par_hash','Syntactic.py',105),
  ('par_hash -> clave COLON valor','par_hash',3,'p_par_hash','Syntactic.py',106),
  ('clave -> SYMBOL','clave',1,'p_clave','Syntactic.py',111),
  ('clave -> STRING','clave',1,'p_clave','Syntactic.py',112),
  ('boolean -> TRUE','boolean',1,'p_boolean','Syntactic.py',116),
  ('boolean -> FALSE','boolean',1,'p_boolean','Syntactic.py',117),
  ('operation -> operand operatorArithm operand','operation',3,'p_operation','Syntactic.py',121),
  ('operation -> operand operatorArithm operation','operation',3,'p_operation','Syntactic.py',122),
  ('if_statement -> IF condition block END','if_statement',4,'p_if_statement','Syntactic.py',127),
  ('if_statement -> IF condition block ELSE block END','if_statement',6,'p_if_statement','Syntactic.py',128),
  ('if_statement -> IF condition block ELSIF condition block END','if_statement',7,'p_if_statement','Syntactic.py',129),
  ('if_statement -> IF condition block ELSIF condition block ELSE block END','if_statement',9,'p_if_statement','Syntactic.py',130),
  ('while_statement -> WHILE condition block END','while_statement',4,'p_while_statement','Syntactic.py',134),
  ('comparison -> valor comparator valor','comparison',3,'p_comparison','Syntactic.py',137),
  ('block -> statement','block',1,'p_block','Syntactic.py',140),
  ('block -> statement block','block',2,'p_block','Syntactic.py',141),
  ('statement -> asignacion','statement',1,'p_statement','Syntactic.py',144),
  ('statement -> impresion','statement',1,'p_statement','Syntactic.py',145),
  ('statement -> if_statement','statement',1,'p_statement','Syntactic.py',146),
  ('statement -> while_statement','statement',1,'p_statement','Syntactic.py',147),
  ('statement -> instantiation','statement',1,'p_statement','Syntactic.py',148),
  ('statement -> return','statement',1,'p_statement','Syntactic.py',149),
  ('return -> RETURN argumentos','return',2,'p_return','Syntactic.py',152),
  ('condition -> comparison','condition',1,'p_condition','Syntactic.py',155),
  ('condition -> boolean','condition',1,'p_condition','Syntactic.py',156),
  ('condition -> NOT_OP comparison','condition',2,'p_condition','Syntactic.py',157),
  ('condition -> comparison operatorCond comparison','condition',3,'p_condition','Syntactic.py',158),
  ('operatorCond -> AND_OP','operatorCond',1,'p_operatorCond','Syntactic.py',161),
  ('operatorCond -> OR_OP','operatorCond',1,'p_operatorCond','Syntactic.py',162),
  ('cond -> valor comparator valor','cond',3,'p_cond','Syntactic.py',165),
  ('cond -> LPAREN comparison RPAREN','cond',3,'p_cond','Syntactic.py',166),
  ('class_definition -> CLASS CLASS_NAME class_body END','class_definition',4,'p_class_definition','Syntactic.py',170),
  ('class_body -> empty','class_body',1,'p_class_body','Syntactic.py',174),
  ('class_body -> constructor_definition','class_body',1,'p_class_body','Syntactic.py',175),
  ('class_body -> class_body_element_list','class_body',1,'p_class_body','Syntactic.py',176),
  ('constructor_definition -> DEF INITIALIZE LPAREN parameters RPAREN body END','constructor_definition',7,'p_constructor_definition','Syntactic.py',179),
  ('class_body_element_list -> class_body_element','class_body_element_list',1,'p_class_body_element_list','Syntactic.py',184),
  ('class_body_element_list -> class_body_element class_body_element_list','class_body_element_list',2,'p_class_body_element_list','Syntactic.py',185),
  ('class_body_element -> asignacion','class_body_element',1,'p_class_body_element','Syntactic.py',189),
  ('class_body_element -> function_definition','class_body_element',1,'p_class_body_element','Syntactic.py',190),
  ('class_body_element -> function_def_no_params','class_body_element',1,'p_class_body_element','Syntactic.py',191),
  ('function_definition -> DEF NAME LPAREN parameters RPAREN body END','function_definition',7,'p_function_definition','Syntactic.py',195),
  ('function_def_no_params -> DEF NAME body END','function_def_no_params',4,'p_function_def_no_params','Syntactic.py',198),
  ('method_call -> NAME DOT NAME LPAREN argumentos_opt RPAREN','method_call',6,'p_method_call','Syntactic.py',201),
  ('method_call -> NAME DOT NAME','method_call',3,'p_method_call','Syntactic.py',202),
  ('instantiation -> CLASS_NAME NEW LPAREN argumentos RPAREN','instantiation',5,'p_instantiation','Syntactic.py',206),
  ('comparator -> EQ','comparator',1,'p_comparator','Syntactic.py',210),
  ('comparator -> NE','comparator',1,'p_comparator','Syntactic.py',211),
  ('comparator -> LT','comparator',1,'p_comparator','Syntactic.py',212),
  ('comparator -> LE','comparator',1,'p_comparator','Syntactic.py',213),
  ('comparator -> GT','comparator',1,'p_comparator','Syntactic.py',214),
  ('comparator -> GE','comparator',1,'p_comparator','Syntactic.py',215),
  ('empty -> <empty>','empty',0,'p_empty','Syntactic.py',218),
  ('parameters -> NAME','parameters',1,'p_parameters','Syntactic.py',223),
  ('parameters -> NAME COMA parameters','parameters',3,'p_parameters','Syntactic.py',224),
  ('parameters -> empty','parameters',1,'p_parameters','Syntactic.py',225),
  ('body -> statement','body',1,'p_body','Syntactic.py',230),
  ('body -> statement body','body',2,'p_body','Syntactic.py',231),
]


# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND_OP CASE CHOMP CLASS CLASS_NAME COLON COMA COMMENT DEF DIVIDE DO DOT EACH ELSE ELSIF END EQ EQUALS FALSE FLOAT FOR GE GETS GT HASHROCKET IF INITIALIZE INTEGER LBRACKET LE LPAREN LSQBRACKET LT MINUS MODULE MULTIPLY NAME NE NEW NEWLINE NOT_OP NULL OR_OP PIPE PLUS POWER PUTS RBRACKET RPAREN RSQBRACKET SEMICOLON STRING SYMBOL TRUE UNLESS UNTIL VARIABLE_CLASE VARIABLE_CONSTANTE VARIABLE_GLOBAL VARIABLE_INSTANCIA VARIABLE_LOCAL WHEN WHILEprogram : code_listcode_list : code\n                 | code code_listcode : asignacion\n            | impresion\n            | solicitud_entrada\n            | if_statementasignacion : NAME EQUALS valor\n                  | VARIABLE_GLOBAL EQUALS valor\n                  | VARIABLE_CLASE EQUALS valor\n                  | VARIABLE_INSTANCIA EQUALS valor\n                  | VARIABLE_LOCAL EQUALS valor\n    impresion : PUTS argumentos_optsolicitud_entrada : PUTS STRING\n                         | NAME EQUALS GETS DOT CHOMP\n    argumentos_opt : argumentos\n                      | emptyargumentos : valor\n                  | valor COMA argumentosvalor : operand\n             | NULL\n             | SYMBOL\n             | boolean\n             | lists\n             | operation\n             | condition\n             | expression\n             | hash\n    expression : expression operatorArithm operand\n                  | operandoperand : INTEGER\n               | FLOAT\n               | NAMEoperatorArithm : PLUS\n                | MINUS\n                | MULTIPLY\n                | DIVIDE\n                | MODULE\n                power_op : INTEGER POWER INTEGERlists : LBRACKET argumentos RBRACKET\n             | LSQBRACKET argumentos RSQBRACKEThash : LBRACKET pares_hash RBRACKET\n            | LBRACKET empty RBRACKETpares_hash : par_hash\n                  | par_hash COMA pares_hashpar_hash : clave HASHROCKET valor\n                | clave COLON valorclave : SYMBOL\n             | STRINGboolean : TRUE\n                | FALSEoperation : operand operatorArithm operand\n                 | operand operatorArithm operation\n    if_statement : IF condition block END\n                 | IF condition block ELSE block END\n                 | IF condition block ELSIF condition block END\n                 | IF condition block ELSIF condition block ELSE block ENDcomparison : valor comparator valor block : statement\n              | statement block statement : asignacion\n                  | impresioncondition : comparison\n                 | boolean\n                 | NOT_OP comparison\n                 | comparison operatorCond comparison\n                 | LPAREN condition RPARENoperatorCond : AND_OP\n                    | OR_OPcond : valor comparator valor\n            | LPAREN comparison RPARENcomparator : EQ\n                  | NE\n                  | LT\n                  | LE\n                  | GT\n                  | GEempty :'
    
_lr_action_items = {'NAME':([0,3,4,5,6,7,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,80,83,84,85,87,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,105,107,108,114,115,117,118,120,],[8,8,-4,-5,-6,-7,37,37,37,37,37,37,37,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,37,37,-63,37,37,86,-64,-8,-9,-10,-11,-12,37,37,-72,-73,-74,-75,-76,-77,37,-34,-35,-36,-37,-38,37,37,-68,-69,-65,86,-61,-62,37,-19,-58,-52,-53,-29,-40,-42,-43,37,37,-41,-66,-67,-54,86,37,37,-15,86,-55,-56,86,-57,]),'VARIABLE_GLOBAL':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,48,50,51,52,53,80,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,103,104,108,114,115,117,118,120,],[9,9,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,9,-64,-8,-9,-10,-11,-12,-65,9,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,9,-15,9,-55,-56,9,-57,]),'VARIABLE_CLASE':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,48,50,51,52,53,80,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,103,104,108,114,115,117,118,120,],[10,10,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,10,-64,-8,-9,-10,-11,-12,-65,10,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,10,-15,10,-55,-56,10,-57,]),'VARIABLE_INSTANCIA':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,48,50,51,52,53,80,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,103,104,108,114,115,117,118,120,],[11,11,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,11,-64,-8,-9,-10,-11,-12,-65,11,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,11,-15,11,-55,-56,11,-57,]),'VARIABLE_LOCAL':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,48,50,51,52,53,80,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,103,104,108,114,115,117,118,120,],[12,12,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,12,-64,-8,-9,-10,-11,-12,-65,12,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,12,-15,12,-55,-56,12,-57,]),'PUTS':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,48,50,51,52,53,80,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,103,104,108,114,115,117,118,120,],[13,13,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,87,-64,-8,-9,-10,-11,-12,-65,87,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,87,-15,87,-55,-56,87,-57,]),'IF':([0,3,4,5,6,7,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,48,50,51,52,53,80,89,90,91,92,93,94,95,96,100,101,102,103,108,115,117,120,],[14,14,-4,-5,-6,-7,-78,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-8,-9,-10,-11,-12,-65,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,-15,-55,-56,-57,]),'$end':([1,2,3,4,5,6,7,13,15,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,48,50,51,52,53,80,89,90,91,92,93,94,95,96,100,101,102,103,108,115,117,120,],[0,-1,-2,-4,-5,-6,-7,-78,-3,-13,-14,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-8,-9,-10,-11,-12,-65,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-54,-15,-55,-56,-57,]),'EQUALS':([8,9,10,11,12,86,],[16,17,18,19,20,107,]),'STRING':([13,40,97,],[22,75,75,]),'NULL':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[27,27,27,27,27,27,27,27,27,27,27,27,27,-72,-73,-74,-75,-76,-77,27,-68,-69,27,27,27,27,27,]),'SYMBOL':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,97,98,99,105,107,],[28,28,28,28,28,28,28,73,28,28,28,28,28,-72,-73,-74,-75,-76,-77,28,-68,-69,28,110,28,28,28,28,]),'INTEGER':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,87,98,99,105,107,],[35,35,35,35,35,35,35,35,35,35,35,35,35,-72,-73,-74,-75,-76,-77,35,-34,-35,-36,-37,-38,35,35,-68,-69,35,35,35,35,35,]),'FLOAT':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,78,79,87,98,99,105,107,],[36,36,36,36,36,36,36,36,36,36,36,36,36,-72,-73,-74,-75,-76,-77,36,-34,-35,-36,-37,-38,36,36,-68,-69,36,36,36,36,36,]),'TRUE':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[38,38,38,38,38,38,38,38,38,38,38,38,38,-72,-73,-74,-75,-76,-77,38,-68,-69,38,38,38,38,38,]),'FALSE':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[39,39,39,39,39,39,39,39,39,39,39,39,39,-72,-73,-74,-75,-76,-77,39,-68,-69,39,39,39,39,39,]),'LBRACKET':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[40,40,40,40,40,40,40,40,40,40,40,40,40,-72,-73,-74,-75,-76,-77,40,-68,-69,40,40,40,40,40,]),'LSQBRACKET':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[41,41,41,41,41,41,41,41,41,41,41,41,41,-72,-73,-74,-75,-76,-77,41,-68,-69,41,41,41,41,41,]),'NOT_OP':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[43,43,43,43,43,43,43,43,43,43,43,43,43,-72,-73,-74,-75,-76,-77,43,-68,-69,43,43,43,43,43,]),'LPAREN':([13,14,16,17,18,19,20,40,41,43,44,54,55,56,57,58,59,60,61,77,78,79,87,98,99,105,107,],[44,44,44,44,44,44,44,44,44,44,44,44,44,-72,-73,-74,-75,-76,-77,44,-68,-69,44,44,44,44,44,]),'GETS':([16,],[49,]),'END':([21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,48,50,51,52,53,80,82,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,106,113,116,119,],[-13,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-8,-9,-10,-11,-12,-65,103,-59,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-60,115,117,120,]),'ELSE':([21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,48,50,51,52,53,80,82,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,106,116,],[-13,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-8,-9,-10,-11,-12,-65,104,-59,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-60,118,]),'ELSIF':([21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,48,50,51,52,53,80,82,83,84,85,87,89,90,91,92,93,94,95,96,100,101,102,106,],[-13,-16,-17,-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-8,-9,-10,-11,-12,-65,105,-59,-61,-62,-78,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-60,]),'RBRACKET':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,69,70,71,72,73,80,89,90,91,92,93,94,95,96,100,101,102,109,111,112,],[-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-78,-63,94,95,96,-44,-22,-65,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-45,-46,-47,]),'RSQBRACKET':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,76,80,89,90,91,92,93,94,95,96,100,101,102,],[-18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,100,-65,-19,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,]),'COMA':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,72,73,80,90,91,92,93,94,95,96,100,101,102,111,112,],[54,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,97,-22,-65,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,-46,-47,]),'EQ':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[56,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,56,56,56,56,56,56,-22,-63,-26,56,-52,-53,-29,-40,-42,-43,-41,-63,-67,56,56,-26,]),'NE':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[57,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,57,57,57,57,57,57,-22,-63,-26,57,-52,-53,-29,-40,-42,-43,-41,-63,-67,57,57,-26,]),'LT':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[58,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,58,58,58,58,58,58,-22,-63,-26,58,-52,-53,-29,-40,-42,-43,-41,-63,-67,58,58,-26,]),'LE':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[59,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,59,59,59,59,59,59,-22,-63,-26,59,-52,-53,-29,-40,-42,-43,-41,-63,-67,59,59,-26,]),'GT':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[60,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,60,60,60,60,60,60,-22,-63,-26,60,-52,-53,-29,-40,-42,-43,-41,-63,-67,60,60,-26,]),'GE':([25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,45,46,47,48,50,51,52,53,73,80,81,90,91,92,93,94,95,96,100,101,102,111,112,114,],[61,-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-26,-23,61,61,61,61,61,61,-22,-63,-26,61,-52,-53,-29,-40,-42,-43,-41,-63,-67,61,61,-26,]),'AND_OP':([26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,80,90,91,92,93,94,95,96,100,101,102,],[-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,78,78,-58,-52,-53,-29,-40,-42,-43,-41,78,-67,]),'OR_OP':([26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,80,90,91,92,93,94,95,96,100,101,102,],[-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,79,79,-58,-52,-53,-29,-40,-42,-43,-41,79,-67,]),'RPAREN':([26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,46,80,81,90,91,92,93,94,95,96,100,101,102,],[-20,-21,-22,-23,-24,-25,-26,-27,-28,-31,-32,-33,-50,-51,-63,-64,-65,102,-58,-52,-53,-29,-40,-42,-43,-41,-66,-67,]),'PLUS':([26,33,35,36,37,91,93,],[63,63,-31,-32,-33,63,-29,]),'MINUS':([26,33,35,36,37,91,93,],[64,64,-31,-32,-33,64,-29,]),'MULTIPLY':([26,33,35,36,37,91,93,],[65,65,-31,-32,-33,65,-29,]),'DIVIDE':([26,33,35,36,37,91,93,],[66,66,-31,-32,-33,66,-29,]),'MODULE':([26,33,35,36,37,91,93,],[67,67,-31,-32,-33,67,-29,]),'DOT':([49,],[88,]),'HASHROCKET':([73,74,75,110,],[-48,98,-49,-48,]),'COLON':([73,74,75,110,],[-48,99,-49,-48,]),'CHOMP':([88,],[108,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'code_list':([0,3,],[2,15,]),'code':([0,3,],[3,3,]),'asignacion':([0,3,45,83,104,114,118,],[4,4,84,84,84,84,84,]),'impresion':([0,3,45,83,104,114,118,],[5,5,85,85,85,85,85,]),'solicitud_entrada':([0,3,],[6,6,]),'if_statement':([0,3,],[7,7,]),'argumentos_opt':([13,87,],[21,21,]),'argumentos':([13,40,41,54,87,],[23,69,76,89,23,]),'empty':([13,40,87,],[24,71,24,]),'valor':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[25,47,48,50,51,52,53,25,25,47,47,25,90,47,25,111,112,47,48,]),'operand':([13,14,16,17,18,19,20,40,41,43,44,54,55,62,68,77,87,98,99,105,107,],[26,26,26,26,26,26,26,26,26,26,26,26,26,91,93,26,26,26,26,26,26,]),'boolean':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[29,46,29,29,29,29,29,29,29,29,46,29,29,29,29,29,29,46,29,]),'lists':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'operation':([13,14,16,17,18,19,20,40,41,43,44,54,55,62,77,87,98,99,105,107,],[31,31,31,31,31,31,31,31,31,31,31,31,31,92,31,31,31,31,31,31,]),'condition':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[32,45,32,32,32,32,32,32,32,32,81,32,32,32,32,32,32,114,32,]),'expression':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'hash':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'comparison':([13,14,16,17,18,19,20,40,41,43,44,54,55,77,87,98,99,105,107,],[42,42,42,42,42,42,42,42,42,80,42,42,42,101,42,42,42,42,42,]),'comparator':([25,47,48,50,51,52,53,90,111,112,],[55,55,55,55,55,55,55,55,55,55,]),'operatorArithm':([26,33,91,],[62,68,62,]),'pares_hash':([40,97,],[70,109,]),'par_hash':([40,97,],[72,72,]),'clave':([40,97,],[74,74,]),'operatorCond':([42,80,101,],[77,77,77,]),'block':([45,83,104,114,118,],[82,106,113,116,119,]),'statement':([45,83,104,114,118,],[83,83,83,83,83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> code_list','program',1,'p_program','Syntactic.py',9),
  ('code_list -> code','code_list',1,'p_code_list','Syntactic.py',12),
  ('code_list -> code code_list','code_list',2,'p_code_list','Syntactic.py',13),
  ('code -> asignacion','code',1,'p_code','Syntactic.py',17),
  ('code -> impresion','code',1,'p_code','Syntactic.py',18),
  ('code -> solicitud_entrada','code',1,'p_code','Syntactic.py',19),
  ('code -> if_statement','code',1,'p_code','Syntactic.py',20),
  ('asignacion -> NAME EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',24),
  ('asignacion -> VARIABLE_GLOBAL EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',25),
  ('asignacion -> VARIABLE_CLASE EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',26),
  ('asignacion -> VARIABLE_INSTANCIA EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',27),
  ('asignacion -> VARIABLE_LOCAL EQUALS valor','asignacion',3,'p_asignacion','Syntactic.py',28),
  ('impresion -> PUTS argumentos_opt','impresion',2,'p_impresion','Syntactic.py',33),
  ('solicitud_entrada -> PUTS STRING','solicitud_entrada',2,'p_solicitud_entrada','Syntactic.py',36),
  ('solicitud_entrada -> NAME EQUALS GETS DOT CHOMP','solicitud_entrada',5,'p_solicitud_entrada','Syntactic.py',37),
  ('argumentos_opt -> argumentos','argumentos_opt',1,'p_argumentos_opt','Syntactic.py',41),
  ('argumentos_opt -> empty','argumentos_opt',1,'p_argumentos_opt','Syntactic.py',42),
  ('argumentos -> valor','argumentos',1,'p_argumentos','Syntactic.py',45),
  ('argumentos -> valor COMA argumentos','argumentos',3,'p_argumentos','Syntactic.py',46),
  ('valor -> operand','valor',1,'p_valor','Syntactic.py',49),
  ('valor -> NULL','valor',1,'p_valor','Syntactic.py',50),
  ('valor -> SYMBOL','valor',1,'p_valor','Syntactic.py',51),
  ('valor -> boolean','valor',1,'p_valor','Syntactic.py',52),
  ('valor -> lists','valor',1,'p_valor','Syntactic.py',53),
  ('valor -> operation','valor',1,'p_valor','Syntactic.py',54),
  ('valor -> condition','valor',1,'p_valor','Syntactic.py',55),
  ('valor -> expression','valor',1,'p_valor','Syntactic.py',56),
  ('valor -> hash','valor',1,'p_valor','Syntactic.py',57),
  ('expression -> expression operatorArithm operand','expression',3,'p_expression','Syntactic.py',61),
  ('expression -> operand','expression',1,'p_expression','Syntactic.py',62),
  ('operand -> INTEGER','operand',1,'p_operand','Syntactic.py',65),
  ('operand -> FLOAT','operand',1,'p_operand','Syntactic.py',66),
  ('operand -> NAME','operand',1,'p_operand','Syntactic.py',67),
  ('operatorArithm -> PLUS','operatorArithm',1,'p_operatorArithm','Syntactic.py',71),
  ('operatorArithm -> MINUS','operatorArithm',1,'p_operatorArithm','Syntactic.py',72),
  ('operatorArithm -> MULTIPLY','operatorArithm',1,'p_operatorArithm','Syntactic.py',73),
  ('operatorArithm -> DIVIDE','operatorArithm',1,'p_operatorArithm','Syntactic.py',74),
  ('operatorArithm -> MODULE','operatorArithm',1,'p_operatorArithm','Syntactic.py',75),
  ('power_op -> INTEGER POWER INTEGER','power_op',3,'p_power_op','Syntactic.py',80),
  ('lists -> LBRACKET argumentos RBRACKET','lists',3,'p_lists','Syntactic.py',83),
  ('lists -> LSQBRACKET argumentos RSQBRACKET','lists',3,'p_lists','Syntactic.py',84),
  ('hash -> LBRACKET pares_hash RBRACKET','hash',3,'p_hash','Syntactic.py',87),
  ('hash -> LBRACKET empty RBRACKET','hash',3,'p_hash','Syntactic.py',88),
  ('pares_hash -> par_hash','pares_hash',1,'p_pares_hash','Syntactic.py',91),
  ('pares_hash -> par_hash COMA pares_hash','pares_hash',3,'p_pares_hash','Syntactic.py',92),
  ('par_hash -> clave HASHROCKET valor','par_hash',3,'p_par_hash','Syntactic.py',95),
  ('par_hash -> clave COLON valor','par_hash',3,'p_par_hash','Syntactic.py',96),
  ('clave -> SYMBOL','clave',1,'p_clave','Syntactic.py',101),
  ('clave -> STRING','clave',1,'p_clave','Syntactic.py',102),
  ('boolean -> TRUE','boolean',1,'p_boolean','Syntactic.py',106),
  ('boolean -> FALSE','boolean',1,'p_boolean','Syntactic.py',107),
  ('operation -> operand operatorArithm operand','operation',3,'p_operation','Syntactic.py',111),
  ('operation -> operand operatorArithm operation','operation',3,'p_operation','Syntactic.py',112),
  ('if_statement -> IF condition block END','if_statement',4,'p_if_statement','Syntactic.py',117),
  ('if_statement -> IF condition block ELSE block END','if_statement',6,'p_if_statement','Syntactic.py',118),
  ('if_statement -> IF condition block ELSIF condition block END','if_statement',7,'p_if_statement','Syntactic.py',119),
  ('if_statement -> IF condition block ELSIF condition block ELSE block END','if_statement',9,'p_if_statement','Syntactic.py',120),
  ('comparison -> valor comparator valor','comparison',3,'p_comparison','Syntactic.py',124),
  ('block -> statement','block',1,'p_block','Syntactic.py',127),
  ('block -> statement block','block',2,'p_block','Syntactic.py',128),
  ('statement -> asignacion','statement',1,'p_statement','Syntactic.py',131),
  ('statement -> impresion','statement',1,'p_statement','Syntactic.py',132),
  ('condition -> comparison','condition',1,'p_condition','Syntactic.py',135),
  ('condition -> boolean','condition',1,'p_condition','Syntactic.py',136),
  ('condition -> NOT_OP comparison','condition',2,'p_condition','Syntactic.py',137),
  ('condition -> comparison operatorCond comparison','condition',3,'p_condition','Syntactic.py',138),
  ('condition -> LPAREN condition RPAREN','condition',3,'p_condition','Syntactic.py',139),
  ('operatorCond -> AND_OP','operatorCond',1,'p_operatorCond','Syntactic.py',142),
  ('operatorCond -> OR_OP','operatorCond',1,'p_operatorCond','Syntactic.py',143),
  ('cond -> valor comparator valor','cond',3,'p_cond','Syntactic.py',146),
  ('cond -> LPAREN comparison RPAREN','cond',3,'p_cond','Syntactic.py',147),
  ('comparator -> EQ','comparator',1,'p_comparator','Syntactic.py',151),
  ('comparator -> NE','comparator',1,'p_comparator','Syntactic.py',152),
  ('comparator -> LT','comparator',1,'p_comparator','Syntactic.py',153),
  ('comparator -> LE','comparator',1,'p_comparator','Syntactic.py',154),
  ('comparator -> GT','comparator',1,'p_comparator','Syntactic.py',155),
  ('comparator -> GE','comparator',1,'p_comparator','Syntactic.py',156),
  ('empty -> <empty>','empty',0,'p_empty','Syntactic.py',159),
]

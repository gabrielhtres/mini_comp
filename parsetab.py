
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIB COMENT DEC_TIPO FIM_ESCOPO FIM_EXP FIM_SEN IDENT INIT_ESCOPO INIT_EXP LACO_FOR OP_AND OP_DIF OP_DIV OP_ELSE OP_IF OP_IGUAL OP_MAIOR OP_MAIOR_IG OP_MENOR OP_MENOR_IG OP_MULT OP_NOT OP_OR OP_SOMA OP_SUB OP_TO TIPO_BOOL TIPO_FL TIPO_INT TIPO_STR VAL_BOOL VAL_FL_N VAL_FL_P VAL_INT_N VAL_INT_P VAL_NULL VAL_STR\n        q0 : IDENT q0l\n        | OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q8\n        | LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13\n        | COMENT q12 COMENT q13\n    \n        q0l : DEC_TIPO q1 ATRIB q2 FIM_SEN q13\n        | ATRIB q9 FIM_SEN q13\n        | ATRIB q10 q11 q10 FIM_SEN q13\n\n    \n        q13 : IDENT q13l\n        | OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q13ll\n        | LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13\n        | COMENT q12 COMENT q13\n        |\n    \n        q13l : DEC_TIPO q1 ATRIB q2 FIM_SEN q13\n        | ATRIB q9 FIM_SEN q13\n        | ATRIB q10 q11 q10 FIM_SEN q13\n    \n        q13ll : FIM_SEN q13\n        | OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13\n    \n        q1 : TIPO_INT\n        | TIPO_FL\n        | TIPO_STR\n        | TIPO_BOOL\n    \n        q2 : VAL_STR\n        | q6\n        | q7\n        | VAL_BOOL\n        | VAL_NULL\n    \n        q3 : q10\n        | VAL_BOOL\n        | VAL_NULL\n        | VAL_STR\n    \n        q4 : OP_AND\n        | OP_OR\n        | OP_IGUAL\n        | OP_DIF\n        | OP_MAIOR\n        | OP_MENOR\n        | OP_MAIOR_IG\n        | OP_MENOR_IG\n    \n        q5 : OP_NOT\n        |\n    \n        q7 : VAL_FL_P\n        | VAL_FL_N\n    \n        q6 : VAL_INT_P\n        | VAL_INT_N\n    \n        q8 : FIM_SEN q13\n        | OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO q13\n    \n        q9 : q3\n        | q10 q11 q10\n    \n        q10 : IDENT\n        | q6\n        | q7\n    \n        q11 : OP_SOMA\n        | OP_SUB\n        | OP_MULT\n        | OP_DIV\n    \n        q12 : q1\n        | q2\n        | q3\n        | q4\n        | q5\n        | q8\n        | q11\n        | q13\n        | IDENT\n    '
    
_lr_action_items = {'IDENT':([0,5,8,9,10,11,32,33,34,35,36,37,38,39,40,41,43,44,45,46,63,66,69,72,73,74,76,77,80,86,96,100,101,102,105,106,107,113,119,120,121,129,130,135,136,142,147,149,151,155,],[2,21,57,-40,64,21,-31,-32,-33,-34,-35,-36,-37,-38,-39,71,-52,-53,-54,-55,57,71,57,71,-40,87,71,57,71,57,-40,71,57,71,71,71,57,-40,71,71,57,71,71,71,71,71,71,71,71,71,]),'OP_IF':([0,5,11,41,66,72,76,80,100,102,105,106,119,120,129,130,135,136,142,147,149,151,155,],[3,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'LACO_FOR':([0,5,11,41,66,72,76,80,100,102,105,106,119,120,129,130,135,136,142,147,149,151,155,],[4,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'COMENT':([0,5,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,49,50,51,52,65,66,67,70,72,76,80,98,100,102,105,106,110,112,119,120,125,126,129,130,135,136,142,146,147,149,150,151,152,155,156,],[5,11,11,66,-63,-56,-57,-58,-59,-60,-61,-62,-49,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-31,-32,-33,-34,-35,-36,-37,-38,-39,11,-52,-53,-54,-55,-43,-44,-41,-42,80,11,-8,-45,11,11,11,-11,11,11,11,11,-14,-46,11,11,-13,-15,11,11,11,11,11,-9,11,11,-16,11,-10,11,-17,]),'$end':([1,6,41,66,67,70,76,80,81,94,98,100,102,105,106,110,112,115,116,119,120,125,126,141,142,145,146,147,149,150,152,155,156,],[0,-1,-12,-12,-8,-45,-12,-12,-4,-6,-11,-12,-12,-12,-12,-14,-46,-5,-7,-12,-12,-13,-15,-2,-12,-3,-9,-12,-12,-16,-10,-12,-17,]),'DEC_TIPO':([2,21,71,],[7,68,68,]),'ATRIB':([2,21,22,23,24,25,53,64,71,82,87,],[8,69,-18,-19,-20,-21,75,79,69,99,104,]),'INIT_EXP':([3,4,47,48,],[9,10,73,74,]),'TIPO_INT':([5,7,11,68,],[22,22,22,22,]),'TIPO_FL':([5,7,11,68,],[23,23,23,23,]),'TIPO_STR':([5,7,11,68,],[24,24,24,24,]),'TIPO_BOOL':([5,7,11,68,],[25,25,25,25,]),'VAL_STR':([5,8,9,11,32,33,34,35,36,37,38,39,40,63,69,73,75,86,96,99,107,113,121,],[26,62,-40,26,-31,-32,-33,-34,-35,-36,-37,-38,-39,62,62,-40,89,62,-40,89,62,-40,62,]),'VAL_BOOL':([5,8,9,11,32,33,34,35,36,37,38,39,40,63,69,73,75,86,96,99,107,113,121,],[29,60,-40,29,-31,-32,-33,-34,-35,-36,-37,-38,-39,60,60,-40,92,60,-40,92,60,-40,60,]),'VAL_NULL':([5,8,9,11,32,33,34,35,36,37,38,39,40,63,69,73,75,86,96,99,107,113,121,],[30,61,-40,30,-31,-32,-33,-34,-35,-36,-37,-38,-39,61,61,-40,93,61,-40,93,61,-40,61,]),'OP_AND':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[32,32,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,32,32,]),'OP_OR':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[33,33,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,33,33,]),'OP_IGUAL':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[34,34,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,34,34,]),'OP_DIF':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[35,35,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,35,35,]),'OP_MAIOR':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[36,36,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,36,36,]),'OP_MENOR':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[37,37,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,37,37,]),'OP_MAIOR_IG':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[38,38,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,38,38,]),'OP_MENOR_IG':([5,11,31,49,50,51,52,57,58,59,60,61,62,78,103,],[39,39,-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,39,39,]),'OP_NOT':([5,9,11,32,33,34,35,36,37,38,39,73,96,113,],[40,40,40,-31,-32,-33,-34,-35,-36,-37,-38,40,40,40,]),'FIM_SEN':([5,11,49,50,51,52,54,55,56,57,58,59,60,61,62,83,84,88,89,90,91,92,93,95,109,111,137,138,143,144,154,],[41,41,-43,-44,-41,-42,76,-27,-47,-49,-50,-51,-28,-29,-30,100,-27,105,-22,-23,-24,-25,-26,106,119,120,41,142,147,149,155,]),'OP_ELSE':([5,11,137,143,],[42,42,42,148,]),'OP_SOMA':([5,11,49,50,51,52,55,57,58,59,84,],[43,43,-43,-44,-41,-42,43,-49,-50,-51,43,]),'OP_SUB':([5,11,49,50,51,52,55,57,58,59,84,],[44,44,-43,-44,-41,-42,44,-49,-50,-51,44,]),'OP_MULT':([5,11,49,50,51,52,55,57,58,59,84,],[45,45,-43,-44,-41,-42,45,-49,-50,-51,45,]),'OP_DIV':([5,11,49,50,51,52,55,57,58,59,84,],[46,46,-43,-44,-41,-42,46,-49,-50,-51,46,]),'VAL_INT_P':([5,8,9,11,32,33,34,35,36,37,38,39,40,43,44,45,46,63,69,73,75,77,79,86,96,99,101,104,107,108,113,121,122,],[49,49,-40,49,-31,-32,-33,-34,-35,-36,-37,-38,-39,-52,-53,-54,-55,49,49,-40,49,49,49,49,-40,49,49,49,49,49,-40,49,49,]),'VAL_INT_N':([5,8,9,11,32,33,34,35,36,37,38,39,40,43,44,45,46,63,69,73,75,77,79,86,96,99,101,104,107,108,113,121,122,],[50,50,-40,50,-31,-32,-33,-34,-35,-36,-37,-38,-39,-52,-53,-54,-55,50,50,-40,50,50,50,50,-40,50,50,50,50,50,-40,50,50,]),'VAL_FL_P':([5,8,9,11,32,33,34,35,36,37,38,39,40,43,44,45,46,63,69,73,75,77,86,96,99,101,107,113,121,],[51,51,-40,51,-31,-32,-33,-34,-35,-36,-37,-38,-39,-52,-53,-54,-55,51,51,-40,51,51,51,-40,51,51,51,-40,51,]),'VAL_FL_N':([5,8,9,11,32,33,34,35,36,37,38,39,40,43,44,45,46,63,69,73,75,77,86,96,99,101,107,113,121,],[52,52,-40,52,-31,-32,-33,-34,-35,-36,-37,-38,-39,-52,-53,-54,-55,52,52,-40,52,52,52,-40,52,52,52,-40,52,]),'FIM_EXP':([31,49,50,51,52,57,58,59,60,61,62,117,118,127,128,],[-27,-43,-44,-41,-42,-49,-50,-51,-28,-29,-30,123,124,131,132,]),'INIT_ESCOPO':([42,123,124,131,132,148,],[72,129,130,135,136,151,]),'OP_TO':([49,50,97,114,],[-43,-44,108,122,]),'FIM_ESCOPO':([67,72,80,85,98,100,110,119,120,125,126,129,130,133,134,135,136,139,140,146,147,149,150,151,152,153,155,156,],[-8,-12,-12,102,-11,-12,-14,-12,-12,-13,-15,-12,-12,137,138,-12,-12,143,144,-9,-12,-12,-16,-12,-10,154,-12,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'q0':([0,],[1,]),'q0l':([2,],[6,]),'q12':([5,11,],[12,65,]),'q13':([5,11,41,66,72,76,80,100,102,105,106,119,120,129,130,135,136,142,147,149,151,155,],[13,13,70,81,85,94,98,110,112,115,116,125,126,133,134,139,140,145,150,152,153,156,]),'q1':([5,7,11,68,],[14,53,14,82,]),'q2':([5,11,75,99,],[15,15,88,109,]),'q3':([5,8,11,63,69,86,107,121,],[16,56,16,78,56,103,117,127,]),'q4':([5,11,78,103,],[17,17,96,113,]),'q5':([5,9,11,73,96,113,],[18,63,18,86,107,121,]),'q8':([5,11,137,],[19,19,141,]),'q11':([5,11,55,84,],[20,20,77,101,]),'q6':([5,8,11,63,69,75,77,79,86,99,101,104,107,108,121,122,],[27,58,27,58,58,90,58,97,58,90,58,114,58,118,58,128,]),'q7':([5,8,11,63,69,75,77,86,99,101,107,121,],[28,59,28,59,59,91,59,59,91,59,59,59,]),'q10':([5,8,11,63,69,77,86,101,107,121,],[31,55,31,31,84,95,31,111,31,31,]),'q9':([8,69,],[54,83,]),'q13l':([21,71,],[67,67,]),'q13ll':([143,],[146,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> q0","S'",1,None,None,None),
  ('q0 -> IDENT q0l','q0',2,'p_q0','MiniCompN.py',217),
  ('q0 -> OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q8','q0',12,'p_q0','MiniCompN.py',218),
  ('q0 -> LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13','q0',13,'p_q0','MiniCompN.py',219),
  ('q0 -> COMENT q12 COMENT q13','q0',4,'p_q0','MiniCompN.py',220),
  ('q0l -> DEC_TIPO q1 ATRIB q2 FIM_SEN q13','q0l',6,'p_q0l','MiniCompN.py',235),
  ('q0l -> ATRIB q9 FIM_SEN q13','q0l',4,'p_q0l','MiniCompN.py',236),
  ('q0l -> ATRIB q10 q11 q10 FIM_SEN q13','q0l',6,'p_q0l','MiniCompN.py',237),
  ('q13 -> IDENT q13l','q13',2,'p_q13','MiniCompN.py',247),
  ('q13 -> OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q13ll','q13',12,'p_q13','MiniCompN.py',248),
  ('q13 -> LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13','q13',13,'p_q13','MiniCompN.py',249),
  ('q13 -> COMENT q12 COMENT q13','q13',4,'p_q13','MiniCompN.py',250),
  ('q13 -> <empty>','q13',0,'p_q13','MiniCompN.py',251),
  ('q13l -> DEC_TIPO q1 ATRIB q2 FIM_SEN q13','q13l',6,'p_q13l','MiniCompN.py',266),
  ('q13l -> ATRIB q9 FIM_SEN q13','q13l',4,'p_q13l','MiniCompN.py',267),
  ('q13l -> ATRIB q10 q11 q10 FIM_SEN q13','q13l',6,'p_q13l','MiniCompN.py',268),
  ('q13ll -> FIM_SEN q13','q13ll',2,'p_q13ll','MiniCompN.py',277),
  ('q13ll -> OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13','q13ll',6,'p_q13ll','MiniCompN.py',278),
  ('q1 -> TIPO_INT','q1',1,'p_q1','MiniCompN.py',287),
  ('q1 -> TIPO_FL','q1',1,'p_q1','MiniCompN.py',288),
  ('q1 -> TIPO_STR','q1',1,'p_q1','MiniCompN.py',289),
  ('q1 -> TIPO_BOOL','q1',1,'p_q1','MiniCompN.py',290),
  ('q2 -> VAL_STR','q2',1,'p_q2','MiniCompN.py',296),
  ('q2 -> q6','q2',1,'p_q2','MiniCompN.py',297),
  ('q2 -> q7','q2',1,'p_q2','MiniCompN.py',298),
  ('q2 -> VAL_BOOL','q2',1,'p_q2','MiniCompN.py',299),
  ('q2 -> VAL_NULL','q2',1,'p_q2','MiniCompN.py',300),
  ('q3 -> q10','q3',1,'p_q3','MiniCompN.py',306),
  ('q3 -> VAL_BOOL','q3',1,'p_q3','MiniCompN.py',307),
  ('q3 -> VAL_NULL','q3',1,'p_q3','MiniCompN.py',308),
  ('q3 -> VAL_STR','q3',1,'p_q3','MiniCompN.py',309),
  ('q4 -> OP_AND','q4',1,'p_q4','MiniCompN.py',315),
  ('q4 -> OP_OR','q4',1,'p_q4','MiniCompN.py',316),
  ('q4 -> OP_IGUAL','q4',1,'p_q4','MiniCompN.py',317),
  ('q4 -> OP_DIF','q4',1,'p_q4','MiniCompN.py',318),
  ('q4 -> OP_MAIOR','q4',1,'p_q4','MiniCompN.py',319),
  ('q4 -> OP_MENOR','q4',1,'p_q4','MiniCompN.py',320),
  ('q4 -> OP_MAIOR_IG','q4',1,'p_q4','MiniCompN.py',321),
  ('q4 -> OP_MENOR_IG','q4',1,'p_q4','MiniCompN.py',322),
  ('q5 -> OP_NOT','q5',1,'p_q5','MiniCompN.py',328),
  ('q5 -> <empty>','q5',0,'p_q5','MiniCompN.py',329),
  ('q7 -> VAL_FL_P','q7',1,'p_q7','MiniCompN.py',338),
  ('q7 -> VAL_FL_N','q7',1,'p_q7','MiniCompN.py',339),
  ('q6 -> VAL_INT_P','q6',1,'p_q6','MiniCompN.py',345),
  ('q6 -> VAL_INT_N','q6',1,'p_q6','MiniCompN.py',346),
  ('q8 -> FIM_SEN q13','q8',2,'p_q8','MiniCompN.py',352),
  ('q8 -> OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO q13','q8',5,'p_q8','MiniCompN.py',353),
  ('q9 -> q3','q9',1,'p_q9','MiniCompN.py',362),
  ('q9 -> q10 q11 q10','q9',3,'p_q9','MiniCompN.py',363),
  ('q10 -> IDENT','q10',1,'p_q10','MiniCompN.py',372),
  ('q10 -> q6','q10',1,'p_q10','MiniCompN.py',373),
  ('q10 -> q7','q10',1,'p_q10','MiniCompN.py',374),
  ('q11 -> OP_SOMA','q11',1,'p_q11','MiniCompN.py',380),
  ('q11 -> OP_SUB','q11',1,'p_q11','MiniCompN.py',381),
  ('q11 -> OP_MULT','q11',1,'p_q11','MiniCompN.py',382),
  ('q11 -> OP_DIV','q11',1,'p_q11','MiniCompN.py',383),
  ('q12 -> q1','q12',1,'p_q12','MiniCompN.py',389),
  ('q12 -> q2','q12',1,'p_q12','MiniCompN.py',390),
  ('q12 -> q3','q12',1,'p_q12','MiniCompN.py',391),
  ('q12 -> q4','q12',1,'p_q12','MiniCompN.py',392),
  ('q12 -> q5','q12',1,'p_q12','MiniCompN.py',393),
  ('q12 -> q8','q12',1,'p_q12','MiniCompN.py',394),
  ('q12 -> q11','q12',1,'p_q12','MiniCompN.py',395),
  ('q12 -> q13','q12',1,'p_q12','MiniCompN.py',396),
  ('q12 -> IDENT','q12',1,'p_q12','MiniCompN.py',397),
]

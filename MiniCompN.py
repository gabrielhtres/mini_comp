import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'IDENT',
    'TIPO_STR',
    'TIPO_INT',
    'TIPO_FL',
    'TIPO_BOOL',
    'DEC_TIPO',
    'ATRIB',
    'VAL_STR',
    'VAL_INT_P',
    'VAL_INT_N',
    'VAL_FL_P',
    'VAL_FL_N',
    'VAL_BOOL',
    'VAL_NULL',
    'OP_IF',
    'OP_ELSE',
    'LACO_FOR',
    'INIT_EXP',
    'FIM_EXP',
    'COMENT',
    'INIT_ESCOPO',
    'FIM_ESCOPO',
    'OP_SOMA',
    'OP_SUB',
    'OP_MULT',
    'OP_DIV',
    'OP_AND',
    'OP_OR',
    'OP_IGUAL',
    'OP_DIF',
    'OP_MAIOR',
    'OP_MENOR',
    'OP_MAIOR_IG',
    'OP_MENOR_IG',
    'OP_NOT',
    'OP_IN',
    'OP_TO',
    'FIM_SEN'
)

# Início Regras da Análise Léxica --------------------------------------------------------------------------------------

def t_IDENT(token):
    r'@[a-zA-Z]+.[a-zA-Z0-9]*'
    return token

def t_TIPO_STR(token):
    r'Str'
    return token

def t_TIPO_INT(token):
    r'Int'
    return token

def t_TIPO_FL(token):
    r'Float'
    return token

def t_TIPO_BOOL(token):
    r'Bool'
    return token

def t_DEC_TIPO(token):
    r':'
    return token

def t_OP_IGUAL(token):
    r'=='
    return token

def t_ATRIB(token):
    r'='
    return token

def t_VAL_STR(token):
    r'\"[a-zA-Z0-9]*\"'
    return token

def t_VAL_FL_P(token):
    r'[0-9]+\.[0-9]+'
    token.value = float(token.value)
    return token

def t_VAL_FL_N(token):
    r'-[0-9]+\.[0-9]+'
    token.value = float(token.value)
    return token

def t_VAL_INT_P(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

def t_VAL_INT_N(token):
    r'-[0-9]+'
    token.value = int(token.value)
    return token

def t_VAL_BOOL(token):
    r'True|False'
    return token

def t_VAL_NULL(token):
    r'Null'
    return token

def t_OP_IF(token):
    r'if'
    return token

def t_OP_ELSE(token):
    r'else'
    return token

def t_LACO_FOR(token):
    r'for'
    return token

def t_INIT_EXP(token):
    r'\('
    return token

def t_FIM_EXP(token):
    r'\)'
    return token

def t_COMENT(token):
    r'\#'
    return token

def t_INIT_ESCOPO(token):
    r'{'
    return token

def t_FIM_ESCOPO(token):
    r'}'
    return token

def t_OP_SOMA(token):
    r'\+'
    return token

def t_OP_SUB(token):
    r'-'
    return token

def t_OP_MULT(token):
    r'\*'
    return token

def t_OP_DIV(token):
    r'/'
    return token

def t_OP_AND(token):
    r'&&'
    return token

def t_OP_OR(token):
    r'\|\|'
    return token

def t_OP_DIF(token):
    r'!='
    return token

def t_OP_MAIOR(token):
    r'>'
    return token

def t_OP_MENOR(token):
    r'<'
    return token

def t_OP_MAIOR_IG(token):
    r'>='
    return token

def t_OP_MENOR_IG(token):
    r'<='
    return token

def t_OP_NOT(token):
    r'!'
    return token

def t_OP_IN(token):
    r'in'
    return token

def t_OP_TO(token):
    r'to'
    return token

def t_FIM_SEN(token):
    r';'
    return token

t_ignore = ' \t\n'

def t_error(token):
    print("Caractere ilegal: %s" % token.value[0])
    token.lexer.skip(1)

# Fim Regras da Análise Léxica -----------------------------------------------------------------------------------------

# Início Regras da Análise Sintática -----------------------------------------------------------------------------------

def p_q0(p):
    '''
        q0 : IDENT q0l
        | OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q8
        | LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13
        | COMENT q12 COMENT q13
    '''
    # p[0] = p[1]

def p_q0l(p):
    '''
        q0l : DEC_TIPO q1 ATRIB q2 FIM_SEN q13
        | ATRIB q9 FIM_SEN q13
    '''

def p_q13(p):
    '''
        q13 : IDENT q13l
        | OP_IF INIT_EXP q5 q3 q4 q5 q3 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO q13ll
        | LACO_FOR INIT_EXP IDENT ATRIB q6 OP_TO q6 FIM_EXP INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13
        | COMENT q12 COMENT q13
        |
    '''

def p_q13l(p):
    '''
        q13l : DEC_TIPO q1 ATRIB q2 FIM_SEN q13
        | ATRIB q9 FIM_SEN q13
    '''

def p_q13ll(p):
    '''
        q13ll : FIM_SEN q13
        | OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO FIM_SEN q13
    '''

def p_q1(p):
    '''
        q1 : TIPO_INT
        | TIPO_FL
        | TIPO_STR
        | TIPO_BOOL
    '''

def p_q2(p):
    '''
        q2 : VAL_STR
        | q6
        | q7
        | VAL_BOOL
        | VAL_NULL
    '''

def p_q3(p):
    '''
        q3 : q10
        | VAL_BOOL
        | VAL_NULL
    '''

def p_q4(p):
    '''
        q4 : OP_AND
        | OP_OR
        | OP_IGUAL
        | OP_DIF
        | OP_MAIOR
        | OP_MENOR
        | OP_MAIOR_IG
        | OP_MENOR_IG
    '''

def p_q5(p):
    '''
        q5 : OP_NOT
        |
    '''

def p_q7(p):
    '''
        q7 : VAL_FL_P
        | VAL_FL_N
    '''

def p_q6(p):
    '''
        q6 : VAL_INT_P
        | VAL_INT_N
    '''

def p_q8(p):
    '''
        q8 : FIM_SEN q13
        | OP_ELSE INIT_ESCOPO q13 FIM_ESCOPO q13
    '''

def p_q9(p):
    '''
        q9 : q3
        | q10 q11 q10
    '''

def p_q10(p):
    '''
        q10 : IDENT
        | q6
        | q7
    '''

def p_q11(p):
    '''
        q11 : OP_SOMA
        | OP_SUB
        | OP_MULT
        | OP_DIV
    '''

def p_q12(p):
    '''
        q12 : q1
        | q2
        | q3
        | q4
        | q5
        | q8
        | q11
        | q13
        | IDENT
    '''

def p_error(p):
    print("Erro de sintaxe", p)

# Fim Regras da Análise Sintática

lexer = lex.lex()
parser = yacc.yacc()

input_text = '''
@teste : Int = 123;
@teste2 : Float = 123.123;
for (@var = 1 to 10) {
    if (@var == 5) {
    
    };
};
# @teste #
'''

lexer.input(input_text)

while True:
    token = lexer.token()
    if not token:
        break  # Quando não houver mais tokens, saia do loop
    print("Encontrado: " + token.type + " com o lexema " + str(token.value) + " na posição " + str(token.lexpos)) 
    #

result = parser.parse(input_text)  # Chama o parser para a linha
print(result)  # Processa o resultado do parser

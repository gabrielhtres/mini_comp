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
    'INIC_EXP',
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

# Início Regras da Análise Léxica

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

def t_ATRIB(token):
    r'='
    return token

def t_VAL_STR(token):
    r'\"[a-zA-Z0-9]*\"'
    return token

def t_VAL_INT_P(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

def t_VAL_INT_N(token):
    r'-[0-9]+'
    token.value = int(token.value)
    return token

def t_VAL_FL_P(token):
    r'[0-9]+\.[0-9]+'
    token.value = float(token.value)
    return token

def t_VAL_FL_N(token):
    r'-[0-9]+\.[0-9]+'
    token.value = float(token.value)
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

def t_INIC_EXP(token):
    r'\('
    return token

def t_FIM_EXP(token):
    r'\)'
    return token

# def t_COMENT(token):
#     r'//.*'
#     pass

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

def t_OP_IGUAL(token):
    r'=='
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
    token.type = 'FIM_SEN'
    return token

t_ignore = ' \t\n'

def t_error(token):
    print("Caractere ilegal: %s" % token.value[0])
    token.lexer.skip(1)

# Fim Regras da Análise Léxica

# Início Regras da Análise Sintática

def p_statement(p):
    '''
        statement : IDENT DEC_TIPO tipo ATRIB valor FIM_SEN
                  | IDENT DEC_TIPO tipo ATRIB valor FIM_SEN statement
    '''

    if len(p) == 7:
        p[0] = {
            'tipo': p[3],
            'valor': p[5],
            'statement': p[7]
        }
    else:
        p[0] = {
            'tipo': p[3],
            'valor': p[5],
        }

def p_ident(p):
    '''
    ident : IDENT
    '''
    p[0] = p[1]

def p_tipo(p):
    '''
    tipo : TIPO_INT
         | TIPO_FL
         | TIPO_BOOL
         | TIPO_STR
    '''
    p[0] = p[1]

def p_valor(p):
    '''
    valor : VAL_INT_P
          | VAL_INT_N
          | VAL_FL_P
          | VAL_FL_N
          | VAL_BOOL
          | VAL_STR
          | VAL_NULL
    '''
    p[0] = p[1]



def p_error(p):
    print("Erro de sintaxe")

# Fim Regras da Análise Sintática

lexer = lex.lex()
parser = yacc.yacc()

lexer.input('''
@teste : Int = 123 ; @var : Str = 2 ;
''')

while True:
    token = lexer.token()
    if not token:
        break  # Quando não houver mais tokens, saia do loop
    print(token)

input_text = '''
@teste : Int = 123; @var : Str = 2;

'''
# Dividir o texto em linhas
lines = input_text.strip().split('\n')
print(lines)

# Loop de processamento das linhas
for line in lines:
    result = parser.parse(line)  # Chama o parser para a linha
    print(result)  # Processa o resultado do parser
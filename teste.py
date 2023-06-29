import ply.yacc as yacc

# Definição dos tokens
tokens = [
    'IDENT',
    'DEC_TIPO',
    'ATRIB',
    'VALOR',
    'FIM_EXP',
]

# Regras de produção
def p_statement(p):
    '''
    statement : IDENT DEC_TIPO tipo ATRIB valor FIM_EXP
    '''
    p[0] = {
        'identificador': p[1],
        'tipo': p[3],
        'valor': p[5]
    }

def p_tipo(p):
    '''
    tipo : TIPO_INT
         | TIPO_FLOAT
         | TIPO_BOOL
         | TIPO_STRING
    '''
    p[0] = p[1]

def p_valor(p):
    '''
    valor : VAL_INT
          | VAL_FLOAT
          | VAL_BOOL
          | VAL_STRING
    '''
    p[0] = p[1]

# Definição dos tokens e regras adicionais...

# Construção do parser
parser = yacc.yacc()

# Exemplo de uso
input_text = "@teste : tipo = valor ;"
result = parser.parse(input_text)
print(result)

import re
import ply.yacc as yacc
import ply.lex as lex

# Define uma expressão regular para cada tipo de token
# IDENT = r'@[a-zA-Z]+\.[a-zA-Z0-9]*'
# TIPO_STRING = r'Str'
# TIPO_INT = r'Int'
# TIPO_FLOAT = r'Float'
# TIPO_BOOL = r'Bool'
# DEC_TIPO = r':'
# ATRIB = r'='
# VAL_STRING = r'\"[a-zA-Z0-9]*\"'
# VAL_INT_POS = r'[0-9]+'
# VAL_INT_NEG = r'-[0-9]+'
# VAL_FLOAT_POS = r'[0-9]+\.[0-9]+'
# VAL_FLOAT_NEG = r'-[0-9]+\.[0-9]+'
# VAL_BOOL = r'True|False'
# VAL_NULL = r'Null'
# OP_IF = r'if'
# OP_ELSE = r'else'
# LACO_FOR = r'for'
# INIC_EXP = r'('
# FIM_EXP = r')'
# COMENT = r'#'
# INIT_ESCOPO = r'{'
# FIM_ESCOPO = r'}'
# OP_SOMA = r'\+'
# OP_SUB = r'-'
# OP_MULT = r'\*'
# OP_DIV = r'/'
# OP_AND = r'&&'
# OP_OR = r'\|\|'
# OP_IGUAL = r'=='
# OP_DIF = r'!='
# OP_MAIOR = r'>'
# OP_MENOR = r'<'
# OP_MAIOR_IG = r'>='
# OP_MENOR_IG = r'<='
# OP_NOT = r'!'
# PONTO = r'\.'
# FIM_EXP = r';'
# OP_IN = r'in'
# OP_TO = r'to'

# regexNumeroInteiroNegativo = r'-[0-9]+'
# regexNumeroInteiroPositivo = r'[0-9]+'
# regexNumeroRealNegativo = r'-[0-9]+\.[0-9]+'
# regexNumeroRealPositivo = r'[0-9]+\.[0-9]+'
# regexSoma = r'\+'
# regexSubtracao = r'-'
# regexMultiplicacao = r'\*'
# regexDivisao = r'/'
# regexAtribuicao = r'='
# regexParenteses = r'[(\|)]'
# regexFimDeLinha = r'\n'

# Associa cada expressão regular a um nome de token
# tokens = {
#     'IDENT' : IDENT,
#     'TIPO_STRING' : TIPO_STRING,
#     'TIPO_INT' : TIPO_INT,
#     'TIPO_FLOAT' : TIPO_FLOAT,
#     'TIPO_BOOL' : TIPO_BOOL,
#     'DEC_TIPO' : DEC_TIPO,
#     'ATRIB' : ATRIB,
#     'VAL_STRING' : VAL_STRING,
#     'VAL_INT_POS' : VAL_INT_POS,
#     'VAL_INT_NEG' : VAL_INT_NEG,
#     'VAL_FLOAT_POS' : VAL_FLOAT_POS,
#     'VAL_FLOAT_NEG' : VAL_FLOAT_NEG,
#     'VAL_BOOL' : VAL_BOOL,
#     'VAL_NULL' : VAL_NULL,
#     'OP_IF' : OP_IF,
#     'OP_ELSE' : OP_ELSE,
#     'LACO_FOR' : LACO_FOR,
#     'INIC_EXP' : INIC_EXP,
#     'FIM_EXP' : FIM_EXP,
#     'COMENT' : COMENT,
#     'INIT_ESCOPO' : INIT_ESCOPO,
#     'FIM_ESCOPO' : FIM_ESCOPO,
#     'OP_SOMA' : OP_SOMA,
#     'OP_SUB' : OP_SUB,
#     'OP_MULT' : OP_MULT,
#     'OP_DIV' : OP_DIV,
#     'OP_AND' : OP_AND,
#     'OP_OR' : OP_OR,
#     'OP_IGUAL' : OP_IGUAL,
#     'OP_DIF' : OP_DIF,
#     'OP_MAIOR' : OP_MAIOR,
#     'OP_MENOR' : OP_MENOR,
#     'OP_MAIOR_IG' : OP_MAIOR_IG,
#     'OP_MENOR_IG' : OP_MENOR_IG,
#     'OP_NOT' : OP_NOT,
#     'PONTO' : PONTO,
#     'FIM_EXP' : FIM_EXP,
#     'OP_IN' : OP_IN,
#     'OP_TO' : OP_TO   
# }

# # Função para analisar uma expressão
# def analisar(expressao):
#     # Adiciona um espaço no final da expressão para facilitar a análise
#     expressao = expressao.strip() + ' '

#     # Inicializa as variáveis de estado
#     posicao = 0
#     tokensEncontrados = []
#     erros = []

#     # Enquanto não chegamos no final da expressão
#     while posicao < len(expressao):
#         # Ignora espaços em branco e quebras de linha
#         if expressao[posicao] in [' ', '\n']:
#             posicao += 1
#             continue

#         # Tenta casar a entrada com cada expressão regular
#         match = None
#         for nome, regex in tokens.items():
#             match = re.match(regex, expressao[posicao:])
#             if match:
#                 valor = match.group(0)
#                 if nome == 'IDENT':
#                     # Se for um identificador, adiciona à lista de tokens encontrados
#                     # e registra seu índice na tabela de símbolos
#                     if valor not in tabelaSimbolos:
#                         tabelaSimbolos[valor] = len(tabelaSimbolos) + 1
#                     tokensEncontrados.append((nome, valor))
#                 else:
#                     # Senão, adiciona o token à lista de tokens encontrados
#                     tokensEncontrados.append((nome, valor))
#                 posicao += len(valor)
#                 break

#         # Se não foi possível casar com nenhum token, registra um erro léxico
#         if not match:
#             erros.append((expressao[posicao], posicao))
#             posicao += 1

#     # Retorna a lista de tokens encontrados e a lista de erros
#     return tokensEncontrados, erros

# # Exemplo de uso
# expressao = '-32.3 * X + 7;'
# # expressao = input("Digite sua expressão: ")
# tabelaSimbolos = {}
# tokensEncontrados, erros = analisar(expressao)

# Imprime os tokens encontrados e os erros
# print('Tokens encontrados:')
# for token in tokensEncontrados:
#     print(token)
# print('Erros:')
# for erro in erros:
#     print(erro)

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
    # 'OP_IF',
    # 'OP_ELSE',
    # 'LACO_FOR',
    # 'INIC_EXP',
    'FIM_EXP',
    # 'COMENT',
    # 'INIT_ESCOPO',
    # 'FIM_ESCOPO',
    # 'OP_SOMA',
    # 'OP_SUB',
    # 'OP_MULT',
    # 'OP_DIV',
    # 'OP_AND',
    # 'OP_OR',
    # 'OP_IGUAL',
    # 'OP_DIF',
    # 'OP_MAIOR',
    # 'OP_MENOR',
    # 'OP_MAIOR_IG',
    # 'OP_MENOR_IG',
    # 'OP_NOT',
    # 'OP_IN',
    # 'OP_TO'
)

# Definição das regras gramaticais
def p_statement(p):
    '''
    statement : IDENT DEC_TIPO tipo ATRIB valor FIM_EXP
    '''
    p[0] = f"{p[1]} : {p[3]} = {p[5]} ;"
    # p[0] = {
    #     'identificador': p[1],
    #     'tipo': p[3],
    #     'valor': p[5]
    # }

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

# Construção do analisador sintático
# lexer = lex.lex()
parser = yacc.yacc()

# Entrada de exemplo
input_text = '@teste : Int = 10;'
result = parser.parse(input_text)
print(result)
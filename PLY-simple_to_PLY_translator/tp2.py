from ply import lex
#import yacc then

#TIREI ASPAS E PLICAS PARA JA

tokens = ['VAR', "TEXT", "PRETTEXT", "PLICASTEXT", "EXPTEXT", "PRINT", "RETURN", "INSTRUCTION", 'COMMENT', "FIM"]
literals = '*+/-:=_%.,()[]»'
states = []

def t_PLICASTEXT(t):
    r'\'[^\']*\''
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_TEXT(t):
    r'"([^\"]*)"'
    t.value = t.value.replace('"', '')
    return t

def t_EXPTEXT(t):
    r'{[^{}]*}'
    t.value = t.value.replace('{', '') 
    t.value = t.value.replace('}', '')
    return t

def t_PRINT(t):
    r'<\/[^<>]*>'
    t.value = t.value.replace('</', '(')
    t.value = t.value.replace('>', ')')
    return t

def t_RETURN(t):
    r'<\\[^<>]*>'
    t.value = t.value.replace('<\\', '')
    t.value = t.value.replace('>', '')
    return t

def t_INSTRUCTION(t):
    r'<[^<>]*>'
    t.value = t.value.replace('<', '') 
    t.value = t.value.replace('>', '')
    return t


def t_PRETTEXT(t):
    r'\[.*\]'
    return t

def t_VAR(t):
    r'\w+'
    return t

def t_FIM(t):
    r'\.'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("ERROR: Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

import sys

#for line in sys.stdin:
#    lexer.input(line)
#    for tok in lexer:
#        print(tok)
#print("--------------------------------")
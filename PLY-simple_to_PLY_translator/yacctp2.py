
import ply.yacc as yacc

from tp2 import tokens

f = open("output.py", "w")

global vari, varj
vari = 0

#def p_expr(p):
#    "expr : aexp"
#    p[0] = p[1]
def p_prog(p):
    "prog : comandos"

def p_comandos_varios01(p):
    "comandos : "

def p_comandos_varios02(p):
    "comandos : comando comandos "

def p_comando(p):
    "comando : percent"

def p_comando2(p):
    "comando : doublepercent"

def p_comando3(p):
    "comando : comment"

def p_comment(p):
    "comment : COMMENT"
    p[0] = p[1]
    print(p[0], file=f)


def p_doublepercent(p):
    "doublepercent : '%' '%' var"
    p[0] = p[3] + "\n"
    print(p[0], file=f)

def p_doublepercent_empty(p):
    "doublepercent : '%' '%'"
    p[0] = "\n"
    print(p[0], file=f)

def p_percent(p):
    "percent : '%' atribs"

def p_atribs(p):
    "atribs : literalsAndIgnore"

def p_atribs2(p):
    "atribs : tokens"

def p_tokens(p):
    "tokens : var '=' PRETTEXT"
    p[0] = p[1] + " " + p[2] + " " + p[3]
    print(p[0], file=f)

def p_literalsAndIgnore(p):
    "literalsAndIgnore : var '=' plicastext"
    p[0] = p[1] + " " + p[2] + " " + p[3]
    print(p[0], file=f) 

def p_comando_expreg(p):
    "comando : exp"
    
def p_exp_1(p): 
    "exp : var ':' expreg ',' instruction"
    global vari, varj
    varj = str(vari) 
    p[0] = "\ndef t_" + p[1] + "_" + varj + "(t)" + p[2] + "\n\tr'" + p[3] + '\'' + "\n\treturn " + p[5]   
    print(p[0], file=f)
    vari += 1

def p_exp_2(p):    
    "exp : var ':' expreg ',' instruction ',' instruction"
    global vari, varj
    varj = str(vari)  
    p[0] = "\ndef t_" + p[1] + "_" + varj + "(t)" + p[2] + "\n\tr'" + p[3] + '\'' + "\n\tprint(" + p[5] + ")" + "\n\t" + p[7]
    print(p[0], file=f)
    vari += 1

def p_exp_3(p):    
    "exp : var '=' exptext"
    p[0] = p[1] + " = {" + p[3] + "}\n"
    print(p[0], file=f)

def p_exp_4(p): 
    "exp : var ':' instruction exptext" 
    global vari, varj
    varj = str(vari)   
    p[0] = "\ndef t_" + p[1] + "_" + varj + "(t)" + p[2] + "\n\t\"" + p[1] + " " + p[2] + " " + p[3] + "\"\n\t" + p[4]
    print(p[0], file=f)
    vari += 1

def p_exp_5(p): 
    "exp : var ':' instruction"
    global vari, varj
    varj = str(vari) 
    p[0] = "\ndef t_" + p[1] + "_" + varj + "(t)" + p[2] + "\n\t " + p[3]   
    print(p[0], file=f)
    vari += 1

def p_exp_6(p): 
    "exp : var var ':' instruction ',' instruction"
    global vari, varj
    varj = str(vari) 
    p[0] = "\ndef t_" + p[1] + "_" + varj + '(' + p[2] + ')' + p[3] + "\n\t" + p[4] + "\n\t" + p[6]
    print(p[0], file=f)
    vari += 1

def p_exp_7(p):    
    "exp : instruction"
    p[0] = "\n" + p[1]
    print(p[0], file=f)


def p_var(p):
    "var : VAR"
    if p[1] == "LEX": p[0] = "from ply import lex"
    elif p[1] == "YACC": p[0] = "\nimport ply.yacc as yacc\n"
    else: p[0] = p[1]

def p_expreg(p):
    "expreg : text"
    p[0] = p[1]

def p_instruction(p):
    "instruction : INSTRUCTION"
    p[0] = p[1]

def p_exptext(p):
    "exptext : EXPTEXT"
    p[0] = p[1]

def p_plicastext(p):
    "plicastext : PLICASTEXT"
    p[0] = p[1]

def p_text(p):
    "text : TEXT"
    p[0] = p[1]

def p_error(p):
    print("Syntax error! '%s'" % p.value[0])

parser = yacc.yacc()

import sys

for line in sys.stdin:
    res = parser.parse(line)
    #print("Resultado:", res)
    #pôr tudo dentro da gramática, fazer para um ficheiro


#Acho que para o que o stor deu está a dar

#FALTA VER ESTE "%prec UMINUS" QUE NÃO SEI O QUE FAZER COM ISTO 
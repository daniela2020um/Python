from email import message_from_binary_file
from blinker import NamedSignal
from paramiko import PKey
import ply.yacc as yacc

from tp2 import tokens

def yacctp(plysimple, output):

    f = open(output, "w")

    global i, j
    i = 0

    #def p_expr(p):
    #    "expr : aexp"
    #    p[0] = p[1]
    def p_prog(p):
        "prog : comandos"

    def p_comandos_empty(p):
        "comandos : "

    def p_comandos(p):
        "comandos : comando comandos "

    def p_comando_percent(p):
        "comando : percent"

    def p_comando_dpercent(p):
        "comando : doublepercent"

    def p_comando_comment(p):
        "comando : comment"

    def p_comando_lex(p):
        "comando : lex"

    def p_comando_yacc(p):
        "comando : yacc"

    def p_comando_func(p):
        "comando : func"

    def p_comando_exp(p):
        "comando : exp"

    def p_comando_instruction(p):
        "comando : instruction"
        p[0] = p[1]
        print(p[0], file=f)

    def p_comment(p):
        "comment : COMMENT"
        p[0] = p[1]
        print(p[0], file=f)


    def p_doublepercent(p):
        "doublepercent : '%' '%' var"
        p[0] = p[3] + "\n"
        print(p[0], file=f)


    def p_percent(p):
        "percent : '%' atribs"


    def p_lex(p):
        "lex : '/' var extra ':' function"
        if p[2] == "error" : p[0] = p[0] = "\ndef t_error" + "(" + p[3] + ")" + p[4] + "\n\t" + p[5]
        else : p[0] = p[0] = "\ndef t_" + p[2] + "(" + p[3] + ")" + p[4] + "\n\t" + p[5] 
        print(p[0], file=f)

    def p_func(p):
        "func : '»' var extra ':' function"
        global i, j
        j = str(i)
        p[0] = p[0] = "\ndef " + p[2] + "(" + p[3] + ")" + p[4] + "\n\t" + p[5] 
        print(p[0], file=f)
        i += 1

    def p_extra_empty(p):
        "extra : "
        p[0] = "t"

    def p_extra(p):
        "extra : var"
        p[0] = p[1]

    def p_yacc(p):
        "yacc : '+' var ':' instruction exptext instructions FIM"
        global i, j
        j = str(i)
        if p[2] == "error" : p[0] = "\ndef p_" + p[2] +  "(t)" + p[3] + "\n\t" + p[4] + "\n\t" + p[5] + "\n\t" + p[6]
        else : p[0] = "\ndef p_" + p[2] + j + "(t)" + p[3] + "\n\t\"" + p[2] + " " + p[3] + " " + p[4] + "\"\n\t" + p[5] + "\n\t" + p[6]
        print(p[0], file=f)
        i += 1

    def p_exp(p):    
        "exp : VAR '=' exptext"
        p[0] = p[1] + " = {" + p[3] + "}\n"
        print(p[0], file=f)

    def p_fuction_instructions(p):
        "function : instructions FIM"
        p[0] = p[1] 

    def p_function(p):
        "function : expreg instructions FIM"
        p[0] = "r\'" + p[1] + '\'' + "\n\t" + p[2]
        #print(p[0], file=f)


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
        if (p[1] == "ignore") : p[1] = "t_ignore"
        p[0] = p[1] + " " + p[2] + " " + p[3]
        print(p[0], file=f) 

    def p_var(p):
        "var : VAR"
        if p[1] == "LEX": p[0] = "import ply.lex as lex"
        elif p[1] == "YACC": p[0] = "\nlexer = lex.lex()\nimport ply.yacc as yacc\n"
        else: p[0] = p[1]

    def p_expreg(p):
        "expreg : text"
        p[0] = p[1]

    def p_instructions_empty(p):
        "instructions : "
        p[0] = " "

    #def p_instructions(p):
    #    "instructions : ',' instruction instructions"
    #    p[0] = p[2] + "\n\t" + p[3]

    def p_instructions_one(p):
        "instructions : instruction instructions"
        p[0] = p[1] + "\n\t" + p[2]
        #print(p[0], file=f)

    def p_instruction_print(p):
        "instruction : PRINT"
        p[0] = p[1]

    def p_instruction_return(p):
        "instruction : RETURN"
        if not p[1]: p[0] = "return t"
        else: p[0] = "t.value = " + p[1] + "\n\treturn t" 

    def p_instruction(p):
        "instruction : INSTRUCTION"
        p[0] = p[1]

    def p_exptext_empty(p):
        "exptext : "
        p[0] = ""

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
        print("Syntax error! '%s'" % p)

    parser = yacc.yacc()

    f1 = open(plysimple, "r")

    for line in f1:
        res = parser.parse(line)
        #print("Resultado:", res)
        #pôr tudo dentro da gramática, fazer para um ficheiro
import ply.lex as lex

literals = '+-/*=()'
## a single char
t_ignore = ' \t\n'
tokens = [ 'VAR','NUMBER' ]

def t_VAR(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	return t
	 

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t
	 

def t_error(t):
	r'.'
	(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]")
	t.lexer.skip(1)
	 

lexer = lex.lex()
import ply.yacc as yacc


precedence = [ ('left','+','-'),('left','*','/'),('right','UMINUS') ]
# symboltable : dictionary of variables
ts = { }


def p_stat0(t):
	"stat : VAR '=' exp"
	ts[t[1]] = t[3]
	 

def p_stat1(t):
	"stat : exp"
	print(t[1])
	 

def p_exp2(t):
	"exp : exp '+' exp"
	t[0] = t[1] + t[3]
	 

def p_exp3(t):
	"exp : exp '-' exp"
	t[0] = t[1] - t[3]
	 

def p_exp4(t):
	"exp : exp '*' exp"
	t[0] = t[1] * t[3]
	 

def p_exp5(t):
	"exp : exp '/' exp"
	t[0] = t[1] / t[3]
	 

def p_exp6(t):
	"exp : '-' exp %prec UMINUS"
	t[0] = -t[2]
	 

def p_exp7(t):
	"exp : '(' exp ')'"
	t[0] = t[2]
	 

def p_exp8(t):
	"exp : NUMBER"
	t[0] = t[1]
	 

def p_exp9(t):
	"exp : VAR"
	t[0] = getval(t[1])
	 

def p_error(t):
	print(f"Syntax error at '{t.value}', [{t.lexer.lineno}]")
	
	 

def getval(n):
	if n not in ts: print(f"Undefined name '{n}'")
	return ts.get(n,0)
	
y=yacc.yacc()
y.parse("3+4*7")
for line in sys.stdin:
   lexer.input(line)
   for tok in lexer:
       print(tok)
print("--------------------------------")

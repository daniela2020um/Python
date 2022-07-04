import sys

from yacc import yacctp

def main():
    plysimple = input("Insira o nome do ficheiro PLY-Simple: ")
    output = input("Insira o nome do ficheiro de output que pretende (ex: output.py): ")
    yacctp(plysimple, output)

main()

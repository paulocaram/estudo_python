#!/usr/bin/python

'''
Estudo de como utilizar o switch no python
'''

def func1():
    print "Opcao 1"
def func2():
    print "Opcao 2"
def func3():
    print "Opcao 3"
def sair():
    print "Obrigado por utilizar o sistema "

def switch(x):
    dict_funcoes = {1:func1,2:func2,3:func3,4:sair}
    dict_funcoes[x]()

print "\n\n"
print "Menu de Opcoes\n"
print "1. Incluir    "
print "2. Modificar  "
print "3. Excluir    "
print "4. Sair       "

x = input("Escolha a opcao de 1 a 4: ")
switch(x)

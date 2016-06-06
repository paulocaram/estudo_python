#!/usr/bin/python

# Teste de cadastro de usuarios

lista = []


def cadastra():
    usuario = raw_input("Digite o nome do usuario: ")
    lista.append(usuario)
    print lista

def exclui():
    usuario = raw_input("Nome do usuario que voce que excluir:")
    lista.remove(usuario)
    print lista

def imprima():

    for i in range(0,len(lista)):
        print lista[i]

def switch(x):
    dict_funcoes = {1:cadastra,2:exclui,3:imprima}
    dict_funcoes[x]()

while True:
    print "\n\n"
    print "1. Cadastra"
    print "2. Exclui  "
    print "3. Lista   "
    print "4. Sai     "

    x = input("Escolha a opcao de 1 a 4: ")
    
    if (x == 4):
        break

    switch(x)

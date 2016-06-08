#!/usr/bin/python
#Importa o modulo sys
import sys


def sai():
    print "Saindo do sistema !!"
    sys.exit()

def cadastra():
    dict_lista = {"login":"","senha":""}
    dict_lista["login"] = raw_input("Digite o login do novo usuario: ")    
    dict_lista["senha"] = raw_input("Digite a nova senha: ")
    lista.append(dict_lista)

def acessa():
    global lista
    usuario = raw_input("Digite o login: ")
    passwd = raw_input("Digite a senha: ")

    if (lista[0]["login"] == usuario):
    
        if (lista[0]["senha"] == passwd):
            mensagem(True,"Acesso permitido")
        else:
            mensagem(False,"Senha invalida")
    else:
        mensagem(False,"Acesso negado !!")

def mensagem(auth,msg):
    if auth:
        print msg
    else:
        print msg

def menu():
    print "\
        1. Cadastra usuario\n\
        2. Acessa sistema\n\
        3. Sai do Sistema\n"

    opcao = input("Digite sua opcao: ")

    return opcao

def switch(x):
    try:
        dict_options = {1:cadastra,2:acessa,3:sai}
        dict_options[x]();
    except Exception as e:
        print "Erro: %s"%e
        print "Opcao invalida"


lista = []

if __name__ == '__main__':

    while True:
        switch(menu())        

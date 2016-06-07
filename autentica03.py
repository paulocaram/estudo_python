#!/usr/bin/python

lista = []

def autentica():
    dict_lista = {"usuario":"","password":""}
    dict_lista["usuario"] = raw_input("Digite o Login: ")
    dict_lista["password"] = raw_input("Digite a senha: ")
    lista.append(dict_lista)

    if (lista[0]["usuario"] == "paulo") and (lista[0]["password"] == "paulo"):
        autenticado = True
    else:
        autenticado = False

    return autenticado 

def mensagem(auth):
    if auth:
        print "Acesso permitido !!!"
    else:
        print "Acesso negado !!!"

def menu():
    print "\
        1. Cadastra usuario\
        2. Acessa sistema\
        3. Sai do Sistema\n"

    opcao = input("Digite sua opcao: ")

    return opcao

def switch(x):
    dict_options = {1:cadastra,2:acessa,3:sai}
    dict_options[x]();

if __name__ == '__main__':
    mensagem(autentica())

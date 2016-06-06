#!/usr/bin/python

# Programa de autenticacao de usuarios

# Variavel Lista que guarda a lista dos usuarios do sistema
lista = []

def cadastra():
    usuarios = {"login":"","senha":""}
    usuarios["login"] = raw_input("Novo login: ")
    usuarios["senha"] = raw_input("Nova senha: ")
    lista.append(usuarios)
def acessa():
    usuario  = raw_input("Digite o usuario: ")
    password = raw_input("Digite a senha:   ")

    for i in range(0,len(lista)):
        
        if (lista[i]["login"] == usuario):
 
            if (lista[i]["senha"] == password):
                print "Usuario: %s Autenticado !!"%lista[i]["login"]
                break
            else:
                print "Senha invalida !!!"
                break
    else:
        print "Usuario nao cadastrado !!!"
            


def imprime():

    for i in range(0,len(lista)):
        print lista[i]["login"]


while True:
    print "Sistema de Autenticacao"
    print "\n"
    print "1. Cadastra usuarios  "
    print "2. Acessa ao sistema  "
    print "3. Imprimi os usuarios"
    print "4. Sai do sistema     "

    opcao = input("Opcao de 1 a 4: ")

    if (opcao == 1):
        cadastra()
    elif (opcao == 2):
        acessa()
    elif (opcao == 3):
        imprime()
    elif (opcao == 4):
        break
    else:
        print "Opcao invalida !!!"


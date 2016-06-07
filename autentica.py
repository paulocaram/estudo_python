#!/usr/bin/python

'''
Aula02 
Task1
Estrutura para cadastro de usuarios
Autor: Paulo Caram
'''

usuario = []
senha = []

def cadastra():
    login = raw_input("Digite o novo login: ")
    password = raw_input("Digite a nova senha: ")
    usuario.append(login)
    senha.append(password)

def acesso():
    login = raw_input("Login: ")
    password = raw_input("Senha: ")

    for key,i in enumerate(usuario):

        if (usuario[key] == login):
 
            if  (senha[key] == password):
                print "Usuario:[%s] autenticado !!!\n"%usuario[key]
                break
            else:
                print "Senha nao confere !!!\n"
                break

        elif (key < len(usuario)):
            continue

        else:
            print "Usuario nao encontrado na lista !!!\n"
            break

def imprime():
    for i in range(0,len(usuario)):
        print usuario[i]
    
#def switch(x):
#    dict_funcoes = {1:cadastra,2:acesso}
#    dict_funcoes[x]()

while True:
    print "Sistema de Cadastro de Usuarios"
    print "\n"
    print "1. Cadastra usuario  "
    print "2. Acessa ao sistema "
    print "3. Imprime a lista de usuarios  "
    print "4. Sai do sistema    "

    x = input("Escolha sua opcao de 1 a 4: ")

    if (x == 4):
        break
    elif (x == 1):
        cadastra()
    elif (x == 2):
        acesso()
    elif (x == 3):
        imprime()
    else:
        print "Opcao invalida !!"

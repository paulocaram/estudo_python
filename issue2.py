#!/usr/bin/python

# Estudo de dicionarios

lista = []
num = 0
while num < 5:

    usuarios = {"login":"","senha":""}

    usuarios["login"] = raw_input("Digite o login: ")
    usuarios["senha"] = raw_input("Digite a senha: ")

    print usuarios["login"],usuarios["senha"]
    lista.append(usuarios)
    print lista
    num += 1

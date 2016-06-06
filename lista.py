#!/usr/bin/python

# Estudo de lista, utilizando for

animais = ["Gato","Gato","Cachorro","Galinha","porco"]
cor = ["preto","branco","amarela","sujo"]

'''
for i in range(0,len(animais)):
    print animais[i]," ",i
'''

for key,i in enumerate(animais):
    print animais[key],key
    print cor[key]

    if animais.count("Gato") > 1:
        print "O animal [%s] esta cadastro + uma vez"%animais[key]
        break

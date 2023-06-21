'''
Escreva um programa que leia 3 números inteiros, calcule e escreva a média aritmética entre eles.
'''

numero1 = int(input("Insira um numero: "))
numero2 = int(input("Insira o segundo numero: "))
numero3 = int(input("Insira o terceiro numero: "))

media_aritimetica = (numero3 + numero2 + numero1) / 3
print("A media aritimetica dos numeros insridos é: {:.2f}".format(media_aritimetica))
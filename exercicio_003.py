'''
Escreva um programa que leia duas notas de um aluno de programação. Em seguida, a média ponderada, com pesos 2 e 3, respectivamente, deve ser calculada.
Por fim, o programa deve imprimir a média obtida. novo
'''

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media_pondera = (nota2 * 3 + nota1 * 2) / 5

print("A media ponderada das notas inseridas é: {:.2f}".format(media_pondera))
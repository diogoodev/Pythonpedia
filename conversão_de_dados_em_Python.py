'''
A função input() é utilizada para permitir a interação do usuário com a aplicação como, por exemplo, informar dados que serão processados pelo seu programa.
'''

'''
se adicionarmos o tipo que queremos na frente do input conseguimos fazer a coersão de tipos, por exepemplo, int, float
'''

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

'''
a função input sempre irá converter os dados inseridos para o formato string.
'''

soma = numero2 + numero1
dobro = numero3 * 2

'''
Se usarmos os valores em strings e tentarmos somar, o que irá acontecer é a concatenação das strings, apos fazermos a coersão de tipos conseguimos somar normalmente
'''

print(soma);
print(dobro)

'''
Função format(), ela recebe um argumento, e retorna ele formatado com quantas casas deciamis quisermos.
'''
print("Soma formatada:  {:.2f}".format(soma))
print("Soma formatada:  {:.6f}".format(dobro))

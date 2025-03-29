'''' 1 Peça ao usuário para inserir um número e informe se ele é positivo, negativo
ou zero.'''
from email.policy import default

'''
num= int(input('Digite um número para saber se ele é positivo, negativo ou zero: '))

if num == 0:
    print(f'O número {num} é zero.')
elif num >= 1:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
    '''
'''2 Solicite ao usuário que informe três notas de um aluno e calcule a média. Em
seguida, informe se o aluno foi aprovado (média ≥ 7), reprovado (média < 5)
ou se está de recuperação (média entre 5 e 7).'''

'''
nota1 = float(input('Digite a primeira nota do aluno: '))

nota2= float(input('Digite a segunda nota do aluno: '))

nota3 = float(input('Digite a terceira nota do aluno: '))

media = (nota1 + nota2 + nota3) /3

if media >= 7:
    print(f' O aluno foi aprovado')
elif media < 5:
    print(f'O aluno foi reprovado')
elif media > 5 or media < 7:
 print(f'O aluno tá de recuperação')
'''

'''3 Peça ao usuário dois números e verifique se o primeiro é múltiplo do
segundo. Se for múltiplo, imprima "Sim", caso contrário, "Não".'''

'''
num1 = int(input(f'Digite um número: '))
num2= int(input(f'Digite outro número: '))

if num1 % num2 == 0:
    print(f'O primeiro número é múltiplo do segundo')
else:
    print(f'O primeiro número não é múltiplo do segundo')
'''

'''4 Peça ao usuário para inserir três números e verifique se eles estão em ordem
crescente (do menor para o maior). Informe ao usuário se a sequência está
ordenada corretamente ou não.'''
'''
print('Digite três números para verificar sua ordem:')
num1 = int(input(f'Digite um número: '))
num2 = int(input(f'Digite o segundo número: '))
num3 = int(input(f'Digite o terceiro número: '))

if num1 < num2 < num3:
    print('EStá na ordem correta')
else:
    print('Os números estão em ordem errada')

'''
'''5 Solicite ao usuário para informar um número inteiro positivo e, em seguida,
conte quantos números ímpares existem entre 1 e o número informado.'''

'''
num = int(input(f'Digite um número inteiro e positivo'))
cont=0
if num > 0:
    for i in range(1, num, 2):
        cont = cont + 1
else:
    print('Digite um número positivo')

print(f'Existem {cont} números ímpares até o número informado')
'''

''' 6 Crie um programa que leia um número e calcule o fatorial desse número. O
fatorial de um número é o produto de todos os números inteiros de 1 até ele.'''

'''
num = int(input(f'Digite um número'))
fat= 1
for i in range(1, num+1,1):
    fat *= i
print(f'O fatorial de {num} é {fat}')
'''
'''7 Solicite ao usuário para inserir um número inteiro e calcule quantos dígitos
esse número possui.'''

'''
num= input(f'Digite um número inteiro para saber quantos digitos ele possui')
cont = 0
for p in num:
    cont+=1

print(f'O {num} possui {cont} dígitos')

'''

'''8 Um número perfeito é um número que é igual à soma de seus divisores,
excluindo ele mesmo. Crie um programa que verifique se um número
informado pelo usuário é perfeito.'''

''' 9 Crie um programa que gere a sequência de Fibonacci até o n-ésimo termo,
onde o primeiro e o segundo termo são 0 e 1, e os termos seguintes são a
soma dos dois termos anteriores.'''
'''
fib = [0,1]

n= int(input(f'Escreva qual vai ser o final da sua sequencia fibonacci'))

for i in range(2,n):
    fib.append(fib[i - 1] + fib[i - 2])
print(f"A sequência de Fibonacci até o {n}º termo é: {fib}")
'''

'''10.Peça ao usuário para inserir dois números: um número base e um limite. Em
seguida, multiplique o número base por 1, 2, 3 até o limite e mostre a
tabuada.'''

num1= int(input(f'Digite um número base: '))
num2 = int(input(f'Digite outro número limite: '))

for i in range(1,num2 +1,1):
    print(f'{num1} x {i}= {num1 * i}')


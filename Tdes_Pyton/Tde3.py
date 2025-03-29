'''1. Crie uma tupla chamada dados com os seguintes elementos:
● um número inteiro,
● um número decimal,
● uma string com seu nome,
● um valor booleano.
Imprima o segundo e o quarto elemento da tupla. Tente modificar um dos valores da
tupla e explique o erro que ocorreu.

dados=(12,5.8,'Vitor', True)

print(dados[1], dados[3])

nome = (input(print(f'Digite umm nome para alterar na lista'))
dados[2]='nome'
print(dados) # o erro ocorreu pois umma tupla não pode ser alterada.
'''


'''2 Crie uma tupla com 5 elementos e use uma função para contar quantas
vezes um determinado valor aparece na tupla. Por exemplo, para a tupla (1,
2, 2, 3, 2), deve retornar o número de vezes que o 2 aparece.

tupla=(1,2,2,3,1)

print(f'O número 2 aparece {tupla.count(2)} vezes; e o número 1 aparece {tupla.count(1)} vezes')
'''

'''3. Crie uma lista de números inteiros e realize as seguintes operações:
● Adicione o número 100 no final da lista.
● Remova o número que está na posição 2 (índice 2).
● Altere o valor da posição 0 para 500.
● Imprima a lista final.

lista=[1,2,3,4,5,6,9]
print(lista)

lista.append(100)
del(lista[2])
lista.insert(0, 500)
print(lista)'''

'''4. Crie uma lista chamada notas com 5 notas de alunos. Escreva um código que
calcule a soma e a média dessas notas. Em seguida, imprima a soma e a
média.

notas=[]

for i in range(5):
    nota= float(input(f'Qual foi a {i + 1} nota do aluno?'))
    notas.append(nota)
soma =sum(notas)
media= soma/len(notas)

print(f'A soma das notas: {soma} e a média das notas dos alunos foi: {media}')
'''
'''5. Crie uma lista de números inteiros. Ordene a lista em ordem crescente e
depois em ordem decrescente. Em seguida, filtre a lista para mostrar apenas
os números maiores que 10.

numeros=[1,4,7,5,2,9,10,6,80,10,55,44,12,34,76,47,56,100]

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

for i in numeros:
    if i>10:
        print(i)
'''

'''6. Crie uma lista de listas (matriz) que represente as notas de 3 alunos em 4
disciplinas. Por exemplo, a lista pode ser: [[7, 8, 9, 6], [6, 5, 8, 7], [10, 9, 8, 9]].
Faça o seguinte:
● Imprima a nota do segundo aluno na terceira disciplina.
● Calcule a média de cada aluno e imprima o nome do aluno com a maior
média.

lista=[]
for i in range(3):
    aluno_nota = []
    for j in range(4):
     notas= float(input(f'Qual foi {j + 1} nota do {i + 1}º aluno?'))
     aluno_nota.append(notas)
    lista.append(aluno_nota)
print(f'A nota do segundo aluno na terceira disciplina: {lista[1][2]}')

maior_media=0
alunoMaiorMedia=0

for i in range(3):
    media=sum(lista[i])/4
    print(f'A média do {i + 1} aluno: {media}')
    if media > maior_media:
        maior_media=media
        alunoMaiorMedia= i +1
print(f'O aluno com a maior média é o {alunoMaiorMedia}º aluno.')
'''
'''7. Crie um programa que leia quatro valores pelo teclado e guarde-os em uma
lista. No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.

lista=[]
pares=[]
for i in range(4):
    num= int(input(f'digite o {i + 1} valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
print(f' número 9 apareceu {lista.count(9)} vezes')
print(f'O valor 3 foi digitado na posição {lista.index(3)+1} vezes')# se o valor 3 não for digitado o programa da erro
#perguntar a thereza nais sobre
print(f'Esses são os números pares: {pares}')
'''

''' 8 sssUm dado é lançado 50 vezes, e o valor correspondente é armazenado em
uma lista. Faça um programa que determine o percentual de ocorrências de
face 6 do dado dentre esses 50 lançamentos.'''

from random import randint
lista=[]
for i in range(50):
    lista.append(randint(1,6))
    qtd6 = lista.count(6)
    percentual = (qtd6 / 50 ) * 100
print(f'Lista dos 50 lançamentos: {lista}')
print(f'A quantidade de vezes que o número 6 apareceu foi {qtd6} vezes.')
print(f'O percentual de ocorrências da face 6 é {percentual:.2f}%')


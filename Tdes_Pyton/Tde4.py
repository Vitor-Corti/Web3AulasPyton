'''1. Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado(entre 0 e 20) e mostrá-la por extenso.


num=("Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezeseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")


n= int(input('Digite um número'))
print(num[n - 1])


'''
from operator import length_hint

'''2. Faça um programa que preencha por leitura uma lista de 10 posições, e conta
quantos valores diferentes existem na lista.



lista= []

for i in range(10):
   num = int(input('Digite um valor par colocar na lista'))
   lista.append(num)

valores_diferentes = set(lista)

print(lista)
print(f'A lista tem {len(valores_diferentes)} elementos diferentes.')
'''

'''3.Crie um programa que leia quatro valores pelo teclado e guarde-os em uma lista.
No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.

lista=[]
lista_pares=[]
print('digite 4 valoes para por na lista')
for i in range(4):
    num=int(input(f'Digite o valor {i +1}'))
    lista.append(num)
    if lista[i] % 2 == 0:
        lista_pares.append(lista[i])

print(f'O número 9 apareceu {lista.count(9)} vezes')
print(f'O valor 3 foi digitados na posição{lista.index(3)}')
print(f'Os números pares da lista foram: {lista_pares}')
'''

'''4. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em uma
lista. Faça um programa que determine o percentual de ocorrências de face 6 do
dado dentre esses 50 lançamentos.

from random import randint
lista=[]
for i in range(50):
    lista.append(randint(1,6))
    qtd6 = lista.count(6)
    percentual = (qtd6 / 50 ) * 100
print(f'Lista dos 50 lançamentos: {lista}')
print(f'A quantidade de vezes que o número 6 apareceu foi {qtd6} vezes.')
print(f'O percentual de ocorrências da face 6 é {percentual:.2f}%')
'''


'''5. Tradutor Simples:
Desenvolva um programa que atue como um tradutor simples entre duas línguas. O
programa deve usar um dicionário onde as chaves são palavras em uma língua e os
valores são suas traduções em outra língua. O usuário deve poder fornecer uma
palavra como entrada e obter sua tradução como saída.

palavras={
    'Chave': 'Key',
    'Eu':'I',
    'estava': 'was',
    'voando':'flying'
}

escolha =input(print('Escolha alguma palavra para obter a tradução: "Chave", "Eu", "estava", "voando" '))

if escolha in palavras:
    print(f'A tradução de "{escolha}" é: {palavras[escolha]}')
else:
    print('Palavra não encontrada no dicionário.')
'''
'''6. Estoque de Produtos:
Implemente um sistema simples de controle de estoque de produtos. O programa
deve permitir ao usuário adicionar novos produtos ao estoque, atualizar a
quantidade de produtos existentes e exibir o estoque atualizado. Use um dicionário
onde as chaves são os nomes dos produtos e os valores são as quantidades
disponíveis.

estoque={
    'arroz': 2,
    'feijão' : 6,
    'cloro': 34,
    'batata': 400,
    'limão': 500
}
escolha= 0
while escolha != 4:
    print('Digite o num de qual operação deseja realizar')
    print('1. Adicionar novos produtos ')
    print('2. Atualizar a quantidades de produtos ')
    print('3. Ver estoque ')
    print('4. Para encerrar o programa ')
    escolha = int(input())
    if escolha== 1:
        new_product= input('Digite o nome do novo produto:')
        quantidade = int(input('Digite a quantidade do novo produto: '))
        estoque.update({new_product:quantidade})
    elif escolha== 2:
        produto = input('Digite o nome do produto:')
        if produto in estoque:
            nova_quantidade = int(input(f'Digite a nova quantidade para {produto}: '))
            estoque[produto] = nova_quantidade
            print(f'Quantidade do produto "{produto}" atualizada para {nova_quantidade}.')
        else:
            print(f'O produto "{produto}" não está no estoque.')
    elif escolha== 3:
        print(estoque)

    elif escolha== 4:
        print('Programa finalizado com sucesso.')
'''

'''7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida.

alt=[]
idad=[]
for i in range(5):
    altura= float (input(f'Digite a altura da { i +1} pessoa'))
    idade=int(input(f'Digite a idade da { i +1} pessoa: '))
    alt.append(altura)
    idad.append(idade)
print(alt)
print(idad)
idad.reverse()
alt.reverse()

print(f'A lista reversa das idades é {idad}')
print(f'A lista reversa das alturas é {alt}')
'''
'''8. Frequência de Letras:
Crie um programa que receba uma string como entrada e conte o número de
ocorrências de cada letra do alfabeto (ignorando maiúsculas/minúsculas).
O programa deve imprimir um dicionário onde as chaves são as letras do alfabeto e os
valores são o número de vezes que cada letra ocorre na string.'''
'''
dic={}
frase= input('Digite uma frase: ')
frase=frase.lower()
for letra in frase:
    if letra.isalpha():
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1
print(f'Sua frase possui {dic}')
'''

'''9. Média de Notas:
Escreva uma função em Python que receba um dicionário contendo nomes de
alunos e suas respectivas notas em uma disciplina. A função deve calcular a média
das notas de todos os alunos e retornar um dicionário onde a chave é "média" e o
valor é a média calculada.'''

'''

def calcula_media(dic):
    soma = 0
    total_alunos = 0
    notas_ind=0

    for notas in dic.values():
        soma += sum(notas)
        notas_ind += len(notas)
        total_alunos += 1
    media = soma / total_alunos
    return media


dic={}

qtd= int(input('Quantos alunos deseja cadastrar'))

for i in range(qtd):
    nome= input(f'Digite o nome do aluno {i+1}:')
    qtd2= int(input('Quantas notas deste aluno você deseja cadastrar?'))
    notas_aluno = []
    for j in range(qtd2):
        nota= float(input(f'Digite a nota {j+1} do aluno '))
        notas_aluno.append(nota)
        dic[nome] = notas_aluno

print(f'Notas dos alunos: {dic}')

media = calcula_media(dic)
print(f'Média das notas de todos os alunos:{media}')
'''
'''10. Contagem de Palavras:
Escreva um programa em Python que receba uma string como entrada e conte o
número de ocorrências de cada palavra na string. O programa deve imprimir um
dicionário onde as chaves são as palavras e os valores são o número de vezes que
cada palavra ocorre na string.'''

'''11 Escreva uma função que recebe um número n como parâmetro e imprime se n é
positivo ou negativo.'''
'''
def verificar_num(num):
    if num >= 0:
        return True
    else:
        return False

num= float(input('Digite um número para descobrir se ele é positivo ou negativo'))

resultado = verificar_num(num)

if resultado == True:
    print('Seu número é positivo')
else:
    print('Seu número é negativo')
'''

''''12. Escreva uma função para imprimir o valor absoluto de um número.'''
'''
def imprimir_valor_absoluto(numero):
    print(abs(numero))

numero = float(input("Digite um número: "))
imprimir_valor_absoluto(numero)
'''

'''13. Escreva uma função que recebe dois números (a e b) como parâmetro e retorne
True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''

def retorne(a,b):

    if a+b > limite:
        return True

limite= float(input('Digite o limite: '))

a= float(input('Digite o valor de a: '))
b= float(input('Digite o valor de b: '))

resultado = retorne(a,b)

if resultado == True:
    print('a soma de a + b é maior do que o limite')
else:
    print('o limite n é ultrapassado')
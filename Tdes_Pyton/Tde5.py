'''Questão 1
Escreva uma função que receba um número do usuário e divida 100 por esse número.
Utilize exceção para tratar casos onde o número fornecido seja zero ou não seja um número
válido (ou seja, um erro de tipo).

def dividir100(msg):
    while True:
        try:
            num = int(input(msg))

            if num == 0:
                raise ZeroDivisionError

            resultado = num/100
        except ZeroDivisionError :
            print('zero não é um número válido!')
            continue
        except (ValueError,TypeError):
            print('Número inválido')
            continue
        else:
            return resultado

n= dividir100(('Digite um valor válido:'))

print(f'O resultado {n}')
'''

'''Questão 2
Crie uma função que abra um arquivo e leia seu conteúdo. Caso o arquivo não exista, exiba
uma mensagem de erro específica. Caso ocorra outro tipo de erro, exiba uma mensagem
genérica.

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o arquivo: {e}")


nome_do_arquivo = "exemplo.txt"
conteudo = ler_arquivo(nome_do_arquivo)
if conteudo:
    print(conteudo)
'''

'''Questão 3
Crie uma exceção personalizada chamada ErroIdadeInvalida, que será levantada
quando uma pessoa tentar acessar um serviço com idade menor do que 18 anos. O código
deve lançar essa exceção se a idade for menor e tratá-la para exibir uma mensagem de
erro específica.


class ErroIdadeInvalida(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

def verificar_idade(idade):
    try:
        if idade < 18:
            raise ErroIdadeInvalida("Erro: Acesso negado. Idade mínima requerida é 18 anos.")
        print("Acesso permitido.")
    except ErroIdadeInvalida as e:
        print(e)

# Exemplo de uso:
idade_usuario = int(input('Qual é a idade do usuário'))  # Altere para testar diferentes idades
verificar_idade(idade_usuario)'''

'''Questão 4
Escreva uma função que solicita ao usuário a entrada de uma data (no formato
"dd/mm/yyyy"). Caso o usuário insira uma data inválida ou mal formatada, o programa deve
lançar e tratar a exceção com uma mensagem adequada.'''





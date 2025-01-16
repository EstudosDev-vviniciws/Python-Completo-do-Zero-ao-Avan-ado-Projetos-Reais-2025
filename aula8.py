# DE FUNCTIONS A LIBRARIES

''' USANDO UM SUPERMERCADO DE EXEMPLO PARA EXPLICAR '''

#FUNCTION

'''

FUNÇÕES:

- Maçã
* Peso
* Cor
* Preço

- Shampoo
* Peso
* Tipo de Cabelo
* Preço

- Picanha
* Peso
* Preço

'''

# MODULE 

'''

- Sessão de Frutas 
- Sessão de Beleza
- Sessão das Carnes

'''

# PACKAGE

'''

- Supermercado A
- Supermercado B
- Supermercado C

'''

# LIBRARY

'''

- HYPER MARKET

'''

# COMO FUNCIONA UMA FUNÇÃO

'''

def boas_vindas():
    print('Ola Vinicius!')
    print('Temos 5 Celulares no estoque')


boas_vindas()


(Não é necessário escrever as informações novamente, apenas damos um nome
aquela função e em seguida chamamos ela logo abaixo.)

'''

# CRIANDO UMA FUNÇÃO DE SOMA

'''

def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)
    
def somar_dois_numeros1():
    numero1 = 10
    numero2 = 10
    resultado = numero1 + numero2
    print(resultado)
    
    
somar_dois_numeros()
somar_dois_numeros1()
    
'''

# PARÂMETROS E ARGUMENTOS EM UMA FUNÇÃO

# COM PARÂMETROS E ARGUMENTOS
# Parametros ---> Argumento

'''

def boas_vindas(nome, quantidade): # Parâmetro vai dentro desse parênteses
    print(f'Ola {nome}.')
    print(f'Temos {str(quantidade)} Celulares no estoque')


boas_vindas('Vinicius', 5) # E aqui vão nossos Argumentos
boas_vindas('Noah', 4)
boas_vindas('Piter', 2)

'''

# SEM PARÂMETROS E ARGUMENTOS

''' 

def boas_vindas_Vinicius():
    print('Ola Vinicius!')
    print('Temos 5 Celulares no estoque')


def boas_vindas_Rafael():
    print('Ola Rafael!')
    print('Temos 4 Celulares no estoque')


def boas_vindas_Jack():
    print('Ola Jack!')
    print('Temos 2 Celulares no estoque')


boas_vindas_Vinicius()
boas_vindas_Rafael()
boas_vindas_Jack()

'''

# ARGUMENTOS DEFAULT E NON-DEFAULT

'''

# Default = Aquele que você define o valor no parâmetro
#Non-Default = Aquele que você não define o valor no parâmetro (ELE SEMPRE VAI VIM PRIMEIRO QUE O DEFAULT)

def boas_vindas(nome, quantidade = 6):
    print(f'Ola {nome}.')
    print(f'Temos {str(quantidade)} Celulares no estoque')


boas_vindas('Vinicius') 

'''

# PRINT OU RETURN EM FUNÇÕES

'''

#PRINT = Tarefa Realizada (O Print vai imprimir o que está no código e depois descartar a informação.)

def cliente1(nome):
    print(f'Ola {nome}')


print(cliente1('Vinicius'))


#RETURN = Já o Return vai armazenar na memória e depois imprimir na tela.

def cliente2(nome):
    return f'Ola {nome}'


print(cliente2('Jonny'))

'''

# VÁRIOS ARGUMENTOS XARGS COM NÚMEROS (Usamos o " * " quando não sabemos q quantidade de argumentos)

'''

def soma(*numeros):
    resultado = 0
    for num in numeros: 
        resultado += num 
    return resultado


x = soma(2,3,4,7)

print(x)

'''

# VÁRIOS ARGUMENTOS XARGS NOMEANDO PARAMETROS

'''

def agencia(**carro):
    return carro


print(agencia(marca= 'Palio', cor = 'Prata', motor = 1.0, placa = "HJ234"))
print(agencia(marca= 'Palio', cor = 'Preto', motor = 1.4, placa = "KL098"))
print(agencia(marca= 'Palio', cor = 'Vermelho', motor = 1.8, placa = "LKD214"))

'''

# IMPORTANDO UM MÓDULO

'''

# Qual é o fatorial de 4 ?

import math
print(math.factorial(4))

'''

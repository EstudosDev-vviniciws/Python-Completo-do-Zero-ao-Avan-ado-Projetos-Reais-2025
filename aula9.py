# INTRODUÇÃO A LISTAS

# É usado quando você precisa armazenar mais de uma informação em uma variável.
# E também precisa manter a sequência dos dados.

'''

cidade1 = 'Rio De Janeiro'
cidade2 = 'Belo Horizonte'
cidade3 = 'Salvador'

cidades = ['Rio De Janeiro', 'Belo Horizonte', 'Salvador']

print(cidades)

'''

# MANIPULANDO LISTAS

# Usamos " [] " quando queremos chamar o valor do Index.

'''

cidade1 = 'Rio De Janeiro'
cidade2 = 'Belo Horizonte'
cidade3 = 'Salvador'

cidades = ['Rio De Janeiro', 'Belo Horizonte', 'Salvador', 'Goiania']

cidades[3] = 'Brasilia' # Nessa situação estamos usando " [] " para trocar o dado dentro do item.
print(cidades) 

'''

# FUNÇÕES DENTRO DE LISTAS

'''

cidade1 = 'Rio De Janeiro'
cidade2 = 'Belo Horizonte'
cidade3 = 'Salvador'

cidades = ['Rio De Janeiro', 'Belo Horizonte', 'Salvador', 'Goiania']

# cidades.append('Santa Catarina')
# cidades.insert(1, 'Santa Catarina') 
# cidades.remove('Salvador')
# cidades.pop(0)
# cidades.sort()

print(cidades) 

'''

# CONCATENANDO LISTAS

# É possível criar uma lista dentro de outra e acessar valores individualmente ou da sublista.

'''

itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens[0][1])

# Outro maneira:

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras) # Usando .extend posso juntar a lista numeros com a lista letras em uma só.

# print(numeros)

'''

# EXTRAINDO VARIÁVEIS DE LISTAS

# É possível associar itens a variáveis em uma única linha, independentemente do número de itens, usando " * ".

'''

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]

item1, item2, *outros, item8 = produtos 

print(item1)
print(item2)
print(item8)
print(outros)

'''

# LOOPING DENTRO DE UMA LISTA

# É possível fazer um loop dentro de uma lista e puxar todos os index para colocar em uma String.

'''

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f'O valor final do produto é de R${x}.')

'''

# VERIFICANDO ITENS EM UMA LISTA

'''

cor_cliente = input('Digite uma cor: ')

cores = ['Amarelo','Verde', 'Azul', 'Vermelho']

if cor_cliente.capitalize() in cores: # Se caso o cliente digitar com letra minúscula, ainda irá encontrar a cor.
    print('Sim')
else:
    print('Não temos essa cor em estoque')

'''

# AGREGANDO DUAS LISTAS COM ZIP

'''

cores = ['Amarelo','Verde', 'Azul', 'Vermelho']
valores = [10, 20, 30, 40]


duas_listas = zip(cores, valores)

print(list(duas_listas))

'''

# INPUT EM UMA LISTA

'''

frutas_usuario = input('Digite o nome das frutas separados por vírgula: ')

frutas_lista = frutas_usuario.split(', ')


print(frutas_lista)

'''

# ENTENDO SOBRE TUPLES

# Armazena mais de uma informação em variáveis
# Mantém a sequência dos dados em uma variável
# Não podem ser alteradas (Immutable) - OS ITENS SÃO FIXOS
# OBS: Utiliza "()" no lugar de "[]" 

'''

cores_list = ['Amarelo','Verde', 'Azul', 'Vermelho']
cores_tuple = ('Amarelo','Verde', 'Azul', 'Vermelho')

cores_tuple.append('ROXO')
print(cores_tuple)

'''

# TRABALHANDO COM ARRAYS

# São usadas quando sua lista é muito grande e estou tendo problemas de performance

'''

from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]


print(letras)
print(numeros_i)
print(numeros_f)

# Utilizando ARRAY:
# Devo utilizar o typecode correto para cada situação, por exemplo: (int = i)  (float = f)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)

'''

# CRIANDO SETS (Listas)

# Similar a listas
# Evita itens duplicados
# Não utiliza index (A ordem pode ser diferente)

'''

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# Aqui a ordem pode ser diferente:

print(num1) 
print(num2)

print(num1 | num2) # O " | " junta duas Listas
print(num1 - num2) # O " - " mostra apenas itens diferentes
print(num1 ^ num2) # O " - " remove itens duplicados
print(num1 & num2) # O " & " mostra apenas itens duplicados

print(len(num1)) # Com o " len " é possível saber o tamanho da variável

'''

# FUNÇÕES EM SETS

'''

s1 = {1, 2, 3, 4, 5, 6}

s1.update([7, 8, 9])
s1.remove(7) # Remove gera um erro ao tentar remover um item que não tem, já o discard não
s1.discard(9)

print(s1)

'''

# SETS COM STRINGS

'''

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}


set4 = set1.intersection(set2)

print(set4)

'''

# INTRODUÇÃO A DICIONÁRIOS

# Utiliza index no formato de Keys e Values 
# Key: 'nome' | Value: 'Ana'
# Aceita string, integer, float, boolean...

'''

aluno = {'nome': 'Ana', 'idade': 17, 'nota_final': 'A', 'aprovação': True}

print(aluno['nome'])

# INTRODUÇÃO A DICIONÁRIOS

'''

# ATUALIZANDO ITENS NO DICIONÁRIO

'''

aluno = {'nome': 'Ana', 'idade': 17, 'nota_final': 'A', 'aprovação': True}

aluno.update({'nome': 'Vinicius', 'nota_final': 'B'})

print(aluno)

'''

# LOOPING DENTRO DE UM DICIONÁRIO

'''

aluno = {'nome': 'Ana', 'idade': 17, 'nota_final': 'A', 'aprovação': True}

for keys, values in aluno.items():
    print(keys, values)

'''

# VISUALIZANDO ITENS, KEYS e VALUES

'''

aluno = {
    'nome': 'Ana',
    'idade': 17, 
    'nota_final': 'A',
    'aprovação': True,
    'Materias': ['Fisíca', 'Inglês', 'Matemática']}


print(aluno.items())
print(aluno.keys())
print(aluno.values())

'''

# CONHECENDO A FUNÇÃO LAMBDA

# É uma função (pequena sem nome)
# Pode ter vários argumentos mas somente 1 expressão
# Muito utilizada dentro de outras funções
# Código mais 'clean'

'''

somar10 = lambda x, y: x + y + 10 # Argumento = x | Expressão = x + y + 10 

print(somar10(2, 4))

'''

# LAMBDA DENTRO DE UMA FUNÇÃO

'''

def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))

'''

# FUNÇÃO MAP EM UMA LISTA

# Muito utilizado com Listas
# Mapeia uma função para cada elemento interável. (list, tuple, dic etc.)

'''

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

resultado = map(multi, lista1)

print(list(resultado))

'''

# FUNÇÃO MAP COM LAMBDA

'''

lista1 = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, lista1)))

'''

# FUNÇÃO FILTER

# Muito utilizado com listas
# Aplica uma função para cada elemento interável, filtrando os items. (list, tuple, dic etc.)

'''

valores = [10, 12, 23, 32, 40]

print(list(filter(lambda x: x > 20, valores)))

'''

# ENTENDENDO LIST COMPREHENSION COM STRINGS

# Usado quando vc precisa criar uma nova lista a partir de uma existente
# Mais simples de escrever
# [expressão for iten in itens]

'''

carros1 = ['civic', 'astra', 'palio', 'lancer', 'opala']

carros2 = [carro for carro in carros1 if 'o' in carro]

print(carros2)

'''

# ENTENDENDO LIST COMPREHENSION COM NÚMEROS

'''

valores = [x * 10 for x in range(6)]

print(valores)

'''

# LISTA E GENERATOR EXPRESSIONS

# Uma forma mais rápido para Listas, dicionários e etc
# Menos memória alocada
# Valores em Bytes
# Usamos o " () " no lugar do " [] "

'''

from sys import getsizeof

numeros = [x * 10 for x in range(100)]

print(list(numeros))
print(type(numeros))
print(getsizeof(numeros))

print('=====')

numeros = (x * 10 for x in range(100))

print(list(numeros))
print(type(numeros))
print(getsizeof(numeros))

'''

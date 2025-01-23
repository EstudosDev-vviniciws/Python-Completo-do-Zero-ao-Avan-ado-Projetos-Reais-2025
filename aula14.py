# Print (Desafio 01)

'''

print('Olá, mundo Python!')

'''

# Variáveis (Desafio 02)

'''

nome = 'Vinícius'
idade = 21

print(f'Olá, meu nome é {nome} e eu tenho {idade} anos')

'''

# Números (Desafio 03)

'''

num1 = 10
num2 = 3.5

divisao = num1 / num2

print(f'O resultado da divisão é {divisao:.2f}')

'''

# Input (Desafio 04)

'''

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

print(f'Olá, {nome}! Você tem {idade} anos.')

'''

# Criando Lista (Desafio 05)

'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}') 
print(f'Multiplição: {multiplicacao}') 
print(f'Divisão: {divisao}') 
print(f'Exponenciação: {exponenciacao}')

'''

# Acessando Lista (Desafio 06)

'''

frutas = ['abacate', 'kiwi', 'laranja', 'banana', 'morango']

print(frutas)

'''

# Modificando Lista (Desafio 07)

'''

frutas = ['abacate', 'kiwi', 'laranja', 'banana', 'morango']

print(f'A primeira fruta é {frutas[0]} e a segunda é {frutas[4]}.')

'''

# Index de Lista (Desafio 08)

'''

frutas = ['abacate', 'kiwi', 'laranja', 'banana', 'morango']

frutas[1] = 'uva'
frutas.append('abacaxi')

print(frutas)

'''

# Removendo itens da Lista (Desafio 09)

'''

frutas = ['abacate', 'kiwi', 'laranja', 'banana', 'morango']

frutas.remove('abacate')
del frutas [3]

print(frutas)

'''

# Listas com loops (Desafio 10)

'''

carros = ['Lancer', 'Astra', 'Pálio', 'Civic']

for carro in carros:
    print('Eu faria um projeto no ' + carro)
    
'''

# Contando com o For Loop (Desafio 11)

'''

for numeros in range(1, 11):
    print(numeros)

'''
   
# Nested For Loop (Desafio 12)

'''

frutas = ['banana', 'maça', 'laranja']
vegetais = ['chuchu', 'espinafre', 'pepino']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)
        
'''

# While Loop (Desafio 13)

'''

numeros = 1

while numeros <= 10:
    print(numeros)
    numeros += 1
    
'''

# Loop com Break e Continue (Desafio 14)

'''

for numeros in range(1, 11):
    if numeros > 5:
        break
    print(numeros)

for numeros1 in range(1, 11):
    if numeros1 == 5:
        continue
    print(numeros1)

'''

# Contador de Lista (Desafio 15)

'''

frutas = str(['maçã', 'maçã', 'maçã', 'banana', 'banana', 'banana'])

for fruta in frutas:
    print(f'Número de maçãs na lista:', frutas.count('maçã'))
    break
    
'''

# Verificador de números com If, Else (Desafio 16)

'''

numero = int(input('Digite um número: '))

if numero > 10:
    print('O número é maior que 10')
else:
    print('O número é menor ou igual a 10 ')
    
'''

# Verificador de Idade (Desafio 17)

'''

idade = int(input('Digite sua idade: '))

if idade <= 13:
    print('Você é uma criança')
elif  13 < idade <= 19:
    print('Você é um adolescente')
elif idade >= 20:
    print('Você é um adulto')
    
'''

# Procura em Listas (Desafio 18)

'''

concessionária = ['BMW X6', 'BMW I5', 'BMW I8']

comprar_carro = str(input('Digite o nome do carro que você quer comprar: '))

if comprar_carro in concessionária:
    print('Este carro está disponível')
else:
    print('Desculpe, este carro não está disponível')

'''

# Encontrando um item com While (Desafio 19)

'''

while True:
    fruta = str(input('Digite o nome de uma fruta: '))
    if fruta.lower() == 'abacate':
        break
    
print('Parabéns, você acertou a fruta!')

'''

# Par e Impar (Desafio 20)

'''

lista = list(range(1, 11))

for numero in lista:
    if numero % 2 == 0:
        print(f'Este número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')

'''

# Lista de Cidades (Desafio 21)

'''

cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')

cidade_usuario = str(input('Digite uma cidade: '))

if cidade_usuario in cidades:
    print('A cidade está na lista de cidades')
else:
    print('A cidade não está na lista de cidades')
    
'''

# Pesquisa de País e Capital (Desafio 22)

'''

capitais = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

pais_usuario = str(input('Digite o nome de um país: '))

if pais_usuario in capitais:
    print(f'A capital de {pais_usuario} é {capitais[pais_usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')
    
'''

# Comparação em Sets (Desafio 23)

'''

lista1 = {'Chiquinha', 'Pedrita', 'Jon', 'Beto', 'Vagner'}
lista2 = {'João', 'Joaquim', 'Cris', 'Beto', 'Vagner'}

resultado = lista1.intersection(lista2)

print(resultado)

'''

# Funções Simples (Desafio 24)

'''

usuario_numero = int(input('Digite um número: '))

resultado = usuario_numero ** 2

print(f'O quadrado de {usuario_numero} é {resultado}.')

'''

# Soma com Funções (Desafio 25)

'''

def soma(num1, num2):
    return num1 + num2
    
usuario_num1 = int(input('Digite o primeiro número: '))
usuario_num2 = int(input('Digite o primeiro número: '))
print(f'A soma dos dois números é igual a : {soma(usuario_num1, usuario_num2)}')

'''

# Calculando Base e Expoente (Desafio 26)

'''


def potencia(base, exponente = 2):
    return base ** exponente

base_usuario = int(input('Digite um número: '))
exponente_usuario = (input('Digite um número: '))


if exponente_usuario:
    print(f'O resultado é: {potencia(base_usuario, int(exponente_usuario))}')
else:
    print(f'O resultado é: {potencia(base_usuario)}')

'''

# Calculando Fatorial (Desafio 27)

'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
usuario_num  = int(input('Digite um número: '))
print(f'O fatorial de  {usuario_num} é {fatorial(usuario_num)}')


'''

# Duas Funções (Desafio 28)

'''

def num1(n):
    return n * 2

def num2(n):
    return num1(n) ** 2

usuario_num = int(input('Digite um número: '))
print(f'O quadrado do dobro do número {usuario_num} é {num2(usuario_num)}')

'''

# Convertendo para Lambda (Desafio 29)

'''

cubo = lambda num: num ** 3
usuario_num = int(input(f'Digite um número: '))
print(f'O cubo de {usuario_num} é {cubo(usuario_num)}')

'''

# Lambda Multiplicando (Desafio 30)

'''

multi = lambda num1, num2: num1 * num2
usuario_num1 = int(input('Digite o primeiro número: '))
usuario_num2 = int(input('Digite o segundo número: '))

print(f'A multiplicação de {usuario_num1} e {usuario_num2} é {multi(usuario_num1, usuario_num2)}')

'''

# Lambda com If, Else (Desafio 31)

'''

numero = lambda num1: ()
usuario_numero = int(input('Digite um número: '))

if usuario_numero % 2 == 0:
    print(f'O número {usuario_numero} é Par')
else:
    print(f'O número {usuario_numero} é Ímpar')
    
'''

# Lambda com For Loop (Desafio 32)

'''

lista_num = [1, 2, 3, 4, 5, 6]

quadrado_num = lambda num: num ** 2

for num in lista_num:
    print(f'O quadrado do número {num} é {quadrado_num(num)}')

'''

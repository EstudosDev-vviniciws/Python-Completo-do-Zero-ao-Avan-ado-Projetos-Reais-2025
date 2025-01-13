# FUNÇÃO INPUT

'''

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
pais_mora = input('Digite o país onde mora: ')

print(f'Olá, meu nome é {nome}. Tenho {idade} anos e moro no {pais_mora}')

'''

#COVERSÃO DE STRING PARA INTEGER(INT)

'''

nome2 = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

print(type(nome2))
print(type(idade))

'''

# EXEMPLO:

'''

valor_produto = float(input('Digite o valor do produto: R$ '))

valor_final = (valor_produto * 1.10) 

print(f'O produto irá custar: R$ {valor_final:.2f}')

'''

# MULTIPLAS ENTRADAS NA MESMA LINHA DE INPUT()

dados = input('Digite o seu nome, idade e altura: ').split() # Vinicius 21 1,78
nome = dados[0]
idade = dados[1]
altura = dados[2]

print(f'Me chamo {nome.upper()}, tenho {idade} anos e tenho {altura} cm de altura.')
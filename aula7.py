# IF, ELIF, ELSE

'''

velocidade = 50

if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Favor reduzir sua velocidade')
elif velocidade < 60:
    print('Favor dirigir acima de 80Km/h')
else:
    print('Velocidade OK')
    
'''

# OPERADORES LOGICOS

'''

renda_acima_5mil = False
nome_limpo = False

if renda_acima_5mil or nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')
    
'''

# MULTIPLOS OPERADORES DE COMPARAÇÃO

'''

valor = 10

if  20 <= valor < 40:
    print('Produto foi aceito')
else:
    print('Produto não aceito')

'''

# FOR LOOP (Utilizando Números)

'''

for numero in range(6):
    print(numero)

'''

# FOR LOOP (Utilizando Strings)

'''

palavra = 'Espetacular'

for letra in palavra:
    print(f'{letra} + Esta dentro da palavra {palavra}')

'''

# FOR LOOP (Utilizando If e Else)

'''

compra_confirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para seu E-mail')
        break
else:
    print('Falha na compra')

'''

# FOR LOOP (Nested Loops)
# O primeiro looping roda uma vez
# Já o segundo roda o número de vezes que estiver entre os parênteses, estando dentro do looping acima

'''

for numero1 in range(1,7): 
    print('Produto' + str(numero1))
    for numero2 in range(12): 
        print(numero1, numero2)

'''

# FOR LOOP (Separando Strings)

'''

palavra = input('Digite uma palavra: ')

for space in palavra:
    print(f' {space}' , end='')

'''

# FOR LOOP (Criando um Retângulo)

'''

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end= '')
    print()

'''

# WHILE LOOP

'''

preco = 100
dia = 0

while preco > 20:
    dia +=1
    print(f'No dia {dia} o produto vai ser vendido por R${preco}')
    preco -= 5

'''

# OPERADOR TERNÁRIO (Deixa a linha de código menor e eficiente)

'''

idade = int(input('Digite sua idade: '))

resultado = 'Voto permitido' if idade >= 16 else 'Voto não Permitido'

print (resultado)

'''

# DIFERENÇAS ENTRE "IF, ELSE" "FOR LOOP" E "WHILE LOOP"

'''

(Verdadeiro ou Falso)
"IF, ELSE" = Executa apenas uma vez. Dependendo se a condição for verdadeiro (IF) ou falsa (ELSE).

(Sabemos o tamanho do loop)
"FOR LOOP" = Executa o código para cada elemento em uma sequência ou pelo número de vezes especificado.

(Não sabemos o tamanho do loop)
"WHILE LOOP" = É executado enquanto a condição for verdadeira, sem saber o
número exato de repetições.

'''

# EXEMPLO DE SITUAÇÃO COM WHILE LOOP

'''

produto = int(input('Digite o valor do produto: R$'))

comissao = 0.10
valor_final = (produto * comissao) + produto

while produto > 20:
    print(f'O produto com comissão de 10% sai por: R$ {valor_final:.2f}')
    break   

'''

''' SEGUNDA FORMA DE FAZER '''

'''

produto = int(input('Digite o valor do produto: R$'))

while produto > 20:
    produto = (produto * 0.10) + produto
    print(f'O produto com comissão de 10% sai por: R$ {produto:.2f}')
    break

'''
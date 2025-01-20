# PROJETOS

# If, Elif (Desafio)

'''

ponto_carne = int(input('Digite a temperatura da carne em Celsius: '))

if ponto_carne < 48:
    print('Cozinar por mais alguns minutos')
elif ponto_carne in range(48, 53):
    print('Selada')
elif ponto_carne in range(54, 59):
    print('Ao ponto para o mal')
elif ponto_carne in range(60, 64):
    print('Ao ponto')
elif ponto_carne in range(65, 70):
    print('Ao ponto para o bem')
elif ponto_carne in range(71, 80):
    print('Bem passado')
elif ponto_carne >= 85:
    print('Queimada')

'''

# Funções (Desafio)

'''

rendimento_tinta = int(input('Qual é o rendimento da lata ? '))
altura = float(input('Qual é a altura da parede ? '))
largura = float(input('Qual é a largura da parede ? '))

tinta_necessaria = (altura * largura) / rendimento_tinta

print(f'Vocé precisa de {tinta_necessaria} latas de tinta')

'''

# Sets (Desafio)

'''

funcionarios = ['Vinicius', 'Joao', 'Marcos', 'Eduardo', 'Maycon', 'Jorel']
turno_dia = ['Vinicius', 'Joao', 'Marcos', 'Eduardo']
turno_noite = ['Maycon', 'Jorel', 'Marcos']
tem_carro = ['Joao', 'Maycon', 'Eduardo', 'Vinicius']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)

'''

# If, Elif (Desafio)

'''

altura = float(input('Digite sua altura em cm: '))
peso = float(input('Digite seu peso em kg: '))
resultado = peso / (altura/100) ** 2 

if resultado < 18.5:
    print('Magreza')
elif resultado >= 18.5 and resultado < 24.9:
    print('Normal')
elif resultado >= 25.0 and resultado < 29.9:
    print('Sobrepeso')
elif resultado >= 30.0 and resultado < 39.9:
    print('Obesidade')
else:
    print('Obesidade Grave')

'''   

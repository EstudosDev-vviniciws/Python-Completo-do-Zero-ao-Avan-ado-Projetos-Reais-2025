# EXERCÍCIO 1

'''

temperatura = int(input('Digite uma temperatura: '))

if temperatura <= 10:
    print('Muito frio')
elif temperatura <= 20:
    print('Esta fresco')
else:
    print('Esta quente')

'''

# EXERCÍCIO 2

'''

horario = float(input('Digite um horário: '))

if horario <= 12:
    print('Bom dia')
elif horario <= 18:
    print('Boa tarde')
else:
    print('Boa noite')
       
'''

# EXERCÍCIO 3

'''

valor_compra = float(input('Digite o valor da sua compra: R$ '))

if valor_compra >= 200:
    desconto = 0.2
elif valor_compra >= 100:
    desconto = 0.1
else:
    desconto = 0.05

valor_final = valor_compra - (valor_compra * desconto)
print(f'O valor final com o desconto é de R$ {valor_final:.2f}')

'''

# EXERCÍCIO 4

'''

username = 'admin'
password = '123456'

username1 = (input('Digite um username: '))
password1 = (input('Digite um password: '))

if username1 == username and password1 == password:
    print('Login OK.')
else:
    print('Usuário ou senha incorretos.')

'''

# EXERCÍCIO 4

'''

nota = int(input('Digite sua nota: '))

if nota >= 9:
    print('Excelente, você tirou um A')
elif nota >= 7:
    print('Bom trabalho, você tirou um B')
elif nota >= 5:
    print('Você passou, mas precisa melhorar.Sua nota é C')
else:
    print('Reprovado')

'''
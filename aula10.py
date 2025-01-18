# TRABALHANDO COM TRY E EXCEPT COM UMA LISTA

# Excelente para testes
# Não realiza o 'stop' no programa
# Mensagens customizadas quando encontra um erro

'''

try:
    letras = ['a', 'b', 'c']
    print(letras[3]) # Aqui propositalmente vai dar erro, pois está fora do alcance
except IndexError:
    print('Index não existe')
    
'''

# TRABALHANDO COM TRY E EXCEPT COM O INPUT

'''

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
    
'''

# ADICIONANDO O ELSE E FINALLY

# Else: Executa apenas se não houver exceções no try.
# Finally: Executa sempre, independentemente de erros.

'''

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
finally:
    print('Código OK')
    
    
# else:
# #print('Usuário digitou um valor correto')

'''
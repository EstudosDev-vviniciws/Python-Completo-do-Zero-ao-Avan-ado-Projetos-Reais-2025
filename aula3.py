import sys # Import necessário para executar o UNICODE
sys.stdout.reconfigure(encoding='utf-8')


mensagem = 'Este curso é bem bom'

# INDEXAÇÃO

print(mensagem[-3:]) # Slice

# METODOS COMUNS EM STRINGS

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.strip())
print(mensagem.replace('bom', 'bacana'))
print(mensagem.split())

nome = 'Vinicius'
idade = 21

print('Me chamo', nome, 'e tenho', idade, 'anos de idade')

# FORMATAÇÃO DE F-STRING

print(f'Me chamo {nome} e tenho {idade} anos de idade')

# ESCAPE SEQUENCE

mensagem = 'Coluna1\t Coluna2\t Coluna3'
print(mensagem)
mensagem = ('Estou aprendendo \nPython agora')
print(mensagem)
mensagem = ('Estou aprendendo \'Python\' agora')
print(mensagem)

# TABULÇÃO

mensagem = 'Nome:\tVinicius Pinto\nIdade:\t21\nPaís:\tBrasil'
print(mensagem)

# CARACTERES UNICODE

mensagem1 = 'Coração: \u2764'
print(mensagem1)
# (PROGRAMAÇÃO ORIENTADA A OBJETOS)

# CRIANDO A SUA PRIMEIRA CLASSE 

# Utilizadas para criar Objetos (instances)
# Objetos são partes dentro de uma Class (instancias)
# Classes são utilizadas para agrupar dados e funções podendo reutilizar
# Class: Frutas
# Objects: Abacate, Banna...
# Para criar a classe, a primeira letra é maiúscula e não precisa de (). ----> class Funcionarios:

'''

class Funcionarios:

    # Dados:
    nome = 'Vinicius'
    sobrenome = 'Pinto'
    data_nascimento = '30/11/2003'
    
usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)

# CRIANDO A SUA PRIMEIRA CLASSE     

'''

# CRIANDO OBJETOS DENTRO DE UMA CLASSE

'''

# Criar a Classe:
class Funcionarios:
    pass # So para passar e ler o que está logo abaixo

# Criar o Objeto:
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# Criar os Parametros do usuario1:
usuario1.nome = 'Vinicius'
usuario1.sobrenome = 'Pinto'
usuario1.data_nascimento = '30/11/2003'

# Criar os Parametros do usuario2:
usuario2.nome = 'Jtp'
usuario2.sobrenome = 'Gabriel'
usuario2.data_nascimento = '01/10/2005'

# Print
print(usuario1.nome)
print(usuario1.data_nascimento)
print(usuario2.nome)
print(usuario2.data_nascimento)

'''

# CRIANDO CONSTRUTORES

'''

# Criar a Classe:
class Funcionarios:

    # Criar o Construtor:
    def __init__(self, nome, sobrenome, data_nascimento): # Self está se referindo a todos os Objetos.
        self.nome = nome
        self.sobrenome  = sobrenome
        self.data_nascimento = data_nascimento
        
# Criar o Objeto:
usuario1 = Funcionarios('Vinicius', 'Pinto', '30/11/2003') # Parametros
usuario2 = Funcionarios('Jtp', 'Gabriel', '01/10/2005')

# Print
print(usuario1.nome)
print(usuario1.data_nascimento)
print(usuario2.nome)
print(usuario2.data_nascimento)

'''

# ADICIONANDO MAIS FUNÇÕES A CLASSE

'''

# Criar a Classe:
class Funcionarios:

    # Criar o Construtor:
    def __init__(self, nome, sobrenome, data_nascimento): # Self está se referindo a todos os Objetos.
        self.nome = nome
        self.sobrenome  = sobrenome
        self.data_nascimento = data_nascimento
        
    # Funções(Tanto acima quanto embaixo)
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
        
# Criar o Objeto:
usuario1 = Funcionarios('Vinicius', 'Pinto', '30/11/2003') # Parametros
usuario2 = Funcionarios('Jtp', 'Gabriel', '01/10/2005')

# Print
print(usuario1.nome_completo())

# Outra maneira:
print(Funcionarios.nome_completo(usuario1))

'''

# CALCULANDO A IDADE DO FUNCIONÁRIO

'''

from datetime import datetime

# Criar a Classe:
class Funcionarios:

    # Criar o Construtor:
    def __init__(self, nome, sobrenome, ano_nascimento): # Self está se referindo a todos os Objetos.
        self.nome = nome
        self.sobrenome  = sobrenome
        self.ano_nascimento = ano_nascimento
        
    # Funções(Tanto acima quanto embaixo) 
    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        
# Criar o Objeto:
usuario1 = Funcionarios('Vinicius', 'Pinto', 2003) # Parametros
usuario2 = Funcionarios('Jtp', 'Gabriel', 2005)

# Print
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))

'''

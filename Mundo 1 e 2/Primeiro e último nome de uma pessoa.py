import ntpath

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer {}'.format(nome),'!')
nome = nome.title() #Toda primeira letra seguida de um espaço fica maiusculo.
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

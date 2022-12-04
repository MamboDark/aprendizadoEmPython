nome = str(input('Digite seu nome completo: ')).strip() #Linha 1 - No final do código o .strip() está servido para remover os espaços no inicio e no fim.
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #Linha 5 = No comando len(nome) está contando a quantidade de letras com espaço em seguida foi utilizado subtração -nome.count(' ') para contar sem o espaço que esta dentro da string.
#print('Seu primeiro nome é {} e ele tem letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

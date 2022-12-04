frase = str(input('Digite uma frase: ')).upper().strip()
print('A letr A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #Nese exemplo utilizamos r antes do find para indicar para o codigo que a busca deve ser da direita para esquerda.

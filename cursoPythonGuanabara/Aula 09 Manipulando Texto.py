'''frase = 'Curso em video Python'
#Fatiamento

#   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20


frase[9] #Colchete é utilizado para lista.
frase[9:13]
frase[9:21]
frase[9:21:2]
frase[:5]#Não tem inicio vai do 0 até o 4.
frase[15:]#Não tem fim vai do 15 até o final.
frase[9::3]

len(frase)      #'len'significa o comprimento da frase. ( Vai ler o tamanho da frase ou string)
frase.count('o, 0, 13')    #Conta quantas vezes tem a letra 'o'na frase. Ou uma contagem + fatiamento.
frase.findi('deo') #Indica onde esta localizado.
frase.find('Android') #Quando colocar str que não existe retorna o valor {-1}.
frase.replace('Python', 'Android') #Vai procurar 'Python'e substituirá por 'Android'
frase.upper()   #Deixa a frase em maiusculo
frase.lower() #Deixa frase em minúsculo
frase.capitalize() #Deixa todos caracteres para minusculo, e somente o primeiro fica em maiusculo.
frase.title()   #Onde tem espaço a letra seguinte ficara maiusculo.

frase = '  Aprenda Python '
frase.strip() #Remove os espaços inuteis no começo e no fim.
frase.rstrip() #Remove somente os ultimos espaços
frase.lstrip() #Remove os espaços da esquerda

frase = 'Curso em video Python'

frase.split() #Onde tem espaço ele cria uma divisão os espaços 'blocos/listas'
'-'.join(frase) #Junta todos os elementos de frase com o traço ( - )
'''

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])



'''Welcome! Are you completely new to programming?
If not then we presume you wil ber looking for information
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quikly.
Its also easy for beginners to use and learn, so jump in!'''

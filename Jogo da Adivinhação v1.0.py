from random import randint
from time import sleep #Biblioteca time no qual tem a função sleep.
computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente me vencer...')
print('-=-' * 20) #Multiplica 20 vezes -=- para dar um aspecto visual melhor.


entrada = int(input('Em que número eu pensei? ')) #Jogador tentando adivinhar.
print('PROCESSANDO...')
sleep(3)        #Faz o computador dormir/esperar/loading antes de processar.
if entrada == computador:
    print('Você conseguiu me vencer ! :( ')
else:
    print('Ganhei de você! haha o número que pensei foi no {} e não {}!'.format(computador, entrada))

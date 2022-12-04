"""velocidade = int(input('Digite a velocidade do veiculo: '))
if velocidade <= 80:
    print('Dentro da velocidade permitida!')
else:
    print('Você foi multado e a multa vai custar R$ 7,00 por cada Km a cima do limite.') """

from time import sleep

velocidade = float(input('Digite a velocidade do veiculo: '))
sleep(1)
if velocidade > 80:
    print('Ultrapassou a velocidade máxima de 80Km/h')
    multa = (velocidade-80) * 7   #Calculando a velocidade que excede vezes 7.
    print('Sua multa irá custar R${:.2F}'.format(multa))
print('Não use celular enquanto dirige!')
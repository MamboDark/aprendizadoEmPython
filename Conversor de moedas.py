saldo = float(input('Qual seu saldo disponível: R$'))
dolar = saldo / 5.19
euro = saldo / 5.04
print('Seu saldo em R$: {:.2F} \nVocê pode converter para Dolar US$: {:.2f} \nVocê pode converter para Euro €: {:.2f}'.format(saldo, dolar, euro))

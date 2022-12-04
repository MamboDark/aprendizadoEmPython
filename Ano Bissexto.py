from datetime import date
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
    print('O ano da sua maquina: ')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é BISSEXTO'.format(ano))
else:
    print('{} Náo é BISSEXTO'.format(ano))

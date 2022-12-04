salario = float(input('Digite o salário do colaborador: R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 /100)
print('Seu salário de R${:.2f} recebera um aumento e passara a ser R${:.2f}'.format(salario, aumento))

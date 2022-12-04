celsius = float(input('Informe a temperatura em C°: '))
f = ((9*celsius)/5)+32 #Os parenteses não fazem muita diferença nesse caso porque as operações estão na ordem certa de precedência.
print('A temperatura de {}°C corresponde a {}F!'.format(celsius, f))

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos a cima não podem formar triângulos')

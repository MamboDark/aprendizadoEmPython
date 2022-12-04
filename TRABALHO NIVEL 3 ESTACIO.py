entrada = eval(input('Insira os numeros da lista separados por virgula:'))

def subconjuntos(lista_entrada):
    return subconjuntos_recursivo([], sorted(lista_entrada))

def subconjuntos_recursivo(atual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(atual, conjunto[1:]) + subconjuntos_recursivo(atual + [conjunto[0]], conjunto[1:])
    return [atual]

lista_entrada = list(entrada)
resultado = subconjuntos(lista_entrada)

print(f'A lista inserida foi: {lista_entrada}')
print(f'A quantidade de subconjuntos é: {len(resultado)}')
print(f'A lista de subconjuntos é: {sorted(resultado)}')
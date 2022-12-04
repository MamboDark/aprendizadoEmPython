'''
ANSI == "ESCAPE SEQUENCE"
Sempre que for representar uma cor em Python == \033[m
Código das cores == \033[ESTILO->TEXT->BACKGROUND->m
EXEMPLO: \033[0;33;44m
TABELA DE CORES PADRÃO ANSI
STYLE:           TEXT:          BACKGROUND:
0 == NONE        30/Branco      40
1 == BOLD        31/Vermelho    41
4 == UNDERLINE   32/Verde       42
7 == NEGATIVE    33/Amarelo     43
                 34/Azul        44
                 35/Roxo        45
                 36/Azul claro  46
                 37/Cinza       47
\033[0;30;41m
\033[4;33;36m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m
'''

print('\033[0;30;41mHello World!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))
nome = 'Nelson'
cores = {'Limpa';'\033[m', \
                 'azul';'\033[34m',\
                 'amarelo';'\033[33m',
                 'pretoebranco','\033[7;30m'}

print('Olá! Muito legal te conhecer, {}{}{}!'.format(cores['amarelo'], nome['limpa']))

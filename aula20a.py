def lin(text):
    print('~' * len(text))
    print(text)
    print('~' * len(text))


def soma(x, y):
    print(f'A = {x} e B = {y}')
    s = x + y
    print(f'A soma de A + B = {s}')


def somaN(*num):
    s = 0
    for c in num:
        s += c
    print(f'Somando os valores {num} temos {s}')


def contador(y, n, x):
    from time import sleep
    for c in range(y, n, x):
        print(c, end=' ')
        sleep(0.5)
    print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa Principal
lin('Olá mundo')
lin('Oi')
lin('Curso em Vídeo de Python')
soma(y=4, x=5)
contador(10, 0, -2)
valores = [2, 4, 4, 8, 16]
dobra(valores)
print(valores)
somaN(4, 5, 6, 9, 16, 44)

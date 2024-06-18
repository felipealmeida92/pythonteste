# Parte prática da aula

def fatorial(n=1):
    """
    -> fatorial de um número
    :param n: número para encontrar fatorial
    :return: fatorial
    CeV : Gustavo Guanabara
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


# Programa Principal
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
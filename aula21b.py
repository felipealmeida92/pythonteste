# Parametros Opcionais


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    Função criada durante o curso CeV professor Gustavo Guanabara
    """
    s = a+b+c
    print(f'A soma vale {s}')


# Programa Principal
somar(1, 2, 7)
somar(1, 5)
somar(1)
somar()
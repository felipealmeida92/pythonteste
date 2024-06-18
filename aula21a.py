def contador (i, f, p):
    # aprendendo a usar uma docstrings
    """
    -> Faz contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Felipe Almeida durante o curso do Gustavo Guanabara do canal CursoemVideo.
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


# Programa Principal
contador(0, 100, 10)
help(contador)
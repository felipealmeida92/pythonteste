# Escopo de variáveis

def teste(b):
    global a
    a = 8  # variável passa a ser global
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa principal
a = 5  # variável desconsiderada
teste(a)
print(f'A fora vale {a}')
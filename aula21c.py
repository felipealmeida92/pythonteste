# Escopo de variáveis
def teste():
    x = 8  # escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 5  # escopo global
print(f'No programa principal, n vale {n}')
print('No programa principal, x vale {nada}')
teste()

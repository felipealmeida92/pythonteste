estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil: #laço para lista
    for k, v in e.items(): #laço para dicionario
        print(f'O campo {k} tem o valor {v}.')


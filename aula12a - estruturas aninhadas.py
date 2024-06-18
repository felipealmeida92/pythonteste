nome = str(input('Qual é o seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito!')
elif nome == 'Jessica' or nome == 'Pedro' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Maria Carlos Joana Adamastor':
    print('Belo nome!')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, {}!'.format(nome))

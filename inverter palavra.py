frase = str(input('Digite uma frase: ')).strip().upper()
divido = frase.split()
junto = ''.join(divido)
inverso = junto[::-1]
print(inverso)
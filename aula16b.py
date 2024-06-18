a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(d) # a ordem importa
print(len(c)) # tamanho da tupla
print(c.count(5)) # contar quantos números 5 na tupla
print(c.index(8)) # em que posição está o número 8
#tupla é imutável
del(d) #para deletar uma tupla inteira
'''print(d)''' #sumiu!
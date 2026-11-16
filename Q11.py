lista = ['a', 'e', 'i', 'o', 'u']

def contar_vogais(texto):
    texto2 = texto.lower()
    quant = 0
    for i in texto2:
        if i in lista:
            quant += 1
    return quant

a = contar_vogais('Instituto federal')
b = contar_vogais('Python')

print(a)
print(b)
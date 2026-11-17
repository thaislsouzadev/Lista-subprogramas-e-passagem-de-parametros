def media(lista):
    if len(lista) == 0:
        return 0
    else:
        resultado = sum(lista) / len(lista)
        return resultado

a = media([7, 8, 9])
b = media([5.5, 6.0])
c = media([])

print(f'{a}\n{b}\n{c}')
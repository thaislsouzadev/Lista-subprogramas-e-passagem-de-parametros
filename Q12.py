def menor_e_maior(lista):
    min = lista[0]
    max = lista[0]
    for i in lista:
        if len(lista) > 0:
            if i < min:
                min = i
            elif i > max:
                max = i

    print(f'Maior = {max}')
    print(f'Menor = {min}')

menor_e_maior([12, 5, 30, 8])
def aprovados(notas, minimo=7):
    notas_aprov = []
    for i in notas:
        if i >= minimo:
            notas_aprov.append(i)
    print(notas_aprov)

aprovados([5.5, 8.0, 7.0, 9.5, 6.9])
aprovados([5.5, 8.0, 7.0, 9.5, 6.9], 9)
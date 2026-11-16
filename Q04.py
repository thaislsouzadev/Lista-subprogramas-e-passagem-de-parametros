numeros = [4, 7, 10]

def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in numeros:
    a = eh_par(i)
    print(f'{i} é par? {a}')
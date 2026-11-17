pontos = 10

def bonus_local():
    pontos = 50
    print(f'dentro (local): {pontos}')

def bonus_global():
    global pontos
    pontos += 50
    print(f'dentro (global): {pontos}')
 
bonus_local()
print(f'fora: {pontos}')
bonus_global()
print(f'fora: {pontos}')
def maior(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

n1 = maior(4, 9, 2)
n2 = maior(-1, -5, -3)
print(n1,'\n',n2)
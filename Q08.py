def preco_final(preco, desconto=10):
    v = preco - preco * (desconto/100)
    return v

a = preco_final(200)
b = preco_final(200, 25)
c = preco_final(desconto=50, preco=80)

print(a)
print(b)
print(c)
arquivo = open("./texto.txt")
print(arquivo.read())

for linha in arquivo:
    print("ola"+linha)
    
contas = open("contas.txt")
valortotal = 0
for valor in contas:
    valortotal+=int(valor)
print(valortotal)

contas.close()

numeros = open("messi.txt")

par = 0 
for num in numeros:
    if int(num) % 2 ==0:
        par+=1

print(par)

arquivo = open("nessi.txt")
num = int(arquivo.read())

if num % 2 ==0:
    
#Exercicio 1
# numero = int(input("digite um numero inteiro: "))
# contador = 1
# while contador < 11:
#     print(numero * contador)
#     contador += 1

#Exercicio 2

# while True:
#     nota = int(input("digite a nota do aluno: "))
#     if nota < 11 and nota > -1:
#         break
#     else: 
#         print("digite uma nota valida")

# #Exercicio 3
# soma = 0
# contador = 0
# while True:
#     valores = int(input("digite os numeros: "))
#     if valores == -1:
#         break
#     soma += valores
#     contador += 1

# print(f"A media é : {soma / contador}")

# #Exercicios 4
# N = int(input("Digite o valor de N: "))

# soma = 0
# i = 1

# while i <= N:
#     soma += i
#     i += 1

# print(f"a soma é: {soma}")

#Exercicio 5 
contador = 0
pares= 0 
impares = 0
while contador < 10:
    numero = int(input("digite os numeros: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print(f"foram lidos {pares} numeros pares e {impares} numeros impares")


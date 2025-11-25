# # Exercício 1
# A = [0,0,0,0,0,0]
# A[0] = 1
# A[1] = 0
# A[2] = 5
# A[3] = -2
# A[4] = -5
# A[5] = 7
# soma = A[0] + A[1] + A[5]
# A[4] = 100
# for i in range(6):
#     print(A[i])

# # Exercício 2
# vetor = [0,0,0,0,0,0]
# for i in range(6):
#     vetor[i] = int(input("digite os numeros: "))
# for i in range(6):
#     print(vetor[i])

# # Exercício 3
# x = [0]*10
# y = [0]*10
# for i in range(10):
#     x[i] = float(input("digite os numeros: "))
#     y[i] = x[i] * x[i]
# for i in range(10):
#     print(x[i], y[i])

# # Exercício 4
# vetor = [0,0,0,0,0,0,0,0]
# for i in range(8):
#     vetor[i] = int(input("digite os valores do vetor: "))
# X = int(input("digite a posição de X: "))
# Y = int(input("digite o posição de Y: "))
# print(vetor[X] + vetor[Y])

# # Exercício 5
# vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# pares = 0
# for i in range(10):
#     vetor[i] = int(input("digite os valores: "))
#     if vetor[i] % 2 == 0:
#         pares += 1
# print(f"o programa encontrou {pares} numeros pares")

# # Exercício 6
# vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(10):
#     vetor[i] = int(input("digite os valores: "))
# maior = vetor[0]
# menor = vetor[0]
# for i in range(10):
#     if vetor[i] > maior:
#         maior = vetor[i]
#     if vetor[i] < menor:
#         menor = vetor[i]
# print(f"O maior valor econtrado foi {maior} e o menor {menor}")

# # Exercício 7
# vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(10):
#     vetor[i] = int(input("digite os valores: "))
# maior = vetor[0]
# pos = 0
# for i in range(10):
#     if vetor[i] > maior:
#         maior = vetor[i]
#         pos = i 
# print(f" o maior valor encontrado foi {maior} no indice {pos} do vetor")

# # Exercício 8
# notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# soma = 0
# for i in range(15):
#     notas[i] = float(input("digite as notas dos alunos: "))
#     soma += notas[i]
# media = soma / 15
# print(f" a media dos alunos foi {media}")

# # Exercício 9
# vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# negativos = 0
# soma_positivos = 0
# for i in range(10):
#     vetor[i] = float(input("digite os valores: "))
#     if vetor[i] < 0:
#         negativos += 1
#     else:
#         soma_positivos += vetor[i]
# print(f"existem {negativos} numeros negativos e a soma dos positivos é {soma_positivos}")

# # Exercício 10
# vetor = [0, 0, 0, 0, 0]
# soma = 0
# for i in range(5):
#     vetor[i] = float(input("digite os valores: "))
#     soma += vetor[i]
# maior = vetor[0]
# menor = vetor[0]
# for i in range(5):
#     if vetor[i] > maior:
#         maior = vetor[i]
#     if vetor[i] < menor:
#         menor = vetor[i]
# media = soma / 5
# print(f"O maior numero é {maior}, o menor é {menor} e a media é {media}")

# Exercício 11
vetor = [0, 0, 0, 0, 0]
for i in range(5):
    vetor[i] = float(input("digite os valores: "))
maior = vetor[0]
menor = vetor[0]
posMaior = 0
posMenor = 0
for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]
        posMaior = i
    if vetor[i] < menor:
        menor = vetor[i]
        posMenor = i
print(f"O maior valor es encontra no inidice {posMaior},e o menor valor no indice {posMenor}")

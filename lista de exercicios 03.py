while True:
    print("============Bem vindo a calculadora de 2 operadores============")
    opcao = int(input("selecione sua opção \n1 Para somar \n2 Para subtrair \n3 Para multiplicar  \n4 para dividir \n0 para cancelar \n: "))
    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))

    if opcao == 1:
        print(f"o resultado é: {n1 + n2}")
    elif opcao == 2:
        print(f"o resultado é: {n1 - n2}")
    elif opcao == 3:
        print(f"o resultado é: {n1 * n2}")
    elif opcao == 4:
        print(f"o resultado é: {n1 / n2}")
    elif opcao == 0:
        break
    else:
        print(f"{opcao} não é uma opção valida")
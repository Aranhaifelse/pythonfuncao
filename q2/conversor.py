def conversao (escolha):
    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        return fahrenheit
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit - 32 / 1.8
        return celsius
    else:
        print("Opção inválida.")

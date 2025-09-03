import os
os.system("cls")

try:
    dia_num = int(input("Digite um número de 1 a 7 para saber o dia da semana: "))

    match dia_num:
        case 1:
            dia = "Domingo, Final de semana"
        case 2:
            dia = "Segunda-feira, dia útil"
        case 3:
            dia = "Terça-feira, dia útil"
        case 4:
            dia = "Quarta-feira, dia útil"
        case 5:
            dia = "Quinta-feira, dia útil"
        case 6:
            dia = "Sexta-feira, dia útil"
        case 7:
            dia = "Sábado, Final de semana"
        case _:
            dia = "Dia inválido. Por favor, digite um número de 1 a 7."

except ValueError:
    dia = "Opção inválida. Por favor, insira um número inteiro."

print(f"Hoje é: {dia}")

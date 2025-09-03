import os 
os.system("cls")  

nome = str(input("Digite o seu nome: "))
altura = float(input(f"Digite sua altura, {nome}: \n"))
sexo = input("Digite o seu sexo (M para masculino, F para feminino): ").strip().upper()

match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"{nome}, seu peso ideal é de {peso_ideal:.2f} kg")
        print(f"{nome}, sua altura é de {altura:.2f} m")
        print(f"{nome}, seu sexo é Masculino")
    
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"{nome}, seu peso ideal é de {peso_ideal:.2f} kg")
        print(f"{nome}, sua altura é de {altura:.2f} m")
        print(f"{nome}, seu sexo é Feminino")
    
    case _:
        print("Sexo inválido. Por favor, digite M para masculino ou F para feminino.")

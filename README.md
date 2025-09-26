import os 
os.system("cls")


soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += n1 
    soma += nota 
    
    continuar = input("Deseja digitar mais uma nota ?")
    if continuar == "n":
        print ("Cauculando média. . .")
        break
media = soma/contador 
print(f"\nMédia: {media}") 

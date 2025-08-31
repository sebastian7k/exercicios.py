import os 
os.system("cls")

print ("Cárdapio do restaurante")
print ("1 - Picanha - R$ 25,00")
print ("2 - Lasanha - R$ 20,00")
print ("3 - Strogonoff - R$ 18,00")
print ("4 - Bife Acebolado - R$ 15,00")
print ("5 - Pão com ovo - R$ 5,00")

codigo = int(input("Digite o número relacionado ao seu prato: "))

#variaveis para amarzenamento 

prato = ""
valor = 0.0

match codigo: 
    case 1:
        prato = "Picanha"
        valor = 25.00       
    case 2:
        prato = "Lasanha"
        valoer = 20.00 
    case 3:
        prato = "Strogonoff"
        valor = 18.00
    case 4:
        prato = "Bife Acebolado"
        valor = 15.00
    case 5:
        prato = "Pão com ovo"
        valor = 5.00
    case _:
        prato = "Prato inválido"
        valor = 0.0

print("\n==== Seu pedido ====")
if valor is not None:
    print (f"Prato escolhido: {prato}")
    print (f"Valor: R$ {valor:2.2f}")
else:
    print("Prato inválido. Por favor, escolha um prato válido do cardápio.")
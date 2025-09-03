import os 
os.system("cls")

print("""
Codigo \t Prato \t\t\t valor
1 \t Picanha \t \tR$ 25.00
2 \t Lasanha \t \tR$ 20.00
3 \t Strogonoff \t \tR$ 18.00
4 \t Bife Acebolado \tR$ 15.00
5 \t Pão com ovo \t \tR$ 5.00
""")

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
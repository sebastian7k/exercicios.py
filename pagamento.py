import os
os.system("cls")
#solicitando valores  e forma de pagamento
valor = float(input("Digite o valor total da compra: R$ "))

print("\n=== Forma de Pagamento ===")

print("1 - À vista")
print("2 - Parcelado")

forma = int(input("Escolha a forma de pagamento (1 ou 2): "))

match forma:
    case 1: #avista
        desconto = valor * 0.10 #para calcular descoto se houver 
        total = valor - desconto
        print(f"\nPagamento à vista")
        print(f"Valor do produto: R$ {valor:2.2f}")
        print(f"forma de pagamento: À vista")
        print(f"Valor do desconto: R$ {desconto:2.2f}")
        print (f"Valor total a pagar: R$ {total:2.2f}")
    case 2: #parcelado
        parcelas = int(input("Digite o número de parcelas (2 a 6): "))
        if 2 <= parcelas <= 6:
            valor_parcela = valor / parcelas
            print(f"\nPagamento parcelado")
            print(f"Valor do produto: R$ {valor:2.2f}")
            print(f"Forma de pagamento: Parcelado em {parcelas}x")
            print(f"Valor de cada parcela: R$ {valor_parcela:2.2f}")
            print(f"Valor total a pagar: R$ {valor:2.2f}")
        else:
            print("Número de parcelas inválido. Por favor, escolha entre 2 e 6 parcelas.")
    case _:
        print("Forma de pagamento inválida. Por favor, escolha 1 ou 2.")

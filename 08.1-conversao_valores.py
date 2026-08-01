# Criação da constante com valor do dólar
DOLAR = 5.50

valor_em_dolar = float(input("Digite o valor em dólares"))
valor_em_real =valor_em_dolar * DOLAR

print(f"O valor convertido em reais e R$ {valor_em_real:2f}".replace(' , ', ','))
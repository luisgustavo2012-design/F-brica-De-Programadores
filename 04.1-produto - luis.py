# Criando as variáveis e solicitando os valores ao usuário
nome_produto = input("Digite o nome do produto: ")
preco = float(input(" Digite o preço do produto: "))
desconto =  input("Digite o percentual de desconto: ")

#calculando o desconto e o preço final
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto


# Apresentando o preço final ao usuário
print(f"Produto: {nome_produto}- preco final: R$ (preco_final)")
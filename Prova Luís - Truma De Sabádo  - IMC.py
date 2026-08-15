# Atividade Luís Gustavo

peso = float(input("digite seu peso em kg: "))
altura = float(input("digite sua altura em metros: "))
nome = input("digite seu nome: ")

# Resolução
imc = peso / (altura ** 2)

print("-----------------------------------")

print(f"nome:{nome}")
print(f"IMC:{imc:.2f}")

print("-----------------------------------")

if imc  <= 18.5:
    print("abaixo do peso.")
elif imc <= 24.9:
    print("peso normal.")
elif imc <= 29.9:
    print("acima do peso.")
elif imc <= 34.9:
    print("obesidade grau 1.")
elif imc <= 39.9:
    print("obesidade grau 2.")
else: 
    print("obesidade grau 3.")

    print("--------------------------------")

    if imc <+ 30:
        print("tudo ok.")
    else:
        print("cuidado com a saúde.")
    print("--------------------------------")
# Lista Inicial
nomes = ["Joaquim","Maria","Ana"]
print("Lista Inicial: ", nomes)

# Adicionando Elementos
nomes.append("carlos") # adicional ao final da lista
print("Após append ", nomes)

nomes.insert(1, "Fernanda") # insere fernanda no índice 1
print("Após insert ", nomes)

# Modificando Elementos
nomes[2] = "Paulo" #modifica o elemento no indice 2
print("Após modificação ", nomes)

# Removendo Elementos
del nomes[3] # remove o elemento de índice 3
print("Após del ", nomes)


nomes.remove("Maria") # remove a primeira incidencia de Maria
print(f"Após pop(removido {removido})", nomes)

removido = nomes.pop(2)
print("apos pop ( removido (remoido))",nomes)

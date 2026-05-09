nome = input("Digite o nome do atleta: ")
idade = int(input("Digite a idade do atleta: "))
altura = float(input("Digite a altura do atleta em metros: "))
categoria = input("Qual categoria do atleta: ")

print("="*50)
print(f"{"Cartão de atleta":^50}")
print("="*50)

	print(f"{"Nome: ":<20}{nome.upper().strip()}")
	print(f"{"Idade: ":<20}{idade}")
	print(f"{"Altura: ":<20}{altura:.2f} Metros")
	print(f"{"Categoria: ":<20}{categoria}")

print("="*50)

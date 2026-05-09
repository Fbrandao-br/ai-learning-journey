# CONSELHO DE NOTAS

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

maior = max(nota1, nota2, nota3)
menor = min(nota1, nota2, nota3)

print(f"O sua média de nota é: {((nota1 + nota2 + nota3) / 3):.1f}")
print(f"Sua maior nota é: {maior}:.1f")
print(f"Sua menor nota é: {menor}:.1f")

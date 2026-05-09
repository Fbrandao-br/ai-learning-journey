#============================
#EXERCICIOS 2
#============================


valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
  print(f"O maior número é {valor1}")
else:
  print(f"O maior número é {valor2}")

#=========================================================
#-- Maneira feita
perct = float(input('Digite o percentual da empresa: '))

if perct > 0:
  print(f"Tivemos um aumento de {perct}%")
else:
  print(f"Tivemos um decrescimento de {perct}%")

# Boas Praticas 
perct = float(input('Digite o percentual da empresa: '))

if perct > 0:
    print(f"Tivemos um aumento de {perct}%")
elif perct < 0:
    print(f"Tivemos um decrescimento de {perct}%")
else:
    print("Não houve crescimento nem decrescimento")

# =========================================================

letra = input("Digite uma letra: ")

letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print("A letra é uma vogal")
else:
  print("A letra é uma consoante")

# =========================================================
# ---------- Maneira feita
preco1 = int(input('Valor do carro primeiro ano: '))
preco2 = int(input('Valor do carro segundo ano: '))
preco3 = int(input('Valor do carro terceiro ano: '))

if preco1 > preco2 and preco2 > preco3:
    print(f"O valor R${preco1} é o maior e o R${preco3} é o menor")
elif preco1 > preco3 and preco3 > preco2:
    print(f"O valor R${preco1} é o maior e o R${preco2} é o menor")
elif preco2 > preco1 and preco1 > preco3:
    print(f"O valor R${preco2} é o maior e o R${preco3} é o menor")
elif preco2 > preco3 and preco3 > preco1:
    print(f"O valor R${preco2} é o maior e o R${preco1} é o menor")
elif preco3 > preco1 and preco1 > preco2:
    print(f"O valor R${preco3} é o maior e o R${preco2} é o menor")
elif preco3 > preco2 and preco2 > preco1:
    print(f"O valor R${preco3} é o maior e o R${preco1} é o menor")

# ------- Boas praticas

preco1 = int(input('Valor do carro primeiro ano: '))
preco2 = int(input('Valor do carro segundo ano: '))
preco3 = int(input('Valor do carro terceiro ano: '))

maior = max(preco1, preco2, preco3)
menor = min(preco1, preco2, preco3)

print(f"O maior valor é R${maior}")
print(f"O menor valor é R${menor}")

# =========================================================
# -----------Maneira feita
prod1 = input("Produto 1: ")
preco1 = int(input('Valor produto 1: '))
prod2 = input("Produto 2: ")
preco2 = int(input('Valor produto 2: '))
prod3 = input("Produto 3: ")
preco3 = int(input('Valor produto 3: '))

if preco1 > preco2 and preco2 > preco3:
  print(f"Compre o {prod3}")
elif preco2 > preco1 and preco1 > preco3:
  print(f"Compre o {prod3}")
elif preco3 > preco1 and preco1 > preco2:
  print(f"Compre o {prod2}")
elif preco1 > preco3 and preco3 > preco2:
  print(f"Compre o {prod2}")
else:
  print(f"Compre o {prod1}")

#  --------Boas praticas

prod1 = input("Produto 1: ")
preco1 = int(input('Valor produto 1: '))
prod2 = input("Produto 2: ")
preco2 = int(input('Valor produto 2: '))
prod3 = input("Produto 3: ")
preco3 = int(input('Valor produto 3: '))

if preco1 <= preco2 and preco1 <= preco3:
    print(f"Compre o {prod1}")
elif preco2 <= preco1 and preco2 <= preco3:
    print(f"Compre o {prod2}")
else:
    print(f"Compre o {prod3}")

# =========================================================
# --------- Maneira feita

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))
valor3 = int(input("Digite o terceiro número: "))

if valor1 > valor2 and valor2 > valor3:
  print(f"Sequencia {valor1}, {valor2}, {valor3}")
elif valor1 > valor3 and valor3 > valor2:
  print(f"Sequencia {valor1}, {valor3}, {valor2}")
elif valor2 > valor1 and valor1 > valor3:
  print(f"Sequencia {valor2}, {valor1}, {valor3}")
elif valor2 > valor3 and valor3 > valor1:
  print(f"Sequencia {valor2}, {valor3}, {valor1}")
elif valor3 > valor1 and valor1 > valor2:
  print(f"Sequencia {valor3}, {valor1}, {valor2}")
else:
  print(f"Sequencia {valor3}, {valor2}, {valor1}")

# ---- Boas praticas

lista = [valor1, valor2, valor3]
lista.sort(reverse=True)

print(lista)
  
# =========================================================

turno = input("Qual seu turno(manhã, tarde ou noite): ")

turno = turno.replace("ã", "a").replace("Ã", "a").lower()

if turno == "manha":
  print("Bom dia!")
elif turno == "tarde":
  print("Boa tarde!")
elif turno == "noite":
  print("Boa noite!")
else:
  print("Valor inválido")

# =========================================================

numero = int(input('Digite um número: '))

if numero % 2 == 0:
  print(f'O número {numero} é par')
else:
  print(f'O número {numero} é ímpar')

# =========================================================

numero = float(input("Digite um número: "))

if numero.is_integer():
    print("O número é inteiro")
else:
    print("O número é decimal")

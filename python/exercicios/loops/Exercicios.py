valor1 = int(input("Digite o número: "))

fator = 1

for contador in range(1, valor1 + 1):

  fator *= contador
  contador += 1

print(f"O valor fatorial de {valor1} é {fator}")

#==================================================================================

contador = 1

while contador <= 15:
  nota = int(input(f'Digite {contador}° nota de 0 a 5: '))
  
  if 0 <= nota <= 5:
    contador += 1
  else:  
    print('Nota inválida')
#=====================================================================================

dias = 0

bacteriaA = 4
bacteriaB = 10

while int(bacteriaA) <= int(bacteriaB):
  bacteriaA += bacteriaA * 0.03
  bacteriaB += bacteriaB * 0.015 
  dias += 1

print(f'Quantidade de {dias} dias')
print(f'Bacteria A: {int(bacteriaA)} Elementos')
print(f'Bacteria B: {int(bacteriaB)} Elementos')


idade = int(input('Digite a idade: '))

de_0_25 = 0
de_26_50 = 0
de_51_75 = 0
de_76_100 = 0

while idade >= 0 :

  if idade>= 0 and idade <= 25:
    de_0_25 += 1
  elif idade >= 26 and idade <= 50:
    de_26_50 += 1
  elif idade >= 51 and idade <= 75:
    de_51_75 += 1
  elif idade >= 76 and idade <= 100:
    de_76_100 += 1
  else:
    print('Idade inválida')

  idade = int(input('Digite a idade (Digitar um numero negativo para encerrar): '))

print(f'Pessoas com idade entre 0 e 25 anos: {de_0_25}')
print(f'Pessoas com idade entre 26 e 50 anos: {de_26_50}')
print(f'Pessoas com idade entre 51 e 75 anos: {de_51_75}')
print(f'Pessoas com idade entre 76 e 100 anos: {de_76_100}')

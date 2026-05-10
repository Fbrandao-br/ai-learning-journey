candidata1 = 0
candidata2 = 0
candidata3 = 0
candidata4 = 0
nulo = 0
branco = 0

for funcionarios in range (1, 21):
  voto = int(input('Digite o seu voto: '))

  while voto <= 0 or voto >6:
    print("Voto inválido")
    voto = int(input(f"Digite novamente: "))

  if voto == 1:
    candidata1 += 1
  elif voto == 2:
    candidata2 += 1
  elif voto == 3:
    candidata3 += 1
  elif voto == 4:
    candidata4 += 1
  elif voto == 5:
    nulo += 1
  elif voto == 6:
    branco += 1
    

perctN = nulo / 20 * 100
perctB = branco / 20 * 100

if (
    candidata1 > candidata2 and
    candidata1 > candidata3 and
    candidata1 > candidata4
):
    print("A candidata 1 venceu a eleição")

elif (
    candidata2 > candidata1 and
    candidata2 > candidata3 and
    candidata2 > candidata4
):
    print("A candidata 2 venceu a eleição")

elif (
    candidata3 > candidata1 and
    candidata3 > candidata2 and
    candidata3 > candidata4
):
    print("A candidata 3 venceu a eleição")

elif (
    candidata4 > candidata1 and
    candidata4 > candidata2 and
    candidata4 > candidata3
):
    print("A candidata 4 venceu a eleição")

else:
    print("A eleição terminou empatada")

print(f"O total de votos da Candidata 1 é: {candidata1}")
print(f"O total de votos da Candidata 2 é: {candidata2}")
print(f"O total de votos da Candidata 3 é: {candidata3}")
print(f"O total de votos da Candidata 4 é: {candidata4}")
print(f"A porcentagem de votos nulos foi de {perctN}% com o total de {nulo} votos")
print(f"A porcentagem de votos brancos foi de {perctB}% com o total de {branco} votos")

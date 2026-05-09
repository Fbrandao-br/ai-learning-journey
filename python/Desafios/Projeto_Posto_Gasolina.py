combustivel = input('Digite o tipo de combustível(Etanol ou Diesel): ')
litros = float(input('Digite a quantidade de litros para abastecer: '))

if litros <= 0:
    print("Quantidade inválida")
    exit()

combustivel = combustivel.strip().lower()

if combustivel == 'etanol':

    preco = 1.70

    if litros <= 15:
        desc = 0.02
    else:
        desc = 0.04

elif combustivel == 'diesel':

    preco = 2.00

    if litros <= 15:
        desc = 0.03
    else:
        desc = 0.05
else:
  print('Quantidade ou tipo inválidos')
  exit()

valordesc = preco*litros*desc
total = preco*litros - valordesc

print(f"Foi abastecido {litros} litros de {combustivel} com {desc*100}% de desconto o valor a pagar é R${total:.2f}")

numero = int(input('Digite um número: '))

# Numero maior ou igual a 1
if numero > 1:
  # criar um contador que no caso sera o nosso divisor do numero dois até o numero anterior ao numero escolhido 
  for divisor in range(2, numero):
    # Se fizer todas as divisões do numero pelo divisor e alguma restar zero o numero não é primo
    if (numero % divisor) == 0:
      print(f'O número {numero} não é primo')
      break
  # Senão é primo
  else:
    print(f'O número {numero} é primo')
else:
  print(f'Não é primo')

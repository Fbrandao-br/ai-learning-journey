# Calculadora

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
print(""" Utilize os seguintes simbolos:
'+' soma
'-' subtração
'*' multiplicação
'/' divisão
'**' potenciação
""")
operacao = input('Digite o simbolo da operação: ')


if operacao == '+':
  valor = number1 + number2
elif operacao == '-':
  valor = number1 - number2
elif operacao == '*':
  valor = number1 * number2
elif operacao == '/':
  valor = number1 / number2
elif operacao == '**':
  valor = number1 ** number2
else:
  print('Operação inválida')
  exit()

if valor == int(valor):
    if valor % 2 == 0:
        tipo = 'par'
    else:
        tipo = 'ímpar'
else:
    tipo = 'não se aplica'
    
if valor > 0:
  sinal = 'positivo'
elif valor < 0:
  sinal = 'negativo'
else:
  sinal = 'neutro'

if valor == int(valor):
    casa = "Inteiro"
else:
    casa = "Decimal"

print(f"O seu resultado é: {valor} que é um numero {tipo} e {sinal} e {casa}")

valor2022 = float(input("Digite o valor de venda do primeiro ano: "))
valor2023 = float(input("Digite o valor de venda do segundo ano: "))

if valor2022 <= 0:
    print("Valor inicial inválido")
    exit()

variacao = ((valor2023 - valor2022) / valor2022) * 100

print(f"Variação percentual: {variacao:.2f}%")

if variacao > 20.0:
  print("Bonificação ao time de vendas !!!")
elif 2.0 <= variacao <= 20.0:
  print("pequena bonificação para time de vendas.") 
elif -10.0 <= variacao < 2.0:
  print('planejamento de políticas de incentivo às vendas.')
else:
  print("Corte de gastos")

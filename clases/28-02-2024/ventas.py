mes = ["octubre", "noviembre", "diciembre"]
ventas = [650000, 68000, 72000]

dic = {k:v for k, v in zip(mes, ventas)}

dic_10 = {k:v * 1.1 for k,v in dic.items()}
div_20 = {k:v * 0.8 for k,v in dic.items()}

print(dic)
print(dic_10)
print(div_20)
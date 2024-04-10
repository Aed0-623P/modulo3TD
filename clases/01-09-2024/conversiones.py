import sys

currency = {

}

solp = float(sys.argv[1])
parg = float(sys.argv[2])
usd = float(sys.argv[3])
clp = float(sys.argv[4])

currency  ["Sol"] = solp
currency  ["PesoArg"] = parg
currency ["USD"] = usd
currency ["CLP"] = clp




print(f"Los 10000 pesos equivalen a:")
print(f"{solp*clp} Soles")
print(f"{parg*clp} Pesos argentinos")
print(f"{usd*clp} Dólares")
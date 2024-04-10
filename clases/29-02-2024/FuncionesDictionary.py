dic = {"nombre" : "carlos",
       "apellido" : "alvarez",
       "edad": 45,
       "altura": 1.66,
       "estado civil": "soltero",       
}

print(dic)

#crear lave nueva
dic["profesion"] = "pastero"
print(dic)

#modificar clave existente

dic["edad"] = 69
print(dic)

#eliminar una clave con pop

elemento = dic.pop("altura")
print(elemento)
print(dic)

#eliminar con del

del(dic["edad"])
print(dic)

#printear keys y values

dic_key = dic.keys()
dic_values = dic.values()

print(dic_key, dic_values)

#get value

gv = dic.get("nombre", "")
print(gv)


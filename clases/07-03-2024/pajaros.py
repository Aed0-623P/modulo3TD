from string import Template
from get import request_get

response = request_get("https://aves.ninjas.cl/api/birds")[:10] #pedir la api de los pajaritos, modificable para mostrar más pajaritos

img_template = Template('<img src="$url">') #template imagenes

nomb_template = Template('<h2>$spanish</h2><h3>$english</h3>') #template textos, ambos para que esten "juntos y separados"

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves de Chile</title>
                            </head>
                            <body>
                            <h1>Aves de Chile</h1>
                            $body
                            </body>
                            </html>
                        ''')
cuerpo="" #lo que se va a asignar al body del html

for elemento in response:
    url = elemento["images"]["main"] #foto 1
    nomb_esp = elemento["name"]["spanish"] #nombre español
    nomb_eng = elemento["name"]["english"] #nombre inglés
    cuerpo += img_template.substitute(url=url) + "\n" #insertar foto a cuerpo (futuro body)
    cuerpo += nomb_template.substitute(spanish=nomb_esp, english=nomb_eng) + "\n" #insertar nombres a cuerpo (futuro body)

html = html_template.substitute(body=cuerpo) #joinear todo

with open("output.html", "w") as f:
    f.write(html)
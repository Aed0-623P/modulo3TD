import requests

url_base = "https://reqres.in/api/users"
response = requests.get(url_base)
user_data =response.json()

#consumir/print
print(user_data)


created_user = {'id': 7,
    'email': 'ignacio.ramos@prueba.com',
    'first_name': 'ignacio',
    'last_name': 'Ramos',
    'avatar': 'https://reqres.in/img/faces/6-image.jpg',
    'profesión': "profesor",
}

print(created_user)

updated_user = {'id': 8,
    'email': 'm.orf@marvel.lol',
    'first_name': 'morpheus',
    'last_name': 'Ramos',
    'avatar': 'https://reqres.in/img/faces/6-image.jpg',
    'residence': "zion",
}

print(updated_user)

response = requests.delete("https://reqres.in/api/users/6")

print(response)


organisations=[]
organisations_a={
    "name":"Tesla",
    "adress":"Tesla avenue 1,USA",
    "id":"92352",
    "contacts":[
        {
            "name":"Elon",
            "position":"CEO",
            "id":1
        },
            {
            "name":"Uber",
            "position":"CTO",
            "id":2 
        }
    ]
}
organisations_b={
    "name":"Dainito",
    "adress":"Daun avenue 2,Latvija",
    "id":"125423",
    "contacts":[
        {
            "name":"Elon",
            "position":"CEO",
            "id":1
        },
            {
            "name":"Uber",
            "position":"CTO",
            "id":2 
        }
    ]
}


organisations.append(organisations_a)
organisations.append(organisations_b)

print(organisations)

for organisation in organisations:
    print('---ORGANISATION---')
    print(f"{organisation['name']}({organisation['id']})")
    print(f"Adrese:{organisation['adress']}")
    print(f"Kontaktu skaits: {len(organisation['contacts'])}")

organisations=[]


print(organisations)


while (True):
    response=input("(1) Add organisation (2) Print organisations (3) Exit ")
    if response=="1":
        organisation_name=input("Organisation name:")
        organisation_adress=input("Organisation adress:")
        organisation_id=input("Organisation id:")

        organisation={
            "name":organisation_name,
            "adress":organisation_adress,
            "id":organisation_id,
            "contacts":[]
        }

        while True:
            response=input("Do you want to add a contact(y/n)")
            if response=='y':
                contact_name=input("Contact name: ")
                contact_position=input("Contact position: ")
                contact_id=input("Contact id: ")

                contact={
                    'name':contact_name,
                    'position':contact_position,
                    'id':contact_id,
                }

                organisation['contacts'].append(contact)

            elif response=='n':
                break


        organisations.append(organisation)

    elif response =="2":
        for organisation in organisations:
            print('---ORGANISATION---')
            print(f"{organisation['name']}({organisation['id']})")
            print(f"Adrese:{organisation['adress']}")
            print(f"Kontaktu skaits: {len(organisation['contacts'])}")
    elif response =="3":
        print("byeeeeeeeeeeeee!")
        exit()



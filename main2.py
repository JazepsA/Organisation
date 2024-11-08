import json

organisations=[]


#print(organisations)

# ielasa datus no json formata un  pardeve tos vardnica
def load_data():
    file=open('organisations.json','r')
    data=json.load(file)
    file.close()
    global organisations
    organisations=data['organisations']
    print("Dati loaded")


def add_organisation():
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
        
def print_organisation():
    for organisation in organisations:
            print('---ORGANISATION---')
            print(f"{organisation['name']}({organisation['id']})")
            print(f"Adrese:{organisation['adress']}")
            print(f"Kontaktu skaits: {len(organisation['contacts'])}")

def save_data():
    data={
            'organisations': organisations
        }
    print('saving data...')
    file = open('organisations.json',"w")
    json.dump(data,file,indent=4)
    print("Data saved!")

def find_organisation_by_id():
    organisation_id=input("Ievadiet organizacijas ID,kuru info velaties atrast: ")
    for organisation in organisations:
          if organisation['id']== organisation_id:
               print("---ORGANIZACIJA---")
               print(f"{organisation['name']}({organisation['id']})")
               break #talak neturpina ciklu jo mes jau atradam

def count_organisations():
    print(f"Ievadīto organizaciju skaits ir :{len(organisations)} ")

def list_organisation_ids():
    for i in organisations:
        print(i['id'])

def organisation_exists():
    a=input("Ievadiet organizacijas id ,kuru velaties uzzinat ,vai tas ir?: ")
    for organisation in organisations:
        if organisation['id'] == a:
            print(f"Organizācijas id {a} eksistē!")

        else:
            pass
    
def delete_organisation_by_id():
    b=input("Ievadiet organizacijas id ,kuru velaties izdzēst: ")
    for organisation in organisations:
            if organisation['id']== b:
                organisations.remove(organisation)
            else:
                pass

def main():
    load_data()
    find_organisation_by_id()
    count_organisations()
    list_organisation_ids()
    organisation_exists()
    delete_organisation_by_id()
    while (True):
        response=input("(1) Add organisation (2) Print organisations (3) Exit ")
        if response=="1":
            add_organisation()
        elif response =="2":
            print_organisation()
        elif response =="3":
            save_data()
            print("Bye bye!")
            exit()
        else:
            print("Choose a number between 1 and 3")
            continue
main()

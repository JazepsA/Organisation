import json
import datetime

Haggy=[]


#print(organisations)

# ielasa datus no json formata un  pardeve tos vardnica

def load_data():
    file=open('Haggy.json','r')
    data=json.load(file)
    file.close()
    global Haggy
    Haggy=data['Haggy']
    print("Dati loaded")



def add_info():
        vai=input("Vai velaties ievadit jaunu apmeklejumu(y/n): ")
        if vai=='y':
            id=input("Ievadiet id: ")
            vards=input("Ievadiet vārdu: ")
            talrunis=input("Ievadiet savu telefona nr.: ")
            pilseta=input("Ievadiet savu pilsetu: ")

        else:
            pass

        info={
            "id":id,
            "vards":vards,
            "talrunis":talrunis,
            "pilseta":pilseta,
            "apmekletajs":[]
        }
        while True:
            response=input("Gribat ievadīt apmeklējuma rezi(y/n): ")
            if response=='y':
                st=input("Stundu daudzums: ")
                berni=input("Bērnu daudzums: ")
                print("Datums ,kad pieteikums ir veikts: ")
                print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                udens=int(input("Vai velaties udeni(cik): "))
                if udens >=1:
                    cenaUdenim=0.45
                    reizinajums=udens*cenaUdenim
                    print(f"Te ir cena,cik ir jasamaksa par nopirkto udeni : {reizinajums} eiro")
                else:
                     pass
                

                apmeklejums={
                    'stundas':st,
                    'bernuDaudzums':berni,
                    'datums':datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'udens':udens,
                }

                info['apmekletajs'].append(apmeklejums)

            elif response=='n':

                break

        Haggy.append(info)
        
def print_apmektetajs():
    for i in Haggy:
            print('Apmekletaju info!')
            print(f"\n{i['vards']}(id:{i['id']},{i['talrunis']},{i['pilseta']}")

def save_data():
    data={
            'Haggy': Haggy
        }
    print('saving data...')
    file = open('Haggy.json',"w")
    json.dump(data,file,indent=4)
    print("Data saved!")

def find_info_by_id():
    id=input("Ievadiet organizacijas ID,kuru info velaties atrast: ")
    for a in Haggy:
          if a['id']== id:
               print("Cilveks")
               print(f"{a['vards']} , id: {a['id']}")



global info

def pievienot():
    while True:
            response=input("Gribat ievadīt apmeklējuma rezi(y/n): ")
            if response=='y':
                st=input("Stundu daudzums: ")
                berni=input("Bērnu daudzums: ")
                print("Datums ,kad pieteikums ir veikts: ")
                print(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
                udens=int(input("Vai velaties udeni(cik): "))
                if udens >=1:
                    cenaUdenim=0.45
                    reizinajums=udens*cenaUdenim
                    print(f"Te ir cena,cik ir jasamaksa par nopirkto udeni : {reizinajums} eiro")
                else:
                     pass
                

                apmeklejums={
                    'stundas':st,
                    'bernuDaudzums':berni,
                    'datums':datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                    'udens':udens,
                }

                ['apmekletajs'].append(apmeklejums)

            elif response=='n':

                break

    Haggy.append['apmekletajs'].append(apmeklejums)
    






def main():
    load_data()
    #add_info()
    #print_apmektetajs()
    #save_data()
    #find_info_by_id()
    while (True):
        response=input("(1) Add information (2) Print info (3) Exit un saglabat info (4) atrast cilveku ar id ")
        if response=="1":
            add_info()
        elif response =="2":
            print_apmektetajs()
        elif response =="3":
            save_data()
            print("Bye bye!")
            exit()
        elif response =="4":
            find_info_by_id()
            pievienot()
            save_data()
            print("Bye bye!")
            exit()
        else:
            print("Choose a number between 1 and 4")
            continue
main()

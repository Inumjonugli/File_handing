# Qambaraliyev Ro'zimuhammad Inomjon o'g'li.
# 5-normativ Talabalar Ma’lumotlarini Boshqarish.


f0 = 'students.txt'
talabalar = ['Ali,Mathematics,85','Vali,Physics,90','Hasan,Computer Science,95','Akmal,Chemistry,80']

def create_file():
    with open(f0,'w') as y:
        for i,t in enumerate(talabalar,1):
            ism,fan,bal = t.split(',')

            yoz = {
                'ID':i,
                'Ism':ism,
                'Fan':fan,
                'Baho':bal
            }
            y.write(f"{yoz['ID']},{yoz['Ism']},{yoz['Fan']},{yoz['Baho']}\n")

def read_file():
    student = []
    with open(f0,'r') as o:
        r1 = o.read()
        print(r1)

def add_file(ism,fan,bal):
    with open(f0,'r') as o:
        soni = sum(1 for _ in o)

    with open(f0,'a') as q:
        i = soni+1
        yoz = {
                'ID':i,
                'Ism':ism,
                'Fan':fan,
                'Baho':bal
            }
        
        y.write(f"{yoz['ID']},{yoz['Ism']},{yoz['Fan']},{yoz['Baho']}\n")
        print(f"{yoz['Ism']} qo'shildi")

    return ''

def serch_file(id1):
    with open(f0,'r') as o:
        top = False
        for line in o:
            id,ism,fan,bal = line.split(',')
            if id1==id:
                print(f"ID:{id}, Ism : {ism}, Fan : {fan}, Bal : {bal}")
                top = True
                break
        if not top:
            print("Bunday 'ID' ga ega o'quvchi yo'q" )
    return ''

def update_file(ism,bal):
    yangi = []
    with open(f0,'r') as u:
        for tal in u:
            id,ism1,fan1,bal1 = tal.split(',')
            if ism==ism1:
                bal1=bal
            
            yangi.append(f"{id},{ism1},{fan1},{bal1}\n")
    with open(f0,'w') as up:
        up.writelines(yangi)
    
def delete_student(ism):
    delat = []

    with open(f0,'r') as u:
        for tal in u:
            id,ism1,fan1,bal1 = tal.split(',')
            if ism!=ism1:
                delat.append(f"{id},{ism1},{fan1},{bal1}\n")
            else:
                print(f"{ism} o'chirildi")
    with open(f0,'w') as up:
        up.writelines(delat)
    return ''

def total():
    create_file()

    while True:
        print('Talabalarni boshqatish tizimi')
        print("1. Barcha talabalarni ko'rish")
        print("2. Yangi talaba qo'shish")
        print("3. Talabani 'ID' bilan qidirish")
        print("4. Bahoni yangilash")
        print("5. Talabani o'chirish")
        print("6. Chiqish")

        tan = input("Tanlang (1-6) : ")

        if tan=='1':
            read_file()
        elif tan == '2':
            ism = input("Ism kiriting : ")
            fan = input("Fan kiriting : ")
            ball = input("Baho kiriting : ")

            add_file(ism,fan,ball)
        
        elif tan == '3':
            print("O'quvchini 'ID' raqamini kiriting")
            id1 = input("ID : ")
            serch_file(id1)
        elif tan == '4':
            ism = input('Talaba : ')
            bal = input('Yangi bal : ')
            update_file(ism,bal)
        elif tan=='5':
            ism = input("O'chiriladigan talaba ismi : ")
            delete_student(ism)
        elif tan=='6':
            print("Dastur yakunlandi")
            break
            
        else:
            print("Noto'g'ri tanlov. Iltimos (1-6) oralig'ida raqam kiriting")
total()




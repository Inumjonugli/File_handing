# Qambaraliyev Rozimuhammad Inomion o'g'li
# 7-normativ. Restoran uchun taomlar menyusini boshqaruvchi dastur.


class Dish:
    def __init__(self,name,tavsif,price):
        self.name = name
        self.tavsif = tavsif
        self.price = price

    def get_info(self):
        return self.name,  self.tavsif ,self.price

class Stater(Dish):
    def __init__(self, name, tavsif, price):
        super().__init__(name, tavsif, price)

class MainCourse(Dish):
    def __init__(self, name, tavsif, price,vegetarian = False, gluten_free = False):
        super().__init__(name, tavsif, price)
        self.veget = vegetarian
        self.glut = gluten_free

    def __str__(self):
        t0 = []
        if self.veget:
            t0.append('Vegetarian')
        if self.glut:
            t0.append('Gliten-free')
        t2 = ','.join(t0) if t0 else ''
        return f"{super().get_info()}{t2}"

class Desert(Dish):
    def __init__(self, name, tavsif, price,vegetarian = False, gluten_free = False):
        super().__init__(name, tavsif, price)
        self.veget = vegetarian
        self.glut = gluten_free
    def __str__(self):
        t0 = []
        if self.veget:
            t0.append('Vegetarian')
        if self.glut:
            t0.append('Gliten-free')
        t2 = ','.join(t0) if t0 else ''
        return f"{super().get_info()}{t2}"

class Menu:
    def __init__(self):
        self.meals = []

    def add_meal(self,new_meal):
        self.meals.append(new_meal)
        return f"{new_meal['Nomi']} ro'yhatga qo'shildi"

    def del_meal(self,m_name):
        for k in self.meals:
            if k['Nomi'] == m_name:
                self.meals.remove(k)
                print(f"{k["Nomi"]} o'chrildi")
        else:
            print("Taom menyuda yo'q")
        return ''

    def get_menu(self):
        if self.meals:
            for m in self.meals:
                print(m)
        else:
            print("Taomlar yo'q")
        return ''
    def get_name(self):
        for n in self.meals:
            jav = n['Nomi']
            print(jav)
        return ''

class Order:
    def __init__(self,menu):
        self.menu = menu
        self.buyurtma = []
    
    def get_buyurtma(self,buyu):
        if buyu:
            for b1 in buyu:
                b3 = False
                for b2 in self.menu.meals:
                    if b1==b2['Nomi']:
                        b1=b2
                        self.buyurtma.append(b1)
                        print(f"Siz {b1['Nomi']} ni buyurtma qildingiz")
                        b3 = True
                        break
                if not b3:
                    print(f"Kechirasiz menyuda {b1['Nomi']} yo'q")
        else:
            return "Menyu bo'sh" 
    def hisob(self):
        total = 0
        for h in self.buyurtma:
            total += h['Narxi']

        if total >= 100_000:
            dis = total*0.9
            print(f"Umumiy hisob chegitma bilan {dis} so'm")
            
        else:
            print(f"Umumiy hisob {total} so'm")
        return ''

def main():
    menu = Menu()
    order = Order(menu)

    while True:
        print("1. Yangi taom qo'shish\n2. Taomni o'chirish\n3. Menyuni ko'rish\n4 Buyurtma qilish\n5. Dasturdan chiqish")

        try:
            a1 = int(input("Tanlov kiriting (1-5) : "))
            if a1 ==1:
                stop = True
                while stop:
                    name = input("Taom nomi : ")
                    tavsif = input("Tavsifi : ")
                    price = int(input("Narxi : "))
                    print("Taom turi : 1) Starter 2) Asosiy 3) Desert")
                    t = input("Tanlang (1/2/3) : ")
                    if t == '1':
                        dish = Stater(name,tavsif,price)
                    elif t == '2':
                        veg = input("Vegetariyan (ha/yoq) : ").lower() == "ha"
                        gf = input("Gluten-free (ha/yoq) : ").lower() == 'ha'
                        dish = MainCourse(name,tavsif,price,veg,gf)
                    elif t == '3':
                        veg = input("Vegetariyan (ha/yoq) : ").lower() == "ha"
                        gf = input("Gluten-free (ha/yoq) : ").lower() == 'ha'
                        dish = Desert(name,tavsif,price,veg,gf)

                    else:
                        print("Noto'g'ri tanlov")
                        continue
                    new_meal = {
                        'Nomi':dish.name,
                        'Tavsifi':dish.tavsif,
                        'Narxi':dish.price
                    }

                    if isinstance(dish,MainCourse) or isinstance(dish,Desert):
                        new_meal['Vegetaran'] = 'Yes'
                        new_meal['Gluten-Free'] = 'Yes'
                    menu.add_meal(new_meal)
                    print(f"{new_meal['Nomi'].title()} menyuga qo'shildi")
                    stop = input("Yana taom qo'shasizmi? (ha/yoq)").lower()=='ha'

            elif a1 == 2:
                m_name = input("O'chiriladigan taom nomini kiriting : ")
                menu.del_meal(m_name)
            elif a1 == 3:
                menu.get_menu()
            elif a1 == 4:
                buy = input(f"{menu.get_name()} \nMenyudan keraklisini tanlang va vergul bilan yozing (osh,choy,non)")
                buy = [b for b in buy.split(',')]
                order.get_buyurtma(buy)
                order.hisob()
            elif a1 == 5:
                print("Dastur yakunlandi")
                break
            else:
                print("Tanlov 1-5 orasida kiritiishi kerak")
        except ValueError:
            print("Faqat raqamlar kiriting.")

if __name__ == '__main__':
    main()

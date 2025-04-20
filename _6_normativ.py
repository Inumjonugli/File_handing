

# # # Qambaraliyev Ro'zimuhammad Inomjon o'g'li
# # # 6-normativ. Bankdagi hisobdan pul yechish


# # def get_money(money):
# #     balance= 1000
# #     m1 = balance - money

# #     try:
# #         if money<=0:
# #             raise ValueError
# #         elif m1<0:
# #             raise Exception
# #         else:
# #             print(f"{money} so'm hisobdan yechildi. Joriy balans : {m1} so'm")
        
# #     except ValueError:
# #         print("Xatolik : Pul miqdori manfiy yoki nol bo'lmasligi kerak.")
# #     except Exception:
# #         print("Xatolik : Hisobda yetarli mablag' mavjud emas.")
# #     finally:
# #         if money<=0:
# #             pul = balance
# #         elif m1<=0:
# #             pul = balance
# #         else:
# #             pul = m1
# #         return f"Dastur yakunlandi qolgan mablag' {pul} so'm"
    
# # print("Pul yechish tizimiga hush kelibsiz!")
# # mon = int(input("Qancha pul yechmoqchisiz? : "))
# # print(get_money(mon))




# class Dish:
#     def init(self, name, description, price):
#         self.name = name
#         self.description = description
#         self.price = price
    
#     def str(self):
#         return f"{self.name} - {self.description} - {self.price} so'm"

# class Starter(Dish):
#     def init(self, name, description, price):
#         super().init(name, description, price)
    
#     def str(self):
#         return f"[Starter] {super().str()}"

# class MainCourse(Dish):
#     def init(self, name, description, price, is_vegetarian=False, is_gluten_free=False):
#         super().init(name, description, price)
#         self.is_vegetarian = is_vegetarian
#         self.is_gluten_free = is_gluten_free
    
#     def str(self):
#         vegetarian = " (Vegetarian)" if self.is_vegetarian else ""
#         gluten_free = " (Gluten-free)" if self.is_gluten_free else ""
#         return f"[Main Course] {super().str()}{vegetarian}{gluten_free}"

# class Dessert(Dish):
#     def init(self, name, description, price, is_vegetarian=False, is_gluten_free=False):
#         super().init(name, description, price)
#         self.is_vegetarian = is_vegetarian
#         self.is_gluten_free = is_gluten_free
    
#     def str(self):
#         vegetarian = " (Vegetarian)" if self.is_vegetarian else ""
#         gluten_free = " (Gluten-free)" if self.is_gluten_free else ""
#         return f"[Dessert] {super().str()}{vegetarian}{gluten_free}"

# class Menu:
#     def init(self):
#         self.dishes = []
    
#     def add_dish(self, dish):
#         self.dishes.append(dish)
#         print(f"'{dish.name}' menyuga qo'shildi.")
    
#     def remove_dish(self, name):
#         for dish in self.dishes:
#             if dish.name.lower() == name.lower():
#                 self.dishes.remove(dish)
#                 print(f"'{dish.name}' menyudan o'chirildi.")
#                 return
#         print(f"'{name}' nomli taom menyuda topilmadi.")
    
#     def view_menu(self):
#         if not self.dishes:
#             print("Menyu hozircha bo'sh.")
#             return
        
#         print("\n=== MENYU ===")
#         for i, dish in enumerate(self.dishes, 1):
#             print(f"{i}. {dish}")
#         print("=============\n")

# class Order:
#     def init(self, menu):
#         self.menu = menu
#         self.items = []
    
#     def add_item(self, dish_name):
#         for dish in self.menu.dishes:
#             if dish.name.lower() == dish_name.lower():
#                 self.items.append(dish)
#                 print(f"'{dish.name}' buyurtmangizga qo'shildi.")
#                 return
#         print(f"'{dish_name}' nomli taom menyuda topilmadi.")
    
#     def calculate_total(self):
#         total = sum(dish.price for dish in self.items)
        
#         if total > 100000:
#             discount = total * 0.1
#             print(f"Original narx: {total} so'm")
#             print(f"Chegirma (10%): {discount} so'm")
#             total -= discount
        
#         return total
    
#     def view_order(self):
#         if not self.items:
#             print("Buyurtmangiz bo'sh.")
#             return
        
#         print("\n=== BUYURTMA ===")
#         for i, dish in enumerate(self.items, 1):
#             print(f"{i}. {dish}")
#         print("===============\n")

# def main():
#     menu = Menu()
#     order = Order(menu)
    
#     while True:
#         print("\nRestoran Menyusi Boshqaruv Tizimi")
#         print("1. Yangi taom qo'shish")
#         print("2. Taomni o'chirish")
#         print("3. Menyuni ko'rish")
#         print("4. Buyurtma qilish")
#         print("5. Dasturdan chiqish")
        
#         choice = input("Tanlovingizni kiriting (1-5): ")
        
#         if choice == "1":
#             print("\nYangi taom qo'shish:")
#             name = input("Taom nomi: ")
#             description = input("Taom tavsifi: ")
#             price = float(input("Taom narxi: "))
#             dish_type = input("Taom turi (1. Starter, 2. Asosiy taom, 3. Desert): ")
            
#             if dish_type == "1":
#                 dish = Starter(name, description, price)
#             elif dish_type == "2":
#                 vegetarian = input("Vegetarianmi? (ha/yo'q): ").lower() == "ha"
#                 gluten_free = input("Gluten-free? (ha/yo'q): ").lower() == "ha"
#                 dish = MainCourse(name, description, price, vegetarian, gluten_free)
#             elif dish_type == "3":
#                 vegetarian = input("Vegetarianmi? (ha/yo'q): ").lower() == "ha"
#                 gluten_free = input("Gluten-free? (ha/yo'q): ").lower() == "ha"
#                 dish = Dessert(name, description, price, vegetarian, gluten_free)
#             else:
#                 print("Noto'g'ri tanlov!")
#                 continue
            
#             menu.add_dish(dish)
        
#         elif choice == "2":
#             print("\nTaomni o'chirish:")
#             name = input("O'chiriladigan taom nomi: ")
#             menu.remove_dish(name)
        
#         elif choice == "3":
#             menu.view_menu()
        
#         elif choice == "4":
#             print("\nBuyurtma qilish:")
#             menu.view_menu()
#             while True:
#                 dish_name = input("Taom nomini kiriting (tugatish uchun 'tugat' yozing): ")
#                 if dish_name.lower() == "tugat":
#                     break
#                 order.add_item(dish_name)
            
#             order.view_order()
#             total = order.calculate_total()
#             print(f"Jami to'lov: {total} so'm")
#             order = Order(menu)  # Yangi buyurtma uchun
        
#         elif choice == "5":
#             print("Dastur tugatildi. Xayr!")
#             break
        
#         else:
#             print("Noto'g'ri tanlov! Iltimos, 1-5 oralig'idagi raqamlardan birini tanlang.")

# if __name__ == "main":
#     main()
b = {
    'Nomi':'osh'

}
h = "osh"

print(h==b['Nomi'])
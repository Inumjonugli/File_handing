# Qambaraliyev Rozimuhammad Inomion o'g'li
# 7-normativ. Restoran uchun taomlar menyusini boshqaruvchi dastur.

#📍 1-qadam: Oddiy funksiya orqali barcha buyurtmalarni birdan tayyorlash   ["osh", "shashlik", "mastava"]

# def buyurtma(ruy):
#     for r in ruy:
#         print(f"Tayyor bo'ldi : {r}")
#     return ''
# roy = ["osh", "shashlik", "mastava"]
# print(buyurtma(roy))


#📍 2-qadam: Generator yordamida buyurtmalarni navbat bilan chiqarish

# def buyurtma(ruy):
#     for r in ruy:
#         jav = f"Tayyor bo'ldi : {r}"
#         yield jav
#     return ''
# roy = ["osh", "shashlik", "mastava"]
# f1 = buyurtma(roy)
# print(next(f1))
# print(next(f1))
# print(next(f1))



#📍 3-qadam: Dekorator yordamida buyurtmalarni logga yozish

# def log_buyurtma(func):
#     def wrapper(*args,**kwargs):
#         nat = func(*args,**kwargs)
#         print("[LOG] Buyurtmalar qabul qilindi")
#         return nat
#     return wrapper
# @log_buyurtma
# def buyurtma(taom):
#     for r in taom:
#         jav = f"Tayyor bo'ldi : {r}"
#         print(jav)
#     return ''

# roy = ["osh", "shashlik", "mastava"]
# f1 = buyurtma(roy)
# print(f1)



#📍 4-qadam: Har bir buyurtmani 2 soniya kechiktirib tayyorlash
# import time

# def log_buyurtma(func):
#     def wrapper(*args,**kwargs):
#         nat = func(*args,**kwargs)
#         print("[LOG] Buyurtmalar qabul qilindi")
#         return nat
#     return wrapper
# @log_buyurtma
# def buyurtma(taom):
#     for r in taom:
#         time.sleep(2)
#         print("(2 soniya kutish ....)")
#         jav = f"Tayyor bo'ldi : {r}"
#         print(jav)
#     return ''

# roy = ["osh", "shashlik", "mastava"]
# f1 = buyurtma(roy)
# print(f1)

#📍 5-qadam: Cheksiz buyurtmalarni qabul qilish

import time

def log_buyurtma(func):
    def wrapper(*args,**kwargs):
        nat = func(*args,**kwargs)
        print("[LOG] Buyurtmalar qabul qilindi")
        return nat
    return wrapper
@log_buyurtma
def buyurtma():
    nom = True
    while nom:
        nom = input("Qaysi taomlarni buyurtma qilasiz? To'xtatish (stop) : ")
        if nom=="stop":
            print("Dastur yakunlandi")
            break
        else:
            print("(2 soniya kutish ....)")
            time.sleep(2)
            jav = f"Tayyor bo'ldi : {nom}"
            print(jav)
        nom = False if nom=='stop' else True   
        
    return ''


f1 = buyurtma()
print(f1)










# Amaliyot va takrorlash
#18.02.2024
# Muallif: Xalelov Suvrob Umarovich
# Xatolar bilan ishlash
mahsulotlar = ['apple', 'orange', 'banana', 'milk', 'book', 'copybook', 'pen', 'pencil', 'potato']
yangi_savat = []
bor_mahsulotlar = []
mavjud_emas = []
for i in range(5):
    yangi_savat.append(input(f"{i+1}- olmoqchi bo'lgan mahsulotingizni kiriting:\n").lower())
for mahsulot in yangi_savat:
    if mahsulot in mahsulotlar:
       bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("siz so'ragan barcha mahsulot do'konimizda bor")
    


        




    
    
    












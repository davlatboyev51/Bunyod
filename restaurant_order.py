menu = {
    'osh': 50000, 'somsa': 15000, 'shashlik': 25000, 'shorva': 40000, 'manti': 30000,
    'salat': 10000, 'qatiq': 8000, 'choy': 5000, 'kampot': 12000, 'ayron': 10000, 'gazli ichimliklar': 15000
}

print("🥘 Salom, Milliy Taomlar Restoraniga xush kelibsiz! 🏡")
a = input("\n🍽 Buyurtma berasizmi, hurmatli mijoz? (ha/yoq): ").lower()

if a == 'ha':
    buyrtma = {}
    umumiy_hisob = 0
    buy = int(input("📝 Nechta buyurtma berasiz? "))

    for i in range(buy):
        taom = input(f"{i+1}-buyurtma: ").lower()
        
        if taom in menu:
            soni = int(input(f"{taom.title()} nechtadan? "))
            buyrtma[taom] = soni
            umumiy_hisob += menu[taom] * soni
        else:
            print(f"⚠ Kechirasiz, {taom.title()} menuda yo‘q.")

    # Buyurtma natijalari
    print("\n🛎 Buyurtma natijalari:")
    for t, s in buyrtma.items():
        print(f"✅ {t.title()} - {s} dona")

    print(f"\n💰 Umumiy hisob: {umumiy_hisob} so‘m")
    print("🎉 Rahmat! Buyurtmangiz tez orada tayyor bo‘ladi.")

elif a == 'yoq':
    print("👋 Xizmatimizdan foydalanganingiz uchun rahmat!")

else:
    print("⚠ Iltimos, faqat 'ha' yoki 'yoq' deb javob bering.")

# Bunyod
youngle_coder
c=int(input("nechta sonni kvadiratini hisoblashni hohlaysiz: "))
# d=int(input("sonlarni qaysi darajaga kotarmoqchisiz: "))
sonlar =[]
daraja=[]
natija=[]
print(f'{c}ta sonni kiriting: ')
for son in range(c):
    n=int(input((f'{son+1}- sonni kiriting: \n>>> ')))
    d=int(input(f'{n} sonini qaysi darajaga kotarmoqchisz: \n>>> '))
    sonlar.append(n)
    daraja.append(d)
    natija.append(n**d)
print(f'\nasl sonlar royxati: {sonlar}')
print(f'\natija: ')
for s,d,kv in zip(sonlar,daraja,natija):
    print(f'{s}**{d}: {kv}')

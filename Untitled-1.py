zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazení vody"]
kosik = []

def zobraz_kosik():
   print("Obsah košíku:")
   for i, item in enumerate(kosik, start=1):
       print(f"{i}. {item}")

for i, zbozi_polozka in enumerate(zbozi, start=1):
   print(f"{i}. {zbozi_polozka}")
while True:
   volba = input("Zadej číslo položky, kterou chceš přidat do košíku (nebo zadej 'konec' pro ukončení): ")
   if volba.lower() == "konec":
       break
   elif not volba.isdigit() or int(volba) < 1 or int(volba) > len(zbozi):
       print("Neplatná volba. Zadej prosím číslo položky ze seznamu.")
       continue
   else:
       index = int(volba) - 1
       kosik.append(zbozi[index])
       print(f"{zbozi[index]} bylo přidáno do košíku.")
zobraz_kosik()
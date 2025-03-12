# vysvědčení
vysvedceni = {"český jazyk": 1, "matematika": 2, "zeměpis": 1}

print(vysvedceni)


# detektivky

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
print(sales)

sales["Vrah zavolá v deset"] += 100
print(sales)


# tombola

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listku = int(input("Zadej číslo svého lístku: "))
print(cislo_listku)

if cislo_listku in tombola:
  print(f"Gratuluji, vyhráváš cenu: {tombola[cislo_listku]}.")
else: 
  print("Bohužel, dnes nevyhráváš!")


#
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
for key, value in sales.items():
    print(key)
    print(value)
for kniha, kusy in sales.items():
    print(kniha)
    print(kusy)

for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} kusů.")
total_book_sold = sum(sales.values())
print(total_book_sold)

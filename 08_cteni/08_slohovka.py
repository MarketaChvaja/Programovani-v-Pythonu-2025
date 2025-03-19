pocet_slov_na_radku = []
with open("Programovani-v-Pythonu-2025/08_cteni/praha.txt", encoding="utf-8") as file:
    for line in file:
        slova = line.split()
        pocet_slov_na_radku.append(len(slova))
index = 1
for pocet in pocet_slov_na_radku:
    print(f"Řádek {index}: {pocet} slov")
    index += 1
celkovy_pocet_slov = sum(pocet_slov_na_radku)
print(f"Celkový počet slov v textu: {celkovy_pocet_slov}")
if celkovy_pocet_slov >= 150:
    print("Zadání bylo splněno.")
else:
    print("Zadání nebylo splněno.")

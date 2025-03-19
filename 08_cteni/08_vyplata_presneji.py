vykaz = []
with open("Programovani-v-Pythonu-2025/08_cteni/vykaz.txt", encoding="utf-8") as file:
    for line in file:
        pocet_hodin = line
        pocet_hodin = float(pocet_hodin)
        vykaz.append(pocet_hodin)

print(vykaz)


hodinova_mzda = int(input("Zadej svou hodinovou mzdu v Kč."))

print("Tvá hodinová mzda je: ", hodinova_mzda, " Kč.")




celkova_mzda = sum(vykaz) * hodinova_mzda
print(celkova_mzda, " ...tohle sis vydělal za posledních 12 měsíců!")
print(len(vykaz), " ...tolik měsíců jsi odpracoval!")
prumerna_mzda = celkova_mzda / len(vykaz)
print(prumerna_mzda, " ...tolik sis vydělal průměrně za měsíc.")

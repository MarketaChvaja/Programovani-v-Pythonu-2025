# typing a jeho využití - příklad


def zkontroluj_telefonni_cislo_bool(telefonni_cislo: str) -> bool:
    # Začíná s +420 A délka je 13
    if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
        return True
    else:
        return False
def zkontroluj_telefonni_cislo_str(telefonni_cislo: str) -> str:
    # Začíná s +420 A délka je 13
    if telefonni_cislo.startswith("+420") and len(telefonni_cislo) == 13:
        return "OK"
    else:
        return "Číslo musí začínát +420 a mít 13 znaků"

vysledek_1 = zkontroluj_telefonni_cislo_bool("+420734123456")
print(vysledek_1)
vysledek_2 = zkontroluj_telefonni_cislo_bool("test")
print(vysledek_2)
vysledek_1 = zkontroluj_telefonni_cislo_str("+420734123456")
print(vysledek_1)
vysledek_2 = zkontroluj_telefonni_cislo_str("test")
print(vysledek_2)




# bonusove cviceni - delky cisel

cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
delky_cisel = []
for c in cisla:
    c = str(c)
    aktualni_delka = len(c)
    delky_cisel.append(aktualni_delka)
print(delky_cisel)
maximalni_delka = max(delky_cisel)
for c in cisla:
    c = str(c)
    aktualni_delka = len(c)
    c = c.rjust(maximalni_delka, ".")
    print(c)


# varianta

cisla = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
max_cislo = max(cisla)
max_cislo = str(max_cislo)
maximalni_delka = len(max_cislo)
for c in cisla:
    c = str(c)
    c = c.rjust(maximalni_delka, ".")
    print(c)




# body a znamky

data = [
    ["A", 9, 7, 8, 5],
    ["B", 5, 3, 6, 6],
    ["C", 8, 4, 9, 7],
    ["D", 8, 5, 4, 8],
    ["E", 10, 6, 10, 7]
]
for radek in data:
    body_student = sum(radek[1:])
    if body_student > 36:
        znamka = 1
    elif body_student > 32:
        znamka = 2
    elif body_student > 26:
        znamka = 3
    elif body_student > 20:
        znamka = 4
    else:
        znamka = 5
    print(f"Známka studenta {radek[0]} je {znamka}.")

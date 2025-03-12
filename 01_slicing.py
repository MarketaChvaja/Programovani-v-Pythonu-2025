venecky = [3, 4, 2, 3, 0, 6, 1]
# venecky[1] = 2
print(venecky[1])
print(venecky[0:2])
print(venecky[-2:])
pocet_venecku = sum(venecky)
print(pocet_venecku)
pocet_dni = len(venecky) #pocet hodnot seznamu
print(pocet_dni)
minimum_venecku = min(venecky)
print(minimum_venecku)
maximum_venecku = max(venecky)
print(maximum_venecku)
serazeny = sorted(venecky, reverse=True)
print(serazeny)

###

jmeno = "Markéta "
prijmeni = "Chvaja"
cele_jmeno = jmeno + prijmeni
print(cele_jmeno)
print(cele_jmeno[-3:])
print(cele_jmeno[::-1]) #napíše jméno pozpátku
print(cele_jmeno[::2]) #vypíše každý druhý znak


###

inzerat = "Na této pracovní pozici budete využívat Python a SQL."
# Je řetězec "Python" v řetězci "inzerat"?
if "Python" in inzerat:
  print("Hurá! To je něco pro mě!")
else:
  print("Bůůůů!")


# hledání v inzerátu - citlivost na velká písmena - převod na velké / malé - upper / lower METODY

inzerat = "Na této pracovní pozici budete využívat python a SQL"
inzerat_velkymi = inzerat.upper()
# Je řetězec "Python" v řetězci inzerat?
if "PYTHON" in inzerat_velkymi:
    print("Hurá")
else:
    print("Bůůůů")


# metoda strip - ořezání mezer

retezec = " czechitas "
print(retezec.strip())

# metoda split - rozdělení řetězce na položky seznamu

retezec = "po út st čt pá"
seznam_retezcu = retezec.split()
print(seznam_retezcu)


zavod = "Alena Josef Natálie"
zavod_seznam = zavod.split()
print(zavod[0])
print(zavod_seznam[0])

zavod = "Alena Malá, Josef Novák, Natálie Nižnanská"
zavod_seznam = zavod.split(", ")
print(zavod_seznam[2])

# metoda JOIN - spojování prvků sezanamu do řetězce
zavod_seznam = ["Alena Malá, Josef Novák, Natálie Nižnanská"]
zavod_retezec = ", ".join(zavod_seznam)
print(zavod_retezec)

# podobně lze pěkně vypsat seznam i pomocí cyklu, ale problém je, že cyklus vypíše oddělovač (např. čárku) i za poslední jméno. 

# metoda REPLACE
text = "Kurz vede lektor Martin."
upraveny_text = text.replace("Martin", "Marek")
print(upraveny_text)

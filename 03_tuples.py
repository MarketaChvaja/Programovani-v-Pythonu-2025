venecky = [2, 3, 4, 1, 2, 3, 1]
venecky.append(5)
print(venecky)

###

venecky = [2, 3, 4, 1, 2, 3, 1]
venecky = venecky + [5, 8]
print(venecky)

### Seznam (list)
venecky_seznam = [2, 3, 4, 1, 2, 3, 1]
### N-tice (tuple)
venecky_ntice = 2, 3, 4, 1, 2, 3, 1
### Množina (set)
venecky_konzumenti_mnozina = {"Jirka", "Lucka", "Katka"}


jmena = {"Jirka", "Lucka"}
jmena.add("Simona")
print(jmena)


# Sloučení množin
jmena = {"Jirka", "Lucie"}
jmena_dalsi = {"Jirka", "Simona"}
jmena = jmena | jmena_dalsi
print(jmena)

# převod množiny na seznam
množina = {"A", "B"}
seznam = list(množina)
print(množina)
print(seznam)

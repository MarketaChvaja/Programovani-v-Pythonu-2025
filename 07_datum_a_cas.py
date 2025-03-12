from datetime import datetime, timedelta  # importuji jen vybrané fce modulu, následný zápis je pak jendodušší

print(datetime.now())

# import datetime - importuji ceý modul, pa musím použít tento zápis pro print:
# print(datetime.datetime.now())

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
# čtení na doma: časové zóny
print(apollo_start.weekday()) # vytiskne den týdne, ale počítá je od nuly, tedy 2 je středa
print(apollo_start.isoweekday())   # počítá dny od čísla jedna, takže 3 je středa
print(apollo_start.month)   # píše se bez závorek, je to jako vlastnost

# apollo_pristani = datetime.strptime("21.7. 1969, 18:54", "%d. %m. %Y, %H:%M"). 

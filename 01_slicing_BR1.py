# Cvičení 1: Pohyby na účtu

"""
1 - Vypiš v pořadí třetí pohyb z uvedeného seznamu. 
2 - Vypište všechny pohyby kromě prvních dvou. 
3 - Vypište kolik je všech pohybů dohromady. 
4 - Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb. 
5 - Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
"""

pohyby = [1200, -250, -800, 540, 721, -613, -222]
# 1
print(pohyby[2])
# 2
print(pohyby[2:])
# 3
pocet_pohybu = len(pohyby)
print(pocet_pohybu)

# 4
nejvyssi_pohyb = max(pohyby)
nejnizsi_pohyb = min(pohyby)
print(nejvyssi_pohyb, "nejvyšší pohyb na účtu")
print(nejnizsi_pohyb, "nejnižší pohyb na účtu")
# Co kdybychom brali v potaz zvlášť odchozí a zvláášť příchozí platby (tedy zvlášť záporné a zvlášť kladné hodnoty?
# 5
celkovy_prirustek = sum(pohyby)
print(celkovy_prirustek)

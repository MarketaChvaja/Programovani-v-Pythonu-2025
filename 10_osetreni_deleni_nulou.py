# Vytvoř program, který vypíše výsledek dělení těchto čísel. Program se postupně zeptá na dvě čísla (mohou být celá i desetinná). Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou. V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.

def deleni(number1, number2):
  return number1 / number2

print(deleni(2, 2))

print(deleni(2, 0))

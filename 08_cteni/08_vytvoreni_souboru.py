nazev_souboru = input("Zde napiš požadovaný název souboru: ") # např. "soubor1" nebo "poznamky"

text_souboru = input("Zde napiš, co má být zapsáno v souboru: ") # např. "Ahoj" nebo "aodihDÁBIZHIIW "

with open(f"{nazev_souboru}.txt", "w", encoding="utf-8") as file: 
  print(f"{text_souboru}", file=file)

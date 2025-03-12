def vypis_pozdrav(jazyk):
  if jazyk == "cs":
    print("Ahoj!")
  elif jazyk == "de":
    print("Guten tag!")
  elif jazyk == "ja":
    print("こんにちは")
  else:
    print("Hello!")

vypis_pozdrav("cs")
vypis_pozdrav("en")
vypis_pozdrav("de")
vypis_pozdrav("ja")


def secti_cisla(a, b):
  return a + b

vysledek_1 = secti_cisla(9, 12)
print(vysledek_1)

# prevody mile na kilometry - nepovinne parametry a typovani

def mile_na_kilometry(mile: float, namorni: bool=False) -> float:
    # není námořní - a tím pádem je pozemní
    if not namorni:
        return mile * 1.609344
    # je to námořní
    else:
        return mile * 1.852
london_oxford_km = mile_na_kilometry(59.7, False)
print(london_oxford_km)
belfast_new_york = mile_na_kilometry(2758.13, True)
print(belfast_new_york)

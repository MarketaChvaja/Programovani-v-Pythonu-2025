# Cvičení na funkce: Vytvoř funkce celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.

def celsius_to_farenheit(celsius):
  return (celsius*1.8)+32


print(celsius_to_farenheit(-40), "Očekávaný výsledek: -40 st. Celsia je -40 st. farenheita.")
print(celsius_to_farenheit(0), "Očekávaný výsledek: 0 st. Celsia je 32 st. farenheita.")
print(celsius_to_farenheit(100), "Očekávaný výsledek: 100 st. Celsia je 212 st. farenheita.")


def farenheit_to_celsius(farenheit):
  return (farenheit-32)/1.8

print(farenheit_to_celsius(32), "- má vyjít 0 st. Celsia")
print(farenheit_to_celsius(212), "- má vyjít 100 st. Celsia")
print(farenheit_to_celsius(-40), "- má vyjít -40 st. Celsia")

print(farenheit_to_celsius(451))

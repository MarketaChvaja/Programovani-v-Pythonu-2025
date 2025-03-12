# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# zadani: https://kodim.cz/czechitas/python-oop/lekce/tridy/tridy/balik

class Package:
  def __init__(self, address, weight, state):
    self.address = address
    self.weight = weight
    self.state = state
  def get_info(self):
    return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
  def delivery_price(self):
    if self.weight < 10:
      return "Cena balíku je 129 Kč."
    if self.weight < 20:
      return "Cena balíku je 159 Kč."
    else: 
      return "Cena balíku je 189 Kč."


balik001 = Package("Václavská 12, Brno", 0.5, "doručen")
balik007 = Package("Rustonka, Praha", 25, "nedoručen")

print(balik001.get_info())
print(balik007.get_info())

print(balik001.delivery_price())
print(balik007.delivery_price())

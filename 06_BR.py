# Celková hodnota balíků : https://kodim.cz/czechitas/python-oop/lekce/dedicnost/dalsi-funkce/seznam-baliku 


class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    
    def delivery_price(self):
        if self.weight < 10:
            return 129
        if self.weight < 20:
            return 159
        else:
            return 359


    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    def deliver(self):
        if self.state == "nedoručen":
          self.state = "doručen"
          return f"Balík právě doručujeme."
        else:
            return f"Balík již byl doručen."

balik1 = Package("Dlouhá třída 20", 0.5, "doručen") 
balik2 = Package("Příčná 1", 20, "nedoručen")



print(balik1)
print(balik2)

print(balik1.deliver())
print(balik2.deliver())
print(balik2.deliver())



class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value
    def __str__(self):
        return super().__str__() + f"Balík má cenu {self.value} Kč."
    def delivery_price(self):
        return super().delivery_price() + (0.05 * self.value)
    
balik3 = ValuablePackage("Majovského 12a", 15, "nedoručen", 2000)

print(balik3)

print(balik3.deliver())
print(balik3.deliver())
print(balik3)

print("Cena přepravy je: ", balik3.delivery_price(), "Kč.")


package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "doručen", 5500)
package_list = [package_1, package_2, package_3]

total_value = 0

for item in package_list:
    if item.state == "nedoručen":
      value1 = (getattr(item, "value", 0))
      total_value = total_value + value1

print(total_value)







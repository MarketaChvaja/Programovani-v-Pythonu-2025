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
        return 359

#    def get_info(self):
#        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

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

# print(balik1.get_info())
# print(balik2.get_info())

print(balik1)
print(balik2)

print(balik1.deliver())
print(balik2.deliver())
print(balik2.deliver())




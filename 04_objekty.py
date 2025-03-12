class Employee:
  def __init__(self, name, position, holiday_entitlement):
    self.name = name 
    self.position = position
    self.holiday_entitlement = holiday_entitlement
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."


frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nová", "konstruktérka", 25)

print(frantisek.name)

print(frantisek.get_info())



###

class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."
frantisek = Employee("František Novák", "konstruktér", 25)
klara = Employee("Klára Nová", "konstruktérka", 25)
print(frantisek.get_info())
print(klara.get_info())

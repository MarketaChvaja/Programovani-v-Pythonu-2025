class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
    
    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Škoda Octavia")
print(marian)
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Škoda Octavia")  

print(marian.take_holiday(20))
print(marian)

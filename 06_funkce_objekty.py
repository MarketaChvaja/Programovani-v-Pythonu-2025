
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    
    def get_info(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car
frantisek = Employee("František Novák", "konstruktér", 25)
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia")
marketa = Employee("Markéta Chvaja", "QA", 25)


if isinstance(frantisek, Manager):
    print("Objekt pochází ze třídy manager.")
    print(f"Má auto: {marian.car}.")
else:
    print("Objekt pochází z jiné třídy.")

employee = [frantisek, marian, marketa]
expected = 0
for item in employee:
    if isinstance(item, Manager):
        expected = expected + 1  ## Java: expected++
print(expected)


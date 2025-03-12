# Slovník
item1 = ["Čajová konvička s hrnky", 899, True]
item2 = {"title": "Čajová konvička s hrnky", "price": 899, "in stock": True}
print(item1)
print(item2)
print(item2["title"])
item2["price"] = 939
print(item2["price"])
item2["weight"] = 0.8
print(item2)
print(item2["weight"])

# bezpečné čtení ze slovníku
if "rating" in item2:
  print(item2["rating"])
else:
  print("No rating :-(")

  print(f"Vybraný předmět je {item2["title"]} a cena je {item2["price"]}.")


#

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
print(f"Vybraný předmět je {item["title"]} a cena je {item["price"]}.")
key = "title"
print(item[key])
item[key] = "Čajová konvička se 6 hrnky"
print(item)

# priklad debbugingu

def is_odd(number):
  return number % 2 == 0
# 4 % 2 -> 0
# 5 % 2 -> 1

# funkce is_odd by měla vrátit True pro liché číslo a False pro sudé
# odd = liché, even = sudé

print(is_odd(3)) # vrátí False, ale očekáváme TRUE 
# opravíme funkci nebo její pojmenování....? 

assert is_odd(4) == False

# správná, opravená verze programu:
# def is_odd(number):
#   return number % 2 == 1


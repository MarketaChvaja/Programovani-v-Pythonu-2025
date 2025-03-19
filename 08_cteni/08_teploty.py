temperatures = []
with open("Programovani-v-Pythonu-2025/08_cteni/mereni.txt", encoding="utf-8") as file:
    for line in file:
        day, temperature = line.split("\t")
        temperature = float(temperature)
        temperatures.append(temperature)
print(temperatures)

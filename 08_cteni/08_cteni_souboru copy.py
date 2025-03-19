lines = []

with open("Programovani-v-Pythonu-2025/08_cteni/mereni.txt", encoding="utf-8") as file:
  for line in file:
    line_list = line.split("\t")
    line_list[1] = float(line_list[1])
    lines.append(line_list)
 

print(lines)



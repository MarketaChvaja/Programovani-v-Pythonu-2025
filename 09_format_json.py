import json

with open("Programovani-v-Pythonu-2025/absolventi.json", encoding="utf-8") as file:
  absolvents = json.load(file)

print(absolvents[0])

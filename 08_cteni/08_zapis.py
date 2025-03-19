text = "Tento text bude zapsán do souboru."
with open("text.txt", "a", encoding="utf-8") as file:
  print(text, file=file)

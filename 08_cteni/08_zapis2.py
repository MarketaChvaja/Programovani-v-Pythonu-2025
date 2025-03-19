names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
with open("text2.txt", "w", encoding="utf-8") as file:
    for item in names:
        print(item, file=file)

# https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vyjimky/krokovani
# https://kodim.cz/cms/assets/czechitas/uvod-do-progr-2/uvod-do-programovani-2/vyjimky/krokovani/smeny.txt

# menu - run - start debbuging

with open("smeny.txt", encoding="utf-8") as file:
  for line in file:
    lines.append(line)
avg_sales = []
for line in lines:
    line = line.split(",")
    # 2904,4
    total_sales, hours = line
    avg = int(total_sales) / int(hours)
    avg_sales.append(avg)

print(avg_sales)

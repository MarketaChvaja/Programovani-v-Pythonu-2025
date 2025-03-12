sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} kusů.")
total_sales = sum(sales.values())
print(f"Celkem bylo prodáno {total_sales} knih.")

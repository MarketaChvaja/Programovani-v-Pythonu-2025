from datetime import datetime, timedelta

planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10, seconds=30)
skutecny_prijezd = planovany_prijezd + zpozdeni
print(skutecny_prijezd)

from datetime import datetime, timedelta
# import datetime
# print(datetime.datetime.now())
apollo_start = datetime(1969, 7, 16, 14, 32)
apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
# parse
apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
print(apollo_start)
print(apollo_pristani)
delka_mise = apollo_pristani - apollo_start
print(delka_mise)

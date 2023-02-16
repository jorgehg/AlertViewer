from datetime import datetime

d = "09-02-2023 14:34:47"

c = datetime.strptime(d, '%d-%m-%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
print(c)

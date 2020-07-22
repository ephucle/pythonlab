from datetime import date

d1 = (2014, 7, 2)
d2 = (2014, 7, 11)

#d = datetime.date(2019, 4, 13), mac tinh: nam, thang, ngay
#day1 = date(d1[0], d1[1], d1[2])
#day2 = date(d2[0], d2[1], d2[2])

#betterm phan biet ngay va thang
day1 = date(year = d1[0], month = d1[1], day = d1[2])
day2 = date(year = d2[0], month = d2[1], day = d2[2])

print (d1)
print(day1)
print (d2)
print(day2)
delta = day2-day1
print (delta)

#https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
print (delta.days)
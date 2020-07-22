#https://stackoverflow.com/questions/27417203/decrease-the-days-in-python
from datetime import date
import datetime
today= date.today()
new_date = today - datetime.timedelta(1)

print (today)
print (new_date)
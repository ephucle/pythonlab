#Exercise 7  
#The datetime module provides date and time objects that are similar to the Date and Time objects in this chapter, but they provide a rich set of methods and operators. Read the documentation at http://docs.python.org/2/library/datetime.html.
#
#Use the datetime module to write a program that gets the current date and prints the day of the week.
#Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
#For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.
#For a little more challenge, write the more general version that computes the day when one person is n times older than the other.


from datetime import date
#>>> date.today().strftime("%A")
#'Wednesday'

#Use the datetime module to write a program that gets the current date and prints the day of the week.
#today 

today = date.today()
print(today)
day_name = date.today().strftime("%A")
print(day_name)


#Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.

year = 1986
month = 8
day = 16
birthday = date(year, month, day)
print(type(birthday)) #<class 'datetime.date'>
print(f'My birthday: {birthday}')  #My birthday: 1986-08-16

old = today - birthday  #<class 'datetime.timedelta'>
print(old) #12394 days, 0:00:00
print(type(old))  #<class 'datetime.timedelta'>
print(old.days) #12394
print(f"My year old: {old.days/365.25:.02f}")  #My year old: 33.93

next_birthday = date(2020 , month, day)
print(f'My next birthday: {next_birthday}')  #My next birthday: 2020-08-16

print(f"delta days to next birth day: {(next_birthday - today).days}")


#For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.
#For a little more challenge, write the more general version that computes the day when one person is n times older than the other.

b1 = date(1990,10,3)
b2 = date(1986,8,16)


def double_day(b1, b2):
    """
    b1 = 2b2
    Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day

the_doubleday = double_day(b1,b2)
print(f"The double day is: {the_doubleday}")
#test again
print((the_doubleday - b1).days)
print((the_doubleday - b2).days)

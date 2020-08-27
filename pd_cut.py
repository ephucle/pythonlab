#https://stackoverflow.com/questions/45751390/pandas-how-to-use-pd-cut

import pandas as pd
#test pd.cut
print('''test = pd.DataFrame({'days': [0,31,45, 70, 15]})''')
test = pd.DataFrame({'days': [0,31,45,70,15]})
print('''test['range'] = pd.cut(test.days, [0,30,60,90])''')
test['range'] = pd.cut(test.days, [0,30,60,90])
print(test)
#   days         range
#0     0           NaN
#1    31  (30.0, 60.0]
#2    45  (30.0, 60.0]
#3    70  (60.0, 90.0]
#4    15   (0.0, 30.0]


test['range'] = pd.cut(test.days, [0,30,60], include_lowest=True)
print (test)
#   days           range
#0     0  (-0.001, 30.0]
#1    31    (30.0, 60.0]
#2    45    (30.0, 60.0]
#3    70             NaN
#4    15  (-0.001, 30.0]


#bins represent the intervals: 0-4 is one interval, 5-6 is one interval, and so on The corresponding labels are "poor", "normal", etc
#[0-4] pool, 4-6 normal, 6-10 "excellent"
student = pd.DataFrame({'grade': [0,3,4,6,8, 10, 2, 9]})
bins = [0, 4, 6, 10]
labels = ["poor","normal","excellent"]
student['grade_cat'] = pd.cut(student['grade'], bins=bins, labels=labels, include_lowest=True)
print(student)
#   grade  grade_cat
#0      0       poor
#1      3       poor
#2      4       poor
#3      6     normal
#4      8  excellent
#5     10  excellent
#6      2       poor
#7      9  excellent
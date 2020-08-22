#!/usr/bin/env python
import pandas as pd
import numpy as np
#df = pd.DataFrame({'x1': [0,1, 2, 3,4], 'x2': [ 5,6,7,8,9]})
exam_one = pd.DataFrame({'Student_Name':list("abcde"),
                          'Exam1_Score':[83,69,91,53,76],
				          'home_town' :['hn', 'hn', 'hn', 'hcm', 'hcm']
						})

exam_two = pd.DataFrame({'Student_Name':list("abcde"),
                          'Exam2_Score':[830,690,910,530,760]})
exam_two = exam_two.sort_values(by=['Exam2_Score'])

print('''print(exam_one)''')
print(exam_one)
print('''print(exam_two)''')
print(exam_two)

# apply "Vlookup" in pandas
print(''' exam_scores = exam_one.merge(exam_two, on='Student_Name')''')
exam_scores = exam_one.merge(exam_two, on='Student_Name')
print(exam_scores)

print('''exam_scores = exam_two.merge(exam_one, on='Student_Name')''')
exam_scores = exam_two.merge(exam_one, on='Student_Name')
print(exam_scores)

#https://codereview.stackexchange.com/questions/31286/python-calculator-script
#improve by Hoang Le P
from collections import OrderedDict

class Operation:
    def __init__(self, func):
        self.func = func

    def calc(self):
        print("self.func", self.func)
        x = self._prompt("First number: ")
        y = self._prompt("Second number: ")
        print(self.func(x, y))



    def _prompt(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Make sure to enter a number...")

def get_operation(operations):
    while True:
        #op_name = input("What would you like to do? " + '|'.join(operations.keys()) + '   \n>>>>> ').title()
        op_name = input("What would you like to do? " + '|'.join(operations.keys()) + '   \n>>>>> ')
        try:
            return operations[op_name]
        except KeyError:
            print("That was not an option.")

#operations = OrderedDict([
#    ('multiply', Operation(lambda x, y: x * y)),
#    ('divide',   Operation(lambda x, y: x / y)),
#    ('add',      Operation(lambda x, y: x + y)),
#    ('subtract', Operation(lambda x, y: x - y)),
#    ('*', Operation(lambda x, y: x * y)),
#    ('/',   Operation(lambda x, y: x / y)),
#    ('+',      Operation(lambda x, y: x + y)),
#    ('-', Operation(lambda x, y: x - y)),
#])

#cach nay tuong tu nhu tren, nhung ngan gon hon
import operator
operations = OrderedDict([
#    ('multiply', Operation(operator.mul)),
#    ('divide',   Operation(operator.truediv)),
#    ('add',      Operation(operator.add)),
#    ('subtract', Operation(operator.sub)),
    ('*', Operation(operator.mul)),
    ('/',   Operation(operator.truediv)),
    ('+',      Operation(operator.add)),
    ('-', Operation(operator.sub)),
])

while True:
	get_operation(operations).calc()
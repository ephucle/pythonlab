import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("type(x)",type(x))
print("type(y)",type(y))
print(y["age"])



data = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


#save to file
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


#load back data
with open('data.txt') as json_file:
    data_dict = json.load(json_file)
    print(type(data_dict))
    print(data_dict)  #{'name': 'John', 'age': 30, 'married': True, 'divorced': False, 'children': ['Ann', 'Billy'], 'pets': None, 'cars': [{'model': 'BMW 230', 'mpg': 27.5}, {'model': 'Ford Edge', 'mpg': 24.1}]}
	
print(data_dict['name'])
print(data_dict['age'])

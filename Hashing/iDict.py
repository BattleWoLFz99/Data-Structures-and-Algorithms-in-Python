0.  # return a value for the given key:
    # Use .get() so that it will return None if not find.
    dict = {'Name': 'Zabra', 'Age': 7}
    dict.get('Age')
    dict.get('Education', "Never")

    Output:
    Value : 7
    Value : Never

# so: 数字出现次数+1；若这个数字第一次出现，则之前出现为0，执行完成后默认1
    num_to_cnt_map[number] = num_to_cnt_map.get(number, 0) + 1


# return a given key for the value(Not Recommended):
def method1(dict, search_age):
    for name, age in dict.items():
        if age == search_age:
            return name

# return all value:
dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values()) 

Output:
dict_values([2, 3, 4])

# return key
for key in d.items()

# return key, value
for key, value in d.items():

# I don't see much use:
>>> a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> d_items = a_dict.items()
>>> d_items  # Here d_items is a view of items
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])


1. 
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False


2. 
# Using set() on a sequence eliminates duplicate elements. The use of sorted() in
# combination with set() over a sequence is an idiomatic way to loop over unique
# elements of the sequence in sorted order.

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear


3. 
# Sometimes, when the KeyError is raised, it might become a problem. To overcome
# this Python introduces another dictionary like container known as Defaultdict
# which is present inside the collections module.
# Python program to demonstrate
# defaultdict
  
  
from collections import defaultdict

# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])

Output:

1
2
Not Present

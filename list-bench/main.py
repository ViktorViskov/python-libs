# libs
from typing import List
from datetime import datetime
from Home import Home
import pickle

# load list with obj from bin file
home_list:List[Home] = []

# generate list
for index in range(100000000):
    if index % 1000000 == 0:
        print(index)
    home_list.append(Home())

# 1 test with list comprension
start = datetime.now()
selected_list = [home for home in home_list if home.id >= 1000 and home.id <=1100]
stop = datetime.now()
print("List comprehension result %s" % (stop - start))

start = datetime.now()
selected_item = next((home for home in home_list if home.id >= 1000 and home.id <=1100), None)
stop = datetime.now()
print("List comprehension and next result %s" % (stop - start))

start = datetime.now()
selected_list = []
for home in home_list:
    if home.id >= 1000 and home.id <=1100:
        selected_list.append(home)
        break
stop = datetime.now()
print("Loop with brake %s" % (stop - start))

start = datetime.now()
selected_list = []
for home in home_list:
    if home.id >= 1000 and home.id <=1100:
        selected_list.append(home)
stop = datetime.now()
print("Loop without brake %s" % (stop - start))

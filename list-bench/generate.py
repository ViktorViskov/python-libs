# libs
from typing import List
from Home import Home
import pickle

# generate list with items
home_list:List[Home] = []

# generate list
for index in range(10000000):
    home_list.append(Home())

# show amount items
print(len(home_list))

# write list to file
bin_file = open("list.bin", "wb")
bin_file.write(pickle.dumps(home_list))
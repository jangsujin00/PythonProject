
import pandas as pd

import random
import os
import pandas as pd
import csv

file_list = os.listdir('C:\\Users\\ASIA-17\\Desktop\\돈벼락\\dow\\dow_balance')
# print(type(file_list))

search = '.xlsx'
for i, word in enumerate(file_list):
    if search in word:
        print('>> modify: ' + word)
        file_list[i] = word.strip(search)

print(file_list)
dow_balance = file_list
with open("dow_balance.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(dow_balance)

for i in file_list:


    i.replace('.xlsx', '').strip()
    print(i)

    old_name = "C:\\Users\\ASIA-17\\Desktop\\돈벼락\\dow\\dow_balance\\{}".format(i)
    new_name = "C:\\Users\\ASIA-17\\Desktop\\돈벼락\\dow\\dow_balance\\{}".format(i)

    os.rename(old_name, new_name)
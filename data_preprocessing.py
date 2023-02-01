import os
import numpy as np
import pandas as pd
from IPython import display
import csv
from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl

# file_list = os.listdir('C:\\Users\\ASIA-17\\Desktop\\돈벼락\\dow\\dow_balance')
# # print(type(file_list))
#
# search = '.xlsx'
# for i, word in enumerate(file_list):
#     if search in word:
#         print('>> modify: ' + word)
#         file_list[i] = word.strip(search)
#
# print(file_list)
# dow_balance_list = file_list
#
# for i in dow_balance_list:
#     xlsx = pd.read_excel("./dow_income/{}.xlsx".format(i), engine='openpyxl')
#     xlsx.to_csv("./dow_income_csv/{}.csv".format(i))

list_folder_name = ['dow_balance_csv', 'dow_cashflow_csv', 'dow_income_csv']
list_csv_folder = [os.path.join(os.getcwd(), file_name) for file_name in list_folder_name]
list_p = []
list_path = []

for i in list_csv_folder:
    _, _, file_names = next(os.walk(i))
    for n, j in enumerate(file_names):
        list_path.append(os.path.join(i, j))
        # print(list_path[n])

#모든 csv파일 불러오기
for i in range(len(list_path)):
    # print(list_path[i])
    csv_data = pd.read_csv(list_path[i], header=0, index_col=0)
    # print(csv_data.isnull().sum())
    df = pd.DataFrame(csv_data)
    csv_data.fillna(0)
    print(csv_data.info())
    # csv_data.transpose()
    # print(csv_data)
    # exit()
    # csv_data.to_csv(list_path[i], mode='w', index=True)


import os
import csv
import pandas as pd
file_list = os.listdir('C:\\Users\\ASIA-17\\Desktop\\돈벼락\\dow\\dow_balance')
#csv파일 저장 후에 excel파일로 변경
dow_balance = []
for file in file_list:
    dow_balance.append(file)
    if file.count('.') == 1:
        name = file.split('.')[0]
        dow_balance.append(name)
    else:
        for k in range(len(file)-1, 0, -1):
            if file[k] == '.':
                dow_balance.append(file[:k])
                break
with open("dow_balance.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(dow_balance)
# # stock_nasdaq
# df_other_cashflow = pd.read_excel('other_cashflow.xlsx')
# df_other_balance = pd.read_excel('other_balance.xlsx')
# df_other_income = pd.read_excel('other_income.xlsx')
# # #cashflow와 balance 데이터비교
# df_other_cashflow_balance_added = set(df_other_cashflow['stock_other']) - set(df_other_balance['stock_other'])
# df_other_cashflow_balance_dropped = set(df_other_balance['stock_other']) - set(df_other_cashflow['stock_other'])
# print('cashflow_balance_추가된_데이터: ', df_other_cashflow_balance_added)
# print('cashflow_balance_삭제된_데이터: ', df_other_cashflow_balance_dropped)
# # cashflow와 income 데이터비교
# df_other_cashflow_income_added = set(df_other_cashflow['stock_other']) - set(df_other_income['stock_other'])
# df_other_cashflow_income_dropped = set(df_other_income['stock_other']) - set(df_other_cashflow['stock_other'])
# print('cashflow_income_추가된_데이터: ', df_other_cashflow_income_added)
# print('cashflow_income_삭제된_데이터: ', df_other_cashflow_income_dropped)
# # balance와 income 데이터비교
# df_other_balance_income_added = set(df_other_balance['stock_other']) - set(df_other_income['stock_other'])
# df_other_balance_income_dropped = set(df_other_income['stock_other']) - set(df_other_balance['stock_other'])
# print('balance_income_추가된_데이터: ', df_other_balance_income_added)
# print('balance_income_삭제된_데이터: ', df_other_balance_income_dropped)
# with open("df_other_balance_income_added.csv", 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(df_other_balance_income_added)
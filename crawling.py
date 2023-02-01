from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
import random
import os
import pandas as pd
import csv

other_cashflow_5003_5484 = pd.read_csv('other_list.csv')

success_other_cashflow_5003_5484 = []
failure_other_cashflow_5003_5484 = []

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('./chromedriver.exe', options=options)
options.add_argument('lang=ko_KR')

Export_to_Excel = '//*[@id="root"]/div/div/section/div/div[2]/div[1]/section[4]/div/div[1]/div[2]/a'

try:

    url = 'https://stockrow.com/AAPL/financials/cashflow/quarterly'
    t_list = [1, 2, 3, 4, 5, 6]
    # a = random.choice(4)
    driver.get(url)
    time.sleep(6)

    #작대기 3개 버튼
    t_list = [1, 2, 3, 4, 5, 6]
    t = random.choice(t_list)
    time.sleep(t)
    driver.find_element('xpath', '//*[@id="root"]/div/div/section/div/div[2]/div[1]/div[1]/div[2]/div/img').click()
    # 로그인

    #signin 버튼 클릭
    driver.find_element('xpath', '//*[@id="root"]/div/div/section/div/div[1]/div/ul[2]/li[2]/a').click()
    t_list = [1, 2, 3, 4, 5, 6]
    t = random.choice(t_list)
    time.sleep(6)

    # 아이디, 비번 입력
    driver.find_element('name', 'user[email]').send_keys('ban090422@gmail.com')
    driver.find_element('name', 'user[password]').send_keys('dl9898als!@#~')
    time.sleep(5)
    # 로그인 버튼 클릭
    driver.find_element('xpath', '//*[@id="new_user"]/div[4]/input').click()
    time.sleep(5)

    for i in other_cashflow_5003_5484['stock_other'][5003:5485]:

        try:

            # 인컴 접속
            url = 'https://stockrow.com/{}/financials/cashflow/quarterly'.format(i)
            t_list = [1, 2, 3, 4, 5, 6]
            a = random.choice(t_list)

            driver.get(url)
            time.sleep(10)





            try:
                #엑셀다운로드 버튼
                driver.find_element('xpath',
                                    '//*[@id="root"]/div/div/section/div/div[2]/div[1]/section[4]/div/div[1]/div[2]/a').click()
                time.sleep(6)
                success_other_cashflow_5003_5484.append(i)
                print(i, "다운로드 성공")
                try:

                    old_name = "C:\\Users\\ASIA-04\\Desktop\\other\\financials.xlsx"
                    new_name = "C:\\Users\\ASIA-04\\Desktop\\other\\{}.xlsx".format(i)
                    time.sleep(6)
                    os.rename(old_name, new_name)
                    print(i, "이름 변경 성공")
                except:
                    failure_other_cashflow_5003_5484.append(i)
                    print(i, "이름 변경 실패")
                # driver.close()

            except:
                failure_other_cashflow_5003_5484.append(i)
                # driver.close()
                print(i, "다운로드 실패")

        except:
            print(i, "cashflow 진입 실패")
            failure_other_cashflow_5003_5484.append(i)



except:
    print(i, "로그인 실패")


with open("success_other_cashflow_5003_5484.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(success_other_cashflow_5003_5484)

with open("failure_other_cashflow_5003_5484.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(failure_other_cashflow_5003_5484)

driver.close()
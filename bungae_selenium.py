from unicodedata import name
from selenium import webdriver
import chromedriver_autoinstaller
import time
import csv

with open('iphone.csv', 'w') as file:
    file.write("title; price; sell_time; locate \n")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]  #크롬드라이버 버전 확인

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')   
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')

driver.implicitly_wait(10)

print("원하시는 상품을 입력해주세요 : ")
def article_scraping(a):
    url = f'https://m.bunjang.co.kr/search/products?q={a}&order=score&page='
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')   
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver')
    for i in range(1, 100):
        driver.get(url + str(i))
        time.sleep(0.1)
        name = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[4]/div/div/a/div[2]/div[1]')
        salary = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[4]/div/div/a/div[2]/div[2]/div[1]')
        sell_time = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[4]/div/div/a/div[2]/div[2]/div[2]')
        locate = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[4]/div/div/a/div[3]')
        with open('iphone.csv', 'a') as file:
            for i in range(len(name)):
                file.write(name[i].text + ';' + salary[i].text + ';' + sell_time[i].text + ';' + locate[i].text + '\n')
            
                
    driver.quit()

article_name = input()
article_scraping(article_name)
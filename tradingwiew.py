from time import sleep
import selenium
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
driver_path="chromedriver.exe"
driver = webdriver.Chrome(driver_path)
chromeOptions.add_argument("-- incognito")
chromeOptions.add_argument("-- headless")

driver.get("https://tr.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT")
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

while True:
    timee = datetime.datetime.now()
    fiyat_bilgi = driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[4]/span[1]/span[1]").text
    print(timee.time()," : ",fiyat_bilgi)
    sleep(30)


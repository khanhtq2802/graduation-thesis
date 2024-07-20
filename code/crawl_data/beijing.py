import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
import csv

options = uc.ChromeOptions()

driver = uc.Chrome(headless=False, use_subprocess=False, options=options)
driver.get("https://www.tripadvisor.com/Attraction_Review-g294212-d319086-Reviews-Forbidden_City_The_Palace_Museum-Beijing.html")

for i in range(0, 8893, 10):
    random_float = random.uniform(10, 10)
    time.sleep(random_float)

    elements = driver.find_elements(by='css selector', value='.JguWG .yCeTE')
    
    with open('beijing.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csv_writer.writerow(['Text'])

        for element in elements:
            csv_writer.writerow([element.text])
    
    with open("count.txt", "a") as file:
        file.write(str(i) + "\n")

    driver.find_element(By.CSS_SELECTOR, '#tab-data-qa-reviews-0 > div > div.LbPSX > div > div:nth-child(11) > div:nth-child(2) > div > div.OvVFl.j > div.xkSty > div > a').click()
    
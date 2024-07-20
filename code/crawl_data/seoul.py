import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
import csv

options = uc.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
driver = uc.Chrome(headless=False, use_subprocess=False, options=options)
driver.get("https://www.tripadvisor.com/Attraction_Review-g294197-d320359-Reviews-Changdeokgung_Palace-Seoul.html")
for i in range(0, 2686, 10):
    random_float = random.uniform(3, 4)
    time.sleep(random_float)

    elements = driver.find_elements(by='css selector', value='.JguWG .yCeTE')
    
    with open('seoul.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csv_writer.writerow(['Text'])

        for element in elements:
            csv_writer.writerow([element.text])
    
    with open("count.txt", "a") as file:
        file.write(str(i) + "\n")

    driver.find_element(By.CSS_SELECTOR, '#tab-data-qa-reviews-0 > div > div.LbPSX > div > div:nth-child(11) > div:nth-child(2) > div > div.OvVFl.j > div.xkSty > div > a').click()
    
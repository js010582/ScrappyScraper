from pandas import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
# PATH = "/home/js010582/Downloads/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome("/home/js010582/Downloads/chromedriver_linux64/chromedriver")
driver.get("https://www.bestbuy.com")

#print page source code
#print(driver.page_source)

search = driver.find_element(By.ID, "gh-search-input")
search.send_keys("rtx 3080")
search.send_keys(Keys.RETURN)

sleep(10)

main = driver.find_element(By.ID, "main")
print(main.text)




# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main-results"))
#     )
#     articles = main.find_elements(By.CLASS_NAME"sku-item abt2822-has-sfl")
#     # products = main.find_(By.CLASS_NAME, "sku-item abt2822-has-sfl")
#     # print(products)
#     for article in articles:
#         header = article.find_elements(By.CLASS_NAME, "sku-item abt2822-has-sfl")
#         print(header.text)

# except:
#     driver.quit()




# products = driver.find_element_by_id("main-results")
# sku-item abt2822-has-sfl
driver.quit()



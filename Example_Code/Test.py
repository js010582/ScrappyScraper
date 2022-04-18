from selenium import webdriver

PATH = "/home/js010582/Downloads/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
print(driver.title)
driver.close() #tab if it's only tab
driver.quit() #closes browser
from selenium import webdriver
import time

path ="chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/index.html")

driver.find_element_by_css_selector("a[name='signup']").click()
time.sleep(2)
driver.back()
time.sleep(2)


driver.find_element_by_css_selector("a[class='btn btn-default btn-lg']").click()
time.sleep(3)

driver.close()
driver.quit()


import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
driver.get("http://members.directconnect.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//div/div/div/div/div[@class="btn-sec text-center"]/a[2]')
driver.find_element_by_xpath('//div/div/div/div/div/div/div/form/div/input[@class="form-control form-control-lg"]').send_keys("1wayitsolutionlivetesting@yopmail.com")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_class_name("btn btn-primary").click()

time.sleep(3)
driver.find_element_by_xpath('//div[@id="wrapper"]/div/div[2]/div/div/div/table/tbody/tr/td[3]/a').click()
print()

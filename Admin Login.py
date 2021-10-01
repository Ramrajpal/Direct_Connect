import time
from selenium import webdriver


driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
driver.maximize_window()
driver.get("http://business.directconnect.com/ctwdr_dmlogin")
driver.implicitly_wait(5)

driver.find_element_by_name("email").send_keys("directconnect@gmail.com")
driver.find_element_by_name("password").send_keys("direct@#devpass")
driver.find_element_by_xpath("/html/body/section[2]/div[2]/form[1]/div[3]/button").click()

time.sleep(10)

driver.find_element_by_xpath("//aside/ul/li[4]").click()
driver.find_element_by_xpath("//main/div[2]/div/input[@type = 'text']").send_keys("Oneway")
time.sleep(2)
print(driver.current_window_handle)
driver.find_element_by_xpath("//main/div[2]/div[5]/div/div[2]/table/tbody/tr[2]/td[9]/a[4]/span/i").click()

al = driver.switch_to.
al.accept()
message = al.text
print(message)



# cw = driver.current_window_handle[2]
# driver.switch_to.window(2)
# print(cw)






# try:
#     alrt = driver.switch_to.alert
#     alrt.accept()
# except Exception:
#     print("No Alert Found")
#
# message = alrt.text
# print("Login pop showing following message: "+ message)
# driver.find_element_by_xpath("//div[@id = 'customerLogin']/div")
# alrt.accept()








import time
from fpdf import FPDF

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/Drive_Chat/Chrome/chromedriver.exe")

driver.maximize_window()
driver.get("http://business.directconnect.com/ctwdr_dmlogin")
time.sleep(5)
driver.find_element_by_xpath("//section[@class='login-content']/div[@class = 'login-box']/form/div[@class ='form-group']/input[@name='email']").send_keys("directconnect@gmail.com")
driver.find_element_by_xpath("//section[@class='login-content']/div[@class = 'login-box']/form/div[@class ='form-group']/input[@name='password']").send_keys("direct@#devpass")
driver.find_element_by_xpath("//section[@class='login-content']/div[@class = 'login-box']/form/div[@class ='form-group btn-container']/button").click()
time.sleep(10)
module_name = driver.find_element_by_xpath("//main/div/div/h1")
txt = module_name.text
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt=txt)
pdf.output("login_status.pdf")
driver.close()
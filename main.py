import time
from fpdf import FPDF
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping

driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/pythonProject/Chrome/chromedriver.exe")
driver.maximize_window()
driver.get("http://members.directconnect.com/ctwdr_dmlogin")
driver.implicitly_wait(5)

driver.find_element_by_name("email").send_keys("directconnect@gmail.com")
driver.find_element_by_name("password").send_keys("direct@#devpass")
submit = driver.find_element_by_xpath("/html/body/section[2]/div[2]/form[1]/div[3]/button")
submit.click()
time.sleep(10)
pdf = FPDF()
for i in range(1, 12):
    driver.find_element_by_xpath("//aside/ul/li[ "+str(i)+"]/a").click()
    time.sleep(5)
    module_name = driver.find_element_by_xpath('//main/div/div/h1')
    txt = module_name.text
    print(txt)

    driver.save_screenshot(r'C:\Users\Tester\PycharmProjects\pythonProject\Screenshots\image'+txt+'.png')

    pdf.add_page(str(i))
    pdf.set_font("Arial", size=13)
    pdf.cell(200,10, txt=txt, ln=1, align='C')
    pdf.image('image'+txt+'.png')
    print()



pdf.output("Module_names.pdf")




"""for i in range(1,10):
    time.sleep(1)
print(driver.title)
try:
    assert title in driver.title
    print("Title matched")
except Exception:
    print("Title not matched")

print("Login Successful")
driver.close()"""


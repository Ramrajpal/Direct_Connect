import smtplib
import time
from email.message import EmailMessage

import pyperclip
from fpdf import FPDF
import pyperclip as pc

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Tester/PycharmProjects/Drive_Chat/Chrome/chromedriver.exe")

driver.maximize_window()
driver.get("http://business.directconnect.com")
time.sleep(2)
driver.find_element_by_xpath("//div/div/div/div/div[@class='btn-sec text-center']/a[@class='btn btn-cutsomer btn-primary']").click()
time.sleep(2)
driver.find_element_by_name("email").send_keys("benn@yopmail.com")
driver.find_element_by_name("password").send_keys("Benn@123")
driver.find_element_by_xpath("//div[@class='register-main-sec cstm-fixed home-login']/div/div[@class='row']/div/div/div/div/form/div[@class='form-group']/button").click()
time.sleep(10)
driver.find_element_by_xpath("//div/div[@id='wrapper']/div/div[2]/div/div/div/table/tbody/tr/td/a[@data-original-title='Login to Art Industry Limited']/i").click()

time.sleep(3)
try:
    driver.find_element_by_xpath("//div[@class='main_wrapper']/div/ul/li[@class='nav-item']/a/span[@class='nav-link-text campaigns_icon']").click()
except Exception :
    print("Element not clicked")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//div[@class='main_wrapper']/div/ul/li[@class='nav-item']/a/span[@class='nav-link-text campaigns_icon']").click()
time.sleep(3)
driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div[@class='container-fluid']/div/div/a[@class='btn btn-primary create-latest-campaign take-tour-campaign']").click()

try:
    driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row step-one-spacing']/div/div/input").send_keys("Automation Email Test Campaign")
    print("Campaign name available")
except Exception as camp_name:
    driver.find_element_by_xpath(
        "//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row step-one-spacing']/div/div/input").send_keys(
        "New Automation Email Test Campaign ")
    print("campaign name not available", camp_name)
driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@id='accordioncamp']/div/div[@id='headingTwo']/h6/input").click()

driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row create-campaign-button']/button").click()
time.sleep(10)

#to get campaign email id

driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div/div/form/div[@class='top_main_camp_div']/div[2]/div/div/div/table/tbody/tr[2]/td[3]/a[@class='azure-copy']").click()
# if len(ele) > 0:
#     ele[0].click()

campaign_Email_id = pyperclip.paste()
print("campaign_Email_id is "+campaign_Email_id)
#send email to campaign
gmail_id = "ram1wayit@gmail.com"
gmail_password = "Crochet@78600"

sent_from = gmail_id
to = campaign_Email_id

#setup gmail server

try:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    msg=EmailMessage()
    server.login(gmail_id, gmail_password)
    msg['From']=gmail_id
    msg['Subject']='Test Subject'
    msg['To']=campaign_Email_id
    msg.set_content("Name: Text automation \n Email: Test@yopmail.com \n Phone: 123456789 \n Message: This is a test message from automated campaign")
    server.send_message(msg)
    print("Email sent Successful")
    server.quit()
except Exception as ex:
    print("Something went wrong, Email not send", ex)

driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div/div/form/div[@class='tab-content campTabs cmpny-contact-tab-sec']/div[@class='tab-pane active']/div[@class='row confirm-notice']/div/input").click()
driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div[@class='tabbable-panel Campaigns-tabs']/div/form/div[@class='tab-content campTabs cmpny-contact-tab-sec']/div[@class='tab-pane active']/div[@class='row next-step-button']/div/div/a").click()
driver.refresh()
#time.sleep(20)

# if:
#     driver
# else:
#     driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div/div/form/div[@class='tab-content campTabs cmpny-contact-tab-sec']/div[@class='tab-pane active']/div[@class='row add-tags-here']/div/div/div/div/div/div/div/span/a").click()
#     driver.refresh()

# txt = module_name.text
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=14)
# pdf.cell(200, 10, txt=txt)
# pdf.output("login_status.pdf")
# driver.close()
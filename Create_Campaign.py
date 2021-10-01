import smtplib
import time
from fpdf import FPDF

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


driver.find_element_by_xpath("//div[@class='main_wrapper']/div/ul/li[@class='nav-item']/a/span[@class='nav-link-text campaigns_icon']").click()

driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div[@class='container-fluid']/div/div/a[@class='btn btn-primary create-latest-campaign take-tour-campaign']").click()
campaign = "one"
try:
    driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row step-one-spacing']/div/div/input").send_keys("Automation Email Test Campaign ")
    print("Campaign name available")
except Exception as camp_name:
    driver.find_element_by_xpath(
        "//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row step-one-spacing']/div/div/input").send_keys(
        "New Automation Email Test Campaign ")
    print("campaign name not available", camp_name)
driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row step-one-spacing']/div/div/input").click()

driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/form/div[@class='row create-campaign-button']/button").click()
time.sleep(5)

#to get campaign email id

campaign_Email_id = driver.find_element_by_xpath("//div[@class='main_wrapper']/div[@id='wrapper']/div/div/form/div[@class='top_main_camp_div']/div[@class='row table-created-campaign nopad']/div/div/div/table/tbody/tr[2]/td[3]/a[@class='azure-copy']/img".)

#send email to campaign
gmail_id = "ram1wayit@gmail.com"
gmail_password = "Crochet@786"

sent_from = gmail_id
to = campaign_Email_id
subject = campaign_Email_id
body = "Name: Text automation /n Email: Test@yopmail.com /n Phone: 123456789 /n Message: This is a test message from automated campaign"

#setup gmail server
try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(gmail_id,gmail_password)
    smtp_server.sendmail(sent_from, to, subject,body)
    smtp_server.close()
    print("Email sent Successful")
except Exception as ex:
    print("Something went wrong, Email not send", ex)



# txt = module_name.text
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=14)
# pdf.cell(200, 10, txt=txt)
# pdf.output("login_status.pdf")
# driver.close()
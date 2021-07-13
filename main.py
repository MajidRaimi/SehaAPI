from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Developer\Python\Web\chromedriver.exe"

bot = webdriver.Chrome(PATH)

username = input("Please Enter Your Username : ")
password = input("Please Enter Your Password : ")

bot.get("https://www.seha.sa/Service/Index/31")


bot.find_element_by_id("UserName").send_keys(username)
bot.find_element_by_id("Password").send_keys(password)


bot.find_element_by_id("LoginButton").click()

code = input("Please Enter The Code : ")

bot.find_element_by_id("VerificationCode").send_keys(code)

bot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[4]/div[2]/button[1]").click()

bot.find_element_by_link_text('سجل التطعيمات').click()
from selenium import webdriver
import time

PATH = "C:\Developer\Python\Web\geckodriver.exe"



username = input("Please Enter Your Username : ")
password = input("Please Enter Your Password : ")


bot = webdriver.Edge(executable_path=r'C:\Developer\Python\Web\msedgedriver.exe')
bot.minimize_window()
bot.get("https://www.seha.sa/Service/Index/31")

bot.find_element_by_id("UserName").send_keys(username)
bot.find_element_by_id("Password").send_keys(password)

bot.find_element_by_id("LoginButton").click()

code = input("Please Enter The Code : ")

bot.find_element_by_id("VerificationCode").send_keys(code)

bot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[4]/div[2]/button[1]").click()

time.sleep(5)
bot.find_element_by_xpath('//*[@id="li_menu_item_7"]/a/span').click()

time.sleep(3)

bot.find_element_by_xpath('//*[@id="li_menu_Child_31"]/a').click()

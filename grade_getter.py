from selenium import webdriver
import time

subject = input("Choose the subject: ")

chrome_path = r"/Users/vladrusu/Desktop/chromedriver"
driver = webdriver.Chrome(chrome_path)

driver.get("https://vampires.managebac.com/student")

def login():
	username = driver.find_element_by_id("session_login")
	username.clear()
	username.send_keys("EMAIL") # replace EMAIL with your actual managebac acount email

	password = driver.find_element_by_id("session_password")
	password.clear()
	password.send_keys("PASSWORD") # replace PASSWORD with your actual managebac password
	driver.find_element_by_name("commit").click()



def nav_to_class(xpath):
	driver.find_element_by_xpath("""//*[@id="menu"]/ul/li[7]/a/span""").click() #press classes button
	time.sleep(1)
	driver.find_element_by_xpath(xpath).click() #press actual class button from menu
	time.sleep(1)					
	driver.find_element_by_id("menu-trigger")
	time.sleep(1)
	driver.find_element_by_xpath("""//*[@id="action-show"]/main/div[2]/div/div[1]/ul/li[2]/a""").click() #press tasks and unit button in from class overview
	time.sleep(1)
	driver.find_element_by_id("menu-trigger")
	time.sleep(1)
	driver.find_element_by_xpath("""//*[@id="action-index"]/main/div[2]/div/h3/a""").click() #press show tasks from tasks and units

def main():
	classesXpath = {
		'English': """//*[@id="menu"]/ul/li[7]/ul/li[1]/a/span""",
		'Romanian': """//*[@id="menu"]/ul/li[7]/ul/li[2]/a/span""",
		'Humanities': """//*[@id="menu"]/ul/li[7]/ul/li[3]/a/span""",
		'Science': """//*[@id="menu"]/ul/li[7]/ul/li[4]/a/span""",
		'Math': """//*[@id="menu"]/ul/li[7]/ul/li[5]/a/span""",
		'Film': """//*[@id="menu"]/ul/li[7]/ul/li[6]/a/span""",
		'PE': """//*[@id="menu"]/ul/li[7]/ul/li[7]/a/span""",
		'Journalism': """//*[@id="menu"]/ul/li[7]/ul/li[8]/a/span"""
	}
	login()
	nav_to_class(classesXpath[str(subject)])

main()
									

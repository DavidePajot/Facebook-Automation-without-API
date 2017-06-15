from selenium import webdriver
from selenium.webdriver.common.keys import Keys
email = ('myemail@gmail.com')
password = ('mypassword123')
page = 0
friends_id = open("C:\\Users\\Davide Pajot\\Desktop\\friends.txt","a")
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(30)
driver.get("https://mbasic.facebook.com")
driver.implicitly_wait(20)

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_name("login").click()

try:
	while True:
		driver.get(f"https://mbasic.facebook.com/friends/center/friends/?ppk={page}")
		page += 1
		for friend in driver.find_elements_by_class_name("bm"):
			friends_id.write(friend.get_attribute('href')[58:friend.get_attribute('href').find("&")] + "\n")
except AttributeError:
	friends_id.close()

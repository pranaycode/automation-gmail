from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Chrome(executable_path='#chromedriver in your computer')
driver.implicitly_wait(10)
driver.maximize_window()
user="#email id"
pwd="#password"
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys(user)
driver.find_element_by_xpath("//*[@id='identifierNext']/span").click()
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(pwd)
driver.find_element_by_xpath("//*[@id='passwordNext']/span").click()
import config
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

driver = webdriver.Chrome(executable_path='C:\\Users\\jakel\\OneDrive\\Desktop\\Lamers-McKean\\chromedriver',chrome_options=chrome_options)

config = ConfigParser()
config.read('config.ini')

def LoginMethod(driver,config):
    driver.get(config['config']['WEBSITE_URL'])

    user_name = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    user_name.send_keys(config['config']['username'])
    password.send_keys(config['config']['password'])

    driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/footer[1]/div[1]/button[1]').click()

LoginMethod(driver,config)

print('Done')

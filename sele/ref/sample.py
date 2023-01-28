import os

from dotenv import load_dotenv

# selenium 4
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

"""
"""

# Load Environment Varibles
load_dotenv('.env')

U = os.environ.get("USERNAME")
P = os.environ.get("PASSWORD")

URL = "https://www.google.com/"

# XPath Variables
USERNAME_XPATH = '//*[@id="associate-login-input"]'
UNAME_XPATH = '//*[@id="login"]'
PASSWORD_XPATH = '//*[@id="password"]'


# Setup Selenium
service = ChromeService(ChromeDriverManager().install())

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True) # Keep Open

driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

# Use Driver
driver.get(URL)
driver.implicitly_wait(1)

#! First Username Check
init_uname = driver.find_element(by=By.XPATH, value=USERNAME_XPATH)
init_uname.send_keys(U)

init_uname.send_keys(Keys.ENTER)

#! Login Page
driver.implicitly_wait(1.2)

# p = driver.find_element(by=By.XPATH, value=PASSWORD_XPATH)

# p.send_keys(P)
# p.send_keys(Keys.ENTER)


#! 2 Factor Auth





import os

from dotenv import load_dotenv

# Utility Imports
from utils.file_save import save_json
from utils.url_builder import build_indeed_url

# selenium 4
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

"""
Date: 01/26/23
Program: Selenium v4 job scraper
Description: Scrape data from job listings on indeed.com using Selenium(Version 4)
"""

# Load Environment Varibles
load_dotenv('settings.env')

#! Get Search Params
QUERY = os.environ.get("QUERY")
LOCATION = os.environ.get("LOCATION")
RADIUS = os.environ.get("RADIUS")

#! Build URl and Filepath
URL = build_indeed_url(QUERY, LOCATION, RADIUS)

FILEPATH = f"data/{QUERY.replace(' ', '_')}_{LOCATION}.json"

# Selector Variables
JOB_TITLE_SELECTOR = 'jobTitle'
COMPANY_NAME_SELECTOR = 'companyName'
COMPANY_LOCATION_SELECTOR = 'companyLocation'
SALARY_SELECTOR = 'salaryOnly'


#! Setup Selenium Driver
service = ChromeService(ChromeDriverManager().install())

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
# options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True) # Keep Open

driver = webdriver.Chrome(service=service, options=options)


#! Use Driver
driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(3) # wait for load

#! Get Job Titles
job_titles = driver.find_elements(by=By.CLASS_NAME, value=JOB_TITLE_SELECTOR)

#! Get Company Name
company_names = driver.find_elements(by=By.CLASS_NAME, value=COMPANY_NAME_SELECTOR)

#! Get Company Location
company_locations = driver.find_elements(by=By.CLASS_NAME, value=COMPANY_LOCATION_SELECTOR)

#! Get Salary
salaries = driver.find_elements(by=By.CLASS_NAME, value=SALARY_SELECTOR)

#! Get Links
job_links = driver.find_elements(by=By.CLASS_NAME, value=f"{JOB_TITLE_SELECTOR} > a")


#! Group/Parse Data
jobs = []
for idx in range(len(job_titles)):
    print(idx)
    job = {
            'title': job_titles[idx].text,
            'link': job_links[idx].get_attribute('href'),
            'company': company_names[idx].text if idx < len(company_names) else None,
            'location': company_locations[idx].text if idx < len(company_locations) else None,
            'salary': salaries[idx].text if idx < len(salaries) else None
        }
    jobs.append(job)

#! Save Data
save_json(FILEPATH, jobs)


#! Quit Driver
driver.implicitly_wait(1)
driver.quit()


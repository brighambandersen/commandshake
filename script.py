import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--query", type=str, help="Job search query", required=True)
args = parser.parse_args()

# Convert spaces to '%20's for url
raw_job_query = args.query
job_query = raw_job_query.replace(" ", "%20")

# Grab up env vars
BYU_USERNAME = os.environ.get("BYU_USERNAME")
BYU_PASSWORD = os.environ.get("BYU_PASSWORD")

# start up web driver
driver = webdriver.Chrome()

# Go to search url (it will first redirect for auth)
driver.get(
    f"https://byu.joinhandshake.com/postings?page=1&per_page=1000&sort_direction=desc&sort_column=default&query={job_query}"
)

# Handle login

# Redirect to CAS BYU Login
byu_login_btn = driver.find_element(By.CLASS_NAME, "sso-button")
byu_login_btn.click()

# Fill in username, password, then sign in to BYU account

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(BYU_USERNAME)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(BYU_PASSWORD)

password_input.send_keys(Keys.ENTER)  # Press enter to submit login

# Give time to do DUO two-factor auth and redirect to postings page
sleep(30)

num_applies = 0  # Keeps track of how many times you applied successfully

# Once redirected back to search, then grab all postings
# postings = driver.find_elements(By.xpath("//a[@data-hook='jobs-card']"))
# postings = driver.find_element(By.cssSelector("a[data-hook='jobs-card']"))

# postings = driver.find_elements(
#     By.XPATH, "//body[contains(@class, 'style__card-content')]"
# )
# print(postings)
# print(len(postings))
########


# For each posting

# Click on sidebar posting

# Check if there's a 'Quick Apply' button

# If yes
# Click 'Quick Apply' Button

# Maybe check here that there's only 1 step
# Click resume button
# Click 'Submit' Button


quick_posting = driver.find_element(By.XPATH, '//*[@id="posting-278714558"]/div')
quick_posting.click()
quick_posting_apply_btn = driver.find_element(
    By.CLASS_NAME,
    "apply-button",
)
quick_posting_apply_btn.click()
quick_posting_add_resume_btn = driver.find_element(
    By.XPATH,
    "/html/body/reach-portal/div[3]/div/div/div/span/form/div[1]/div/div[2]/fieldset/div/div[2]/span[1]/button",
)
quick_posting_add_resume_btn.click()
quick_posting_submit_btn = driver.find_element(
    By.XPATH,
    "/html/body/reach-portal/div[3]/div/div/div/span/form/div[2]/div/span/div/button",
)
quick_posting_submit_btn.click()


print("Successfully applied to", num_applies, raw_job_query, "jobs!")
APP_RESULTS_URL = "https://byu.joinhandshake.com/applications?ref=account-dropdown"
print(f"Visit {APP_RESULTS_URL} for details on where you applied.")

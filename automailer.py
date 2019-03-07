# Program to login in to a gmail account and send an email
# sys.argv = 1. username 2. password 3. receiving email 4. subject 5. message
# gmail dynamically changes css selectors for send_to, subject, message, send,
# so doesn't always work unless you grab the css selectors first

import sys
import time
import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Opening email login page.....')

url = 'https://mail.google.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
driver = webdriver.Firefox(executable_path=r'c:\Users\bills\Desktop\ATBS\geckodriver.exe')
driver.get(url)
res = requests.get(url, headers=headers)
res.raise_for_status()

# Login
soup = bs4.BeautifulSoup(res.text, 'html.parser')
sign_in = soup.select('.header__nav--ltr > li:nth-child(2) > a:nth-child(1)')
print('Entering username.....')
time.sleep(2)
login = driver.find_element_by_css_selector('#identifierId')
login.send_keys(sys.argv[1] + Keys.ENTER)
print('Entering password.....')
time.sleep(2)
password = driver.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)')
password.send_keys(sys.argv[2] + Keys.ENTER)

# Compose and send
time.sleep(10)
compose = driver.find_element_by_css_selector('.T-I-KE')
compose.click()
print('Composing email to ' + sys.argv[3] + '.....')
time.sleep(2)
send_to = driver.find_element_by_css_selector('#\\:8x')
send_to.send_keys(sys.argv[3])
subject = driver.find_element_by_css_selector('#\\:8f')
subject.send_keys(sys.argv[4])
message = driver.find_element_by_css_selector('#\\:9k')
message.send_keys(sys.argv[5])
send = driver.find_element_by_css_selector('#\\:85')
send.click()

print('Mail sent successfully to ' + sys.argv[3] + '.....')

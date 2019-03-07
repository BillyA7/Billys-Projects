from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import random

print('Welcome to the 2048 game simulator!')
time.sleep(1)

num_of_games = int(input('Please enter how many games you would like the program to simulate:\n'))

print('Please wait, loading game now.......')

url = 'https://gabrielecirulli.github.io/2048/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}
driver = webdriver.Firefox(executable_path=r'c:\Users\bills\Desktop\ATBS\geckodriver.exe')
driver.get(url)
res = requests.get(url, headers=headers)
res.raise_for_status()

play = driver.find_element_by_css_selector('body')
retry = driver.find_element_by_class_name('retry-button')
score = driver.find_element_by_class_name('score-container')
best_score = driver.find_element_by_class_name('best-container')

keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
games = 0
moves = 0
while games < num_of_games:
    if retry.is_displayed() is False:
        play.send_keys(random.choice(keys))
        moves += 1
    else:
        games += 1
        print('You made', str(moves), 'moves in game', str(games))
        print('Your score was ' + score.text)
        moves = 0
        retry.click()

print('Your best score over', str(num_of_games), 'games was', best_score.text)

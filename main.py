import requests
import keyboard
import time
import random
import mouse
from random import randint
from bs4 import BeautifulSoup
from selenium import webdriver

def input_word(syllable):
    match_list = []
    start_list = []
    global old_word

    with open('word_list.txt', 'rt') as word_file:
        data = word_file.readlines()
    for line in data:
        if syllable in line:
            match_list.append(line)

    if match_list != []:
        for string in match_list:
            if string.startswith(syllable):
                start_list.append(string)
        if len(start_list) > 1 and randint(1,2) == 1:
            word = random.choice(start_list)
            if word == old_word:
                i = start_list.index(word)
                del start_list[i]
                word = random.choice(start_list)
        else:
            word = random.choice(match_list)
        print("Word Found!: " + word)
        old_word = word

        if randint(1,150) == 12:
            keyboard.write(word[0])
            time.sleep(randint(3,7)/100)
            keyboard.press_and_release('enter')
            time.sleep(randint(3,7)/100)
        time.sleep(randint(6,15)/10)
        for letter in word:
            if randint(1,100) == 12:
                keyboard.write(letter)
                time.sleep(randint(3,7)/100)
                keyboard.write(letter)
                time.sleep(randint(33,42)/100)
                keyboard.press_and_release('backspace')
                time.sleep(randint(3,7)/100)
                keyboard.press_and_release('backspace')
                time.sleep(randint(3,7)/100)
            keyboard.write(letter)
            if randint(1,60) == 12:
                time.sleep(randint(37,44)/100)
            time.sleep(randint(5,10)/100)
        time.sleep(randint(6,8)/100)
        keyboard.press_and_release('enter')
        time.sleep(randint(6,8)/100)
        mouse.click('left')

def tip_word(syllable):
    match_list = []
    start_list = []

    with open('word_list.txt', 'rt') as word_file:
        data = word_file.readlines()
    for line in data:
        if syllable in line:
            match_list.append(line)

    if match_list != []:
        for string in match_list:
            if string.startswith(syllable):
                start_list.append(string)
        if len(start_list) > 1 and randint(1,2) == 1:
            word = random.choice(start_list)
        else:
            word = random.choice(match_list)
        word = word[:-1]
        print("Tip: " + word)

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Carter\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path = PATH)
driver.get("https://jklm.fun/")

print("Waiting for game...")
while True:
    if len(driver.find_elements_by_tag_name("iframe")) == 1:
        print("Game found!")
        driver.switch_to.frame(0)
        global old_word
        old_name = ""
        old_word = ""
        time.sleep(2)
        while True:
            driver.switch_to.default_content()
            if(len(driver.find_elements_by_tag_name("iframe")) == 0):
                break
            driver.switch_to.frame(0)
            time.sleep(0.2)
            body = driver.find_element_by_tag_name('body').text
            if "Show rules" in body:
                syl = body.splitlines()[2].lower()
                name = body.splitlines()[3]
                if name != old_name:
                    old_name = name
                    print(name)
                    tip_word(syl)
            else:
                syl = body.splitlines()[1].lower()
                counter = 0
                input_word(syl)

import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from lxml import html
import csv
import time
import random
import json
import math


def simulate(htmlstring, driver):


    userID = "markoaleksic0616@gmail.com"
    pwd = "akfldaidqh1989"
    txt = "Hello, \n Nice to meet you. \n\n I am a full stack and full time freelancer. \n\n I wanna discuss some problems. \n When you have free time, please ping me here. \n\n Thanks."

    user_input = driver.find_element_by_id("username")
    user_input.send_keys(userID)
    time.sleep(3)

    pwd_input = driver.find_element_by_id("password")
    pwd_input.send_keys(pwd)
    time.sleep(3)

    signinBtn = driver.find_element_by_xpath("//button[contains(@class, 'btn__primary--large') and contains(@class, 'from__button--floating')]")
    signinBtn.click()
    time.sleep(5)

    filepath = 'ukraine_linkedin_1.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            # print("Line {}: {}".format(cnt, line.strip()))
            print(cnt, line.strip())
            line = fp.readline()
            
            if cnt >= 50 and cnt < 100:
                url = line.strip()

                driver.get(url)
                time.sleep(10)

                try:
                    connectBtn = driver.find_element_by_id("ember62")
                    btnText = driver.find_element_by_xpath("//button[@id='ember62']/span").text
                    if "Connect" in btnText:
                        connectBtn1 = True
                    else:
                        connectBtn1 = False
                except:
                    connectBtn1 = False


                try:
                    if connectBtn1:
                        connectBtn.click()
                        time.sleep(1)
                        print("------------------------------> Click Connect Button")

                        time.sleep(1)
                        add_noteBtn = driver.find_element_by_xpath("//button[@aria-label='Add a note']")
                        print(add_noteBtn)
                        add_noteBtn.click()
                        time.sleep(1)

                        text_area = driver.find_element_by_id("custom-message")
                        text_area.send_keys(txt)
                        time.sleep(2)

                        try:
                            doneBtn = driver.find_element_by_xpath("//button[@aria-label='Done']")    
                            doneBtn.click()

                        except:
                            doneBtn = driver.find_element_by_xpath("//button[@aria-label='Send invitation']")    
                            doneBtn.click()

                    else:
                        moreBtn = driver.find_element_by_id("ember68")
                        moreBtn.click()
                        time.sleep(1)

                        connectBtn = driver.find_element_by_id("ember87")
                        connectBtn.click()
                        time.sleep(1)

                        add_noteBtn = driver.find_element_by_xpath("//button[@aria-label='Add a note']")
                        print(add_noteBtn)
                        add_noteBtn.click()
                        time.sleep(1)

                        text_area = driver.find_element_by_id("custom-message")
                        text_area.send_keys(txt)
                        time.sleep(2)

                        try:
                            doneBtn = driver.find_element_by_xpath("//button[@aria-label='Done']")    
                            doneBtn.click()

                        except:
                            doneBtn = driver.find_element_by_xpath("//button[@aria-label='Send invitation']")    
                            doneBtn.click()

                except:
                    print("Continue")
                time.sleep(30)
            cnt += 1
    

if __name__ == '__main__':

    path = "driver\\chromedriver.exe"

    driver = Chrome(executable_path=path)
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    driver.maximize_window()
    time.sleep(10)

    simulate(driver.page_source, driver)
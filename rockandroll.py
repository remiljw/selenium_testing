# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys
import time


mails = ['admi0nest@yahoo.com', 'admi9ntest@gmail.com'] #list of emails go here
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://vote.rockhall.com/results"
driver.get(url) 

try:
    for mail in mails:
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[3]/div/main/div/div[2]/div/a[2]'))).click()
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.rock-cookie-popup-accept'))).click()
                print('Cookie Accepted')
            except:
                print("Could not accept cookie")

            try:
                select_fela = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'artistNominee010'))).send_keys(keys.Keys.SPACE)
                print('Fela Selected')
            except:
                print('Could Not Select Fela')
                
            try:
            
                login = driver.find_element_by_css_selector(".rock-button-primary")
                login.click()
                emailbox = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.rock-input')))
                emailbox.send_keys(mail)
                register_email = driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div[3]/div/main/div/section/div/form/button[1]').click() 
                
                print("Logged in")
            except:
                print ("Could Not Log in")

            try:
                count_vote = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[3]/div/main/div/section/div/div/button[1]'))).click()
                success = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[3]/div/main/div/div[2]/a[1]'))).click()
                print('Vote Submitted')   
            except:
                try:
                    already_voted = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[3]/div/main/div/section/div/div/a'))).click()
                    print('Already Voted')
                except:
                    print('Could Not Submit Vote')
except:
        print("An error has occurred")
        time.sleep(10)
        driver.quit()

driver.quit()


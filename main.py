from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from random_username.generate import generate_username

import names
import requests
import json
import time
import random
import os
import string
import sys
from dhooks import Webhook

# Webhook sender
hookurl = Webhook("https://discord.com/api/webhooks/901336319719002183/w7C5K8sTyFIjUMGwNFk0QHKYADWAA9-MYcy-WFDDOxYmCvLViyBNv00EUPSwIVKvn24e")

# 2captcha stuff

#5sim stuff
token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjY1ODkwMjgsImlhdCI6MTYzNTA1MzAyOCwicmF5IjoiMDJlY2JjZTQzYWQwYzUxOWM3MjcyZWM2MDU2OTZmYjQiLCJzdWIiOjQ2ODEzMX0.Gwir_J9kmpW7qcxk7US-d3FgliPpVvRRnZPNmm1F2QCSvI_3a_qOmPCBo9PYTceVURSN0flgMA8TKqZ8wxF_qEU4YXCTWmzfwuVTqY96x9KgT_Kb8WkZDwQEDXT-liVuEiesRYkNmFwFAOd7Urttljyq2R-2kRtTCHDGzhd1TgYGhwOo7Usgxzb5JVys15zMfYU5z0HxEmTDzp-oYWlaQelW4aEfVH1YobZHIQEr8aXO0pL8e-YnuuGxV876ThMBrXwIoWVtBJ3o8UW1N0k2RDccsnv0nxSdSIHg8IXna6PHieEhHB2kqypfIXrsPWSJyTTYgzSmVLxU1QyykaIOiQ'
country = 'russia'
operator = 'virtual27'
product = 'blizzard'

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
}
# 5sim var
phoneVerf = 1 # Ignore this..

if phoneVerf := 1:
    # 5sim Part
    print("[+] Requesting phone number..")
    response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product,
                            headers=headers)
    # print(response)
    data = json.loads(response.text)
    id = data['id']
    phoneNumberr = data['phone']
    print("Phone Request Info:")
    print('Phone Number: ' + str(phoneNumberr))
    print('Phone Price: ' + str(data['price']))
    # End 5Sim

#Generator Stuff

while True:
    try:
        
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--window-size=600,920')
       #chrome_options.add_argument('--proxy-server=2154.16.63.16:8080') get a working proxy and u done
        web: WebDriver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
        web.get('https://account.battle.net/creation/flow/creation-full')
        print(web.title + " process was started")
        hookurl.send(f"Script started.")
        def random_string(string_length=12):
            # Generate a random string of letters and digits
            letters_hexdigits = string.hexdigits
            return ''.join(random.choice(letters_hexdigits) for i in range(string_length))
            
        def random_firstName(string_length=10):
            # Generate a random first name.
            name_firstName = string.ascii_letters
            return ''.join(names.get_first_name((name_firstName) for i in range(string_length)))
            
        def random_lastName(string_length=10):
            # Generate a random last name.
            name_lastName = string.ascii_letters
            return ''.join(names.get_first_name((name_lastName) for i in range(string_length)))
            
        # Strings
        Email = random_string()
        firstName = random_firstName()
        lastName = random_lastName()
        domain = "@happylobb.com"
        password = random_string()
        securityQuestion = "VYNXC IS GAY"
        bnetName = "VynxcSuxChox"
        print(firstName, Email, lastName, domain, password, bnetName, securityQuestion)
        #Generator stuff
        x = 1

        cntry = Select(web.find_element_by_xpath('//*[@id="capture-country"]'))
        cntry.select_by_visible_text("Russian Federation")
        print("Country set as Russian Federation")
        time.sleep(0.1)

        time.sleep(0.5)
        print("DOB set to 11/11/2000")
        c1 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c1.click()

        dob = web.find_element_by_xpath('//*[@id="dob-field-inactive"]')
        dob.click()
        dob2 = web.find_element_by_xpath('//*[@id="dob-field-active"]/input[1]')
        dob2.send_keys(11112000)


        time.sleep(0.5)
        print("Waiting for captcha completion")
        wait = WebDriverWait(web, 200)
        wait.until(EC.element_to_be_clickable((By.ID, 'capture-first-name')))
        time.sleep(0.2)
        fn = web.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[1]/input')
        fn.send_keys(firstName)
        ln = web.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/input')
        ln.send_keys(lastName)
        c2 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c2.click()
        wait = WebDriverWait(web, 200)
        wait.until(EC.visibility_of_element_located((By.ID, 'capture-email')))
        time.sleep(0.2)
        mail = web.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[1]/input')
        mail.send_keys(Email + domain)
        # Insert SMS Recieve here
        phone = web.find_element_by_xpath('//*[@id="capture-phone-number"]')
        phone.click()
        phoneNumbr = str(phoneNumberr)
        phone.send_keys(phoneNumbr)

        c3 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c3.click()
        time.sleep(0.2)

        if phoneVerf := 1:
            codeInp = ""
        while (requests.get('https://5sim.net/v1/user/check/' + str(id), headers=headers)):
            response = requests.get('https://5sim.net/v1/user/check/' + str(id), headers=headers)
            data = json.loads(response.text)
            print(data)
            if (data['status'] == "RECEIVED"):
                if (data['sms']):
                    codeInp = data['sms'][0]['code']
                    # print("Code: " + data['sms'][0]['code'])
                    break
            elif (data['status'] == "PENDING"):
                print("Waiting for code")
            else:
                print("Something went wrong: STATUS: " + data['status'])
        print("[+] Got SMS Code: " + codeInp)
        code5 = web.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[1]/div/input[1]')
        code5.click()
        code5.send_keys(codeInp)
        time.sleep(0.2)
        varmistus = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        varmistus.click()

        wait = WebDriverWait(web, 400)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'step__field--label__text')))
        # EC wait END
        time.sleep(0.2)
        tos = web.find_element_by_xpath('//*[@id="legal-checkboxes"]/label')
        tos.click()
        c4 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c4.click()
        wait = WebDriverWait(web, 200)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-password"]')))
        time.sleep(0.2)
        pw = web.find_element_by_xpath('//*[@id="capture-password"]')
        pw.click()
        pw.send_keys(password)
        c5 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c5.click()
        time.sleep(0.2)
        wait = WebDriverWait(web, 200)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
        time.sleep(0.2)
        name3 = web.find_element_by_xpath('//*[@id="capture-battletag"]')
        name3.click()
        name3.clear();
        name3.send_keys(bnetName)
        time.sleep(0.1)
        c6 = web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]')
        c6.click()
        time.sleep(0.2)
        web.get('https://www.blizzard.com/login')
        wait = WebDriverWait(web, 200)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/div/input')))
        time.sleep(0.3)
        l1 = web.find_element_by_xpath('//*[@id="accountName"]')
        l1.click()
        l1.send_keys(Email + domain)
        l2 = web.find_element_by_xpath('//*[@id="password"]')
        l2.click()
        l2.send_keys(password)
        l3 = web.find_element_by_xpath('//*[@id="submit"]')
        l3.click()
        time.sleep(2.5)
        web.get('https://account.battle.net/overview')
        time.sleep(2.5)
        web.get('https://account.battle.net/security#secret-question')
        wait = WebDriverWait(web, 200)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/section[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/span/a')))
        s2 = web.find_element_by_xpath('/html/body/div[1]/main/section[2]/div/div[4]/div[2]/div/div[2]/div/div/div[2]/span/a')
        s2.click()
        time.sleep(0.5)
        s3 = Select(web.find_element_by_xpath('//*[@id="question-select"]'))
        s3.select_by_visible_text("What was the first car you owned?")
        time.sleep(0.5)
        s4 = web.find_element_by_xpath('//*[@id="answer"]')
        s4.click()
        s4.send_keys(securityQuestion)
        time.sleep(0.5)
        s5 = web.find_element_by_xpath('//*[@id="sqa-submit"]')
        s5.click()
        time.sleep(0.5)
        #
        print ("Email set to: " + Email + domain)
        print("Password set to:  " + password)
        print("Security Question Set as:  " + securityQuestion)
        print("Name Was randomised")
        print("Code Ran successfully [DEBUG]")
        print(Email + domain + ":" + password + ":" + securityQuestion)
        hookurl.send(f"{Email}@happylobb.com : {password} : {securityQuestion} : {bnetName}")
        hookurl.send(f"Script executed sucessfully.")
        web.close()
        os.execl(sys.executable, sys.executable, *sys.argv)
    except KeyboardInterrupt:
        hookurl.send(f"Script execution stopped by user.")
        exit()
        ##updated by ayyo#0001
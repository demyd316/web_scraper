import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
#####NEW CODE##################
LinkOne = "https://www.currys.co.uk/gbuk/smart-tech/smart-tech/smart-watches-and-fitness/smart-watches/samsung-galaxy-watch-active-rose-gold-10190976-pdt.html"
# LinkOne = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/msi-geforce-rtx-3060-ti-8-gb-ventus-2x-oc-graphics-card-10219342-pdt.html"
LinkTwo = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/msi-geforce-rtx-3060-ti-8-gb-ventus-3x-oc-graphics-card-10219341-pdt.html"
LinkThree = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/msi-geforce-rtx-3060-ti-8-gb-gaming-x-trio-graphics-card-10219250-pdt.html"
LinkFour = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-gaming-oc-graphics-card-10219305-pdt.html"
LinkFive = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-eagle-oc-graphics-card-10219306-pdt.html"
LinkSix = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-eagle-graphics-card-10219307-pdt.html"
LinkSeven = "https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/gigabyte-geforce-rtx-3060-ti-8-gb-aorus-master-graphics-card-10219303-pdt.html"
###############################
# PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome()

    #EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[3]/div[2]/section/div[4]/div[4]/div[1]/button'))
def Check():
    addtobasket = browser.find_element_by_class_name("space-b center")
    addtobasket = browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[3]/div[2]/section/div[3]/div[2]/div[4]/div[1]/button')
    addtobasket.click()
    pass

#click Accept all cookie button
browser.get(LinkOne)
while True:
    try:
        cookies = browser.find_element_by_class_name("banner-actions-container")
        cookies.click()
        break
    except NoSuchElementException:
        pass

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get(LinkTwo)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[2])
browser.get(LinkThree)
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[3])
browser.get(LinkFour)
browser.switch_to.window(browser.window_handles[0])


#browser.get(httpswww.currys.co.ukgbukcomputing-accessoriescomponents-upgradesgraphics-cardsgigabyte-geforce-rtx-3060-ti-8-gb-gaming-oc-graphics-card-10219305-pdt.html)

#FAIL SAFE. This will 100% kill the program after the GPU has been bought
def yay():
    print("Your GPU is paid and coming !")
    sys.exit()

buybutton = False

while not buybutton:

    try: #测试以下代码
        addtocart = browser.find_element_by_class_name("nostock") 
        print("Nope.. You still can't get your RTX 3060ti..")
        time.sleep(5)
        browser.refresh()
        Check()
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(1)
        browser.refresh()
        Check()
        browser.switch_to.window(browser.window_handles[2])
        time.sleep(1)
        browser.refresh()
        Check()
        browser.switch_to.window(browser.window_handles[3])
        time.sleep(1)
        browser.refresh()
        Check()
        browser.switch_to.window(browser.window_handles[0])

    except: #没有找到上面代码的话 执行以下代码
        print("Button Was Clicked, Lucky")
        time.sleep(5)
        browser.get("https://www.currys.co.uk/app/checkout")
        while True:
            try:
                time.sleep(1)
                ContinueToBasket = browser.find_element_by_xpath("""/html/body/div[16]/div/div/div[1]/div[2]/button""")
                ContinueToBasket.click()
                break
            except WebDriverException:
                pass
        while True:
            try:
                ContinueToBasket = browser.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/button""")
                ContinueToBasket.click()
                break
            except WebDriverException:
                pass
        while True:
            try:
                postCode = """/html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/form/input"""
                browser.find_element_by_xpath(postCode).send_keys("Leeds")
                time.sleep(1)
                browser.find_element_by_xpath(postCode).send_keys("" + Keys.ENTER)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                free = browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button")
                free.click()
                break
            except WebDriverException:
                pass
        while True:
            try:
                email = """
        //*[@id="root"]/div/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/div[1]/div/input
        """
                browser.find_element_by_xpath(email).send_keys("Test@gmail.com")
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/form/button").click()
                break
            except WebDriverException:
                pass
        while True:
            try:
                Guest = browser.find_element_by_xpath("""//*[@id="root"]/div/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div/div/div/span[2]/span/a""")
                Guest.click()
                break
            except WebDriverException:
                pass
        while True:
            try:
                Title = browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[2]/div/div[1]/input""")
                Title.click()
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[2]/div/div[1]/input""").send_keys("" + Keys.ARROW_DOWN)
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[2]/div/div[1]/input""").send_keys("" + Keys.ENTER)
                break
            except NoSuchElementException:
                pass
        # Lots of shite
        while True:
            try:
                DelPostCode = """//*[@id="addresses"]/div[2]/div[6]/div[1]/div/input"""
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.ARROW_DOWN)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.ENTER)
                break
            except NoSuchElementException:
                pass
#CONFIG
######################################################################################################################
        Email = "Test@gmail.com"
        FirstName = "FIRST NAME"
        LastName = "Last Name"
        Number = "07483737784"
        PostCode = "LS11 9QJ"
        Address = "21 Sandlewood Green"
        City = "Leeds"
        CardNumber = "5555555555554444"
        Month = "2"
        Year = "23"
        SecureCode = "341"
######################################################################################################################
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[3]/input""").send_keys(FirstName)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[4]/input""").send_keys(LastName)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[5]/div/input""").send_keys(Number)
                break
            except NoSuchElementException:
                pass

        while True:
            try:
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                browser.find_element_by_xpath(DelPostCode).send_keys("" + Keys.BACKSPACE)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[6]/div[1]/div/input""").send_keys(PostCode)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[8]/input""").send_keys(Address)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[10]/input""").send_keys(City)
                browser.find_element_by_xpath("""//*[@id="addresses"]/div[2]/div[10]/input""").send_keys("" + Keys.ENTER)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                time.sleep(5)
                Card = browser.find_element_by_xpath("""/html/body/div[4]/div/div[2]/div[2]/div/div/div[4]/div[2]/div[2]/div[2]/div[2]/div[1]/button""")
                Card.click()
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="cardholderName"]""").send_keys(FirstName.upper() + " " + LastName.upper())
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="cardNumber"]""").send_keys(CardNumber)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="expiryMonth"]""").send_keys(Month)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="expiryYear"]""").send_keys(Year)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                browser.find_element_by_xpath("""//*[@id="securityCode"]""").send_keys(SecureCode)
                break
            except NoSuchElementException:
                pass
        while True:
            try:
                PAY = browser.find_element_by_xpath("""//*[@id="submitButton"]""")
                PAY.click()
                break
            except WebDriverException:
                pass
        buybutton = True
        yay()
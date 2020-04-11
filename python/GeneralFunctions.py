import sys
import random
import string
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class GeneralFunctions:
    # setting up the webdriver
    # param: website (str) pass the webadress e.g.: https://twitch.com
    @staticmethod
    def openWindow(driver, website, streamer=''):
        driver.get(website + '/' + streamer)
        driver.maximize_window()
        sleep(3)
        return

    # finds element with its tag-name and "data-test-selector"
    # param:
    #       + elementType (str) e.g.: 'button', 'textarea', usw
    #       + elementAttribute (str) pass the 'data-a-target' e.g.: 'chat-send-button', 'chat-send-button'
    @staticmethod
    def findElementByTagName(driver, elementType, attributeValue, attribute):
        wantedElements = driver.find_elements_by_tag_name(elementType)
        for idx in wantedElements:
            if idx.get_attribute(attribute) == attributeValue:
                return idx
        return None

    # finds elements with its tag-name and "data-test-selector"
    # param:
    #       + elementType (str) e.g.: 'button', 'textarea', usw
    #       + elementAttribute (str) pass the 'data-a-target' e.g.: 'chat-send-button', 'chat-send-button'
    @staticmethod
    def findElementsByTagName(driver, elementType, attributeValue, attribute):
        allElements = driver.find_elements_by_tag_name(elementType)
        wantedElements = []
        for idx in allElements:
            if idx.get_attribute(attribute) == attributeValue:
                wantedElements.append(idx)
        return wantedElements

    # find the code in the email
    # param: elementType (str) e.g.: 'p'
    @staticmethod
    def findCode(driver, elementType):
        wantedElement = None
        allOfType = driver.find_elements_by_tag_name(elementType)
        for element in allOfType:
            if len(element.text) == 6:
                wantedElement = element
        if wantedElement is None:
            print("Code not found")
            return None
        return wantedElement

    # clicks the wanted button
    # param: buttonAttribute (str) pass the 'data-a-target' e.g.: 'chat-send-button'
    @staticmethod
    def clickButton(driver, buttonAttribute, elementType='button', attribute='data-a-target'):
        element = GeneralFunctions.findElementByTagName(driver, elementType, buttonAttribute, attribute)
        if element is None:
            print("Button not found")
            return
        element.click()

    # passes the wanted text to the textbox
    # param:
    #       + areaAttribute (str)
    #       + text (str) pass the 'data-a-target' of the textbox e.g.: 'chat-input'
    @staticmethod
    def insertText(driver,  attributeValue, text, elementType='textarea', attribute='data-a-target'):
        element = GeneralFunctions.findElementByTagName(driver, elementType, attributeValue, attribute)
        if element is None:
            print("Textbox not found")
            return
        element.send_keys(text)

    # generate 3 digit random number
    @staticmethod
    def randomNumber(minDigits=1, maxDigits=4, lower=0, upper=9):
        number = ''
        for i in range(minDigits, maxDigits):
            number += str(random.randrange(lower, upper))
        return number

    # generate username
    @staticmethod
    def generateUsername(firstName, lastName):
        letters = string.ascii_lowercase
        username = firstName + lastName
        for i in range(3):
            username += str(random.choice(letters))
        username += GeneralFunctions.randomNumber()
        return username

    # generate 8 digit password
    @staticmethod
    def generatePassword(pwLenght=8):
        letters = string.ascii_lowercase
        letters += string.ascii_uppercase
        specialChar = ["!", "$", "#", "+", "%"]
        pwstring = ''.join(random.choice(letters) for i in range(pwLenght - 1))
        return pwstring + random.choice(specialChar)

    # safe userdata to .txt file
    @staticmethod
    def storeUserdata(self, file='userdata.txt'):
        userdata = open(file, "w")
        userdata.write(self.firstName + ', ')
        userdata.write(self.lastName + ', ')
        userdata.write(self.username + '@protonmail.com, ')
        userdata.write(self.password + ', ')
        userdata.write(self.birthday + ', ')
        userdata.write(self.birthmonth + ', ')
        userdata.write(self.birthyear + '\n')
        userdata.close()

    # get last email
    @staticmethod
    def getLastUser():
        userdatafile = open("userdata.txt", "r")
        userdata = userdatafile.readlines()
        userdatafile.close()
        lastUserdata = userdata[-1].split(', ')
        lastUserEmail = lastUserdata[2]
        lastUserPw = lastUserdata[3]
        return lastUserEmail, lastUserPw



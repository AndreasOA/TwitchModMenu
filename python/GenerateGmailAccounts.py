from selenium import webdriver
from GeneralFunctions import *


class GenerateGmailAccounts:
    def __init__(self, firstName, lastName):
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.username = GeneralFunctions.generateUsername(self.firstName, self.lastName)
        self.password = GeneralFunctions.generatePassword(8)
        self.birthday = GeneralFunctions.randomNumber(minDigits=1, maxDigits=3, lower=1, upper=10)
        self.birthmonth = int(GeneralFunctions.randomNumber(minDigits=1, maxDigits=2, lower=1, upper=13))
        self.birthyear = GeneralFunctions.randomNumber(minDigits=4, maxDigits=5, lower=1980, upper=2003)
        self.gender = int(GeneralFunctions.randomNumber(minDigits=1, maxDigits=2, lower=1, upper=3))
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.lastUserEmail, self.lastUserPw = GeneralFunctions.getLastUser()

    def generate(self):
        GeneralFunctions.openWindow(self.driver, "https://mail.protonmail.com/create/new?language=en")
        sleep(3)
        iframe = self.driver.find_elements_by_tag_name('iframe')
        self.driver.switch_to.frame(iframe[0])
        GeneralFunctions.insertText(self.driver, 'username', self.username, elementType='input', attribute='id')
        self.driver.switch_to.default_content()
        GeneralFunctions.insertText(self.driver, 'password', self.password, elementType='input', attribute='id')
        GeneralFunctions.insertText(self.driver, 'passwordc', self.password, elementType='input', attribute='id')
        self.driver.switch_to.frame(iframe[1])
        sleep(0.5)
        GeneralFunctions.clickButton(self.driver, 'submitBtn', elementType='button', attribute='name')
        self.driver.switch_to.default_content()
        sleep(0.5)
        GeneralFunctions.clickButton(self.driver, 'confirmModalBtn', elementType='button', attribute='id')
        sleep(3)
        GeneralFunctions.clickButton(self.driver, 'id-signup-radio-email', elementType='input', attribute='id')
        GeneralFunctions.insertText(self.driver, 'emailVerification', self.lastUserEmail,
                                    elementType='input', attribute='id')
        GeneralFunctions.clickButton(self.driver, 'pm_button primary codeVerificator-btn-send',
                                     elementType='button', attribute='class')
        



    def runGenorator(self):
        self.generate()
        GeneralFunctions.storeUserdata(self)


acc1 = GenerateGmailAccounts('hans', 'peter')
acc1.runGenorator()

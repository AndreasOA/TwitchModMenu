from GeneralFunctions import *


class GmailCodeRead:
    def __init__(self, email, password):

        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(r'chromedriver.exe')

    def login(self):
        GeneralFunctions.insertText(self.driver, 'email', self.email, elementType='input', attribute='type')
        GeneralFunctions.clickButton(self.driver, 'RveJvd snByac', elementType='span', attribute='class')

        while self.driver.find_element_by_class_name('xkfVF').get_attribute('tabindex') == '-1':
            pass

        sleep(0.1)
        GeneralFunctions.insertText(self.driver, 'password', self.password, elementType='input', attribute='type')
        sleep(0.1)
        GeneralFunctions.clickButton(self.driver, 'RveJvd snByac', elementType='span', attribute='class')

    def getCode(self):
        while True:
            try:
                siteLoaded = self.driver.find_element_by_class_name('aAU')
                if siteLoaded.get_attribute('data-awr-sg-installed') == 'true':
                    break
            except NoSuchElementException:
                pass
        for element in self.driver.find_elements_by_tag_name('tr'):
            if 'zA' in element.get_attribute('class') and 'zE' in element.get_attribute('class'):
                for idx in element.find_elements_by_tag_name('span'):
                    if idx.text == 'Twitch':
                        element.click()
                        break
                break
        sleep(1)
        code = GeneralFunctions.findCode(self.driver, 'p').text
        return code

    def run(self):
        GeneralFunctions.openWindow(self.driver, 'https://gmail.com')
        self.login()
        code = self.getCode()
        sleep(1)
        self.driver.close()
        return str(code)

from GeneralFunctions import *
from GmailCodeRead import *


class TwitchChatbot:
    def __init__(self, username, password, streamername, gmailmail, gmailpw):

        self.username = username
        self.password = password
        self.streamername = streamername
        self.gmailmail = gmailmail
        self.gmailpassword = gmailpw
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.action = ActionChains(self.driver)

    # Reading in the chats from .txt file
    # returns a list containing different frases
    @staticmethod
    def getChats(filename):
        chatTextFile = open(filename, "r")
        chatsList = chatTextFile.read()
        return chatsList.split(',')

    # logs in with the given account data
    def loginAccount(self, testing=False):
        # Open login frame
        GeneralFunctions.clickButton(self.driver, 'login-button')
        sleep(0.5)
        # pass login data
        self.driver.find_element_by_id('login-username').send_keys(self.username)
        self.driver.find_element_by_id('password-input').send_keys(self.password)

        # press login button
        GeneralFunctions.clickButton(self.driver, 'passport-login-button')
        if testing:
            sleep(10)
        mailacc = GmailCodeRead(self.gmailmail, self.gmailpassword)
        code = mailacc.run()
        GeneralFunctions.findElementByTagName(self.driver, 'input', 'text', attribute='type').send_keys(code)

    def streamOptions(self, autoFollow='True', mute='True'):
        while True:
            try:
                GeneralFunctions.findElementByTagName(self.driver, 'button', 'whisper-box-button',
                                                      attribute='data-a-target')
                sleep(1)
                break
            except NoSuchElementException:
                pass

        if autoFollow:
            followButton = GeneralFunctions.findElementByTagName(self.driver, 'button', 'follow-button',
                                                                 attribute='data-a-target')
            if followButton is not None:
                self.driver.execute_script("arguments[0].scrollIntoView();", followButton)
                followButton.click()
                sleep(1)

        if mute:
            muteButton = GeneralFunctions.findElementByTagName(self.driver, 'button', 'player-mute-unmute-button',
                                                               'data-a-target')
            self.action.move_to_element(muteButton).perform()
            muteButton.click()

            optionsButton = GeneralFunctions.findElementByTagName(self.driver, 'button', 'player-settings-button',
                                                                  'data-a-target')
            self.action.move_to_element(optionsButton).perform()
            optionsButton.click()

            qualityButton = GeneralFunctions.findElementByTagName(self.driver, 'button',
                                                                  'player-settings-menu-item-quality'
                                                                  , 'data-a-target')
            self.action.move_to_element(qualityButton).perform()
            qualityButton.click()

            qualityOptions = GeneralFunctions.findElementsByTagName(self.driver, 'input',
                                                                    'tw-radio', 'data-a-target')
            self.action.move_to_element(qualityOptions[-1]).perform()
            qualityOptions[-1].click()


    # chats random frases
    def chating(self, good=False, bad=False):
        randomfrases = TwitchChatbot.getChats('randomfrases.txt')
        goodfrases = TwitchChatbot.getChats('goodfrases.txt')
        badfrases = TwitchChatbot.getChats('badfrases.txt')
        cooldown = 0
        while True:
            if not good and not bad:
                if cooldown > random.randrange(32, 360):
                    GeneralFunctions.insertText(self.driver, 'chat-input',
                                                randomfrases[random.randrange(len(randomfrases))])
                    cooldown = 0
                sleep(1)
            elif good:
                GeneralFunctions.insertText(self.driver, 'chat-input',
                                            randomfrases[random.randrange(len(goodfrases))])
                good = False
            elif bad:
                GeneralFunctions.insertText(self.driver, 'chat-input',
                                            randomfrases[random.randrange(len(badfrases))])
                bad = False

    # running the bot
    def runBot(self):
        GeneralFunctions.openWindow(self.driver, 'https://twitch.com', self.streamername)
        self.loginAccount(testing=True)
        self.streamOptions()
        self.chating()


tb1 = TwitchChatbot(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
tb1.runBot()

import sys
from TwitchChatbot import *

account_name = sys.argv[1]
account_password = sys.argv[2]
twitch_username = sys.argv[3]
twitch_password = sys.argv[4]
twitch_viewgenre = sys.argv[5]

tb1 = TwitchChatbot(twitch_username, twitch_password, twitch_viewgenre, account_name, account_password)
tb1.runBot()

print(account_name + account_password + twitch_username + twitch_password + twitch_viewgenre )
sys.stdout.flush()

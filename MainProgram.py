import telepot
import sys
from TelegramBotSets import Telegram_MSG


class Main:
	def __init__(self):
		self.TelegramKey = ""  # Initialize the TokenAPI as blank
		self.treatysargv()  # TokenAPI treatment

		try:
			self.Telegram_Bot = telepot.Bot(self.TelegramKey)  # Initialize the Bot with TokenAPI
		except telepot.exception.TelegramError:
			print("There is an error with TOKEN API!")
			exit()

		# MySql Configs ##########################
		''' Configure o telegram_bot_msg with your MySql settings
			fhost="localhost", 
			fuser="root", 
			fpassword="admin", 
			fdatabase="telegram_bot"
		'''
		self.MySql_Configs = {"fhost": "localhost", "fuser": "root", "fpassword": "", "fdatabase": "telegram_bot"}
		self.telegram_bot_msg = Telegram_MSG(self.Telegram_Bot, self.MySql_Configs)

		# STARTS LOOP
		self.Telegram_Bot.message_loop(self.telegram_bot_msg.received_msg)
		# ------------------------------------------------------------

	def treatysargv(self):
		# DEFAULT SET TOKEN KEY API AS BLANK

		print(sys.argv)

		# SEARCH FOR AN ARGUMENT if not SEARCH for botkey.txt
		if len(sys.argv) >= 3:
			for i in range(0, len(sys.argv)):
				if sys.argv[i] == "-t":
					self.TelegramKey = sys.argv[i + 1]
					break
		else:
			telegramfilekey = open("botkey.txt", "rt")
			self.TelegramKey = telegramfilekey.read()
			telegramfilekey.close()

		print("Telegram Bot Key: " + str(self.TelegramKey))

		# Exit if no key were found
		if len(self.TelegramKey) < 2:
			exit()


if __name__ == '__main__':
	pass

while True:
	pass

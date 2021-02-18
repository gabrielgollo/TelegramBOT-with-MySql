import telepot
import sys
from DBconnect import MyDatabase
from TelegramBotSets import Telegram_MSG

class Main:

	#DEFAULT SET TELEGRAMKEY AS "0"
	TelegramKey = ""
	print(sys.argv)
	#SEARCH FOR AN ARGUMENT if not SEARCH for botkey.txt
	if len(sys.argv) >= 3:
		for i in range(0, len(sys.argv)):
			if sys.argv[i] == "-t":
				TelegramKey = sys.argv[i + 1]
				break
	else:
		TelegramFileKey = open("botkey.txt", "rt")
		TelegramKey = TelegramFileKey.read()
		TelegramFileKey.close()

	print("Telegram Bot Key: " + str(TelegramKey))


	### Exit if no key were founded
	if ( len(TelegramKey) < 2):
		exit()


	try:
		Telegram_Bot = telepot.Bot(TelegramKey)
	except telepot.exception.TelegramError:
		print("There is an error with TOKEN API!")
		exit()

	telegram_bot_msg = Telegram_MSG(Telegram_Bot)

	##STARTS LOOP
	Telegram_Bot.message_loop(telegram_bot_msg.received_msg)


if __name__ == '__main__':
    pass

while True:
	pass
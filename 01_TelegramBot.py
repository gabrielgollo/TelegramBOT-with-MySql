import os
import telepot
import sys
import mysql.connector
from DBconnect import MyDatabase


class Telegram_MSG:
	def __init__(self):
		self.database = MyDatabase()

	def Received_msg(self, msg):

		print(msg)
		mensagem = msg['text']
		mensagem_Lowercase = str(mensagem).lower()

		print("Mensagem Enviada pra consulta:")
		print(mensagem_Lowercase+"\n")

		# ChatId = msg['chat']['id']
		tipoMsg, tipochat, ChatId = telepot.glance(msg)

		if(self.database== None):
			exit()



		### IF IT'S A COMMAND
		if (mensagem_Lowercase[:1] == "/"):
			print(mensagem_Lowercase[:1])
			print("here")
			answerMsg = self.database.searchMsg(mensagem_Lowercase[0:], "commands")
			pass

		else: # It's a msg
			answerMsg = self.database.searchMsg(mensagem_Lowercase, "dicionario")
			if len(answerMsg)>1:
				Telegram_Bot.sendMessage(ChatId, answerMsg)
				print("Resposta encontrada Enviada para o chat:")
				print(answerMsg)
			else:
				if msg['chat']['username'] == 'GabrielGollo':
					answerMsg = "Resposta não encontrada, deseja adicionar uma?"
					print(answerMsg+"\n")
					Telegram_Bot.sendMessage(ChatId, answerMsg)

					Telegram_Bot.getUpdates()
					if msg['text'].lower() == 'sim':
						self.database.imprimir()

		self.database.close()



TelegramKey=0
print(sys.argv)
for i in range(0, len(sys.argv)):
	if sys.argv[i] == "-t":
		TelegramKey = sys.argv[i+1]
		break

print("Telegram Bot Key: "+str(TelegramKey))


TelegramFileKey= open("botkey.txt", "rt")
TelegramKey= TelegramFileKey.read()
TelegramFileKey.close()


### Exit if no key were founded
if(TelegramKey == 0):
	exit()



Telegram_Bot = telepot.Bot(TelegramKey)

class main():

	telegram_bot_msg = Telegram_MSG()
	Telegram_Bot.message_loop(telegram_bot_msg.Received_msg)


if __name__ == '__main__':
    pass

while True:
    pass
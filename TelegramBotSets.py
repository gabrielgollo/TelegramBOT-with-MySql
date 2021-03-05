import telepot
from DBconnect import MyDatabase
import re

class Telegram_MSG:
	def __init__(self, Telegram_Bot):
		self.database = MyDatabase()
		print(self.database.connected)
		self.Telegram_Bot= Telegram_Bot
		self.connection = self.database.connected
		self.lastmsg={}

	def list_to_str_msg(self, x):
		try:
			return x[0][0]
		except Exception as e:
			return ""

	def search_user(self, usernameID):
		x = self.database.searchMsg(usernameID, 'admins', 'ID', 'username')
		return self.list_to_str_msg(x)

	def received_msg(self, msg):

		if self.database.connected == True:
			#print(msg)
			mensagem = msg['text']
			mensagem_Lowercase = str(mensagem).lower()

			print("Mensagem Enviada pra consulta:")
			print(mensagem_Lowercase+"\n")

			# ChatId = msg['chat']['id']
			tipoMsg, tipochat, ChatId = telepot.glance(msg)

			if(self.database.connected == False):
				print("No database connected")
				exit()


			print(self.search_user(msg['chat']['id']))
			### IF IT'S A COMMAND
			if ( mensagem_Lowercase[:1] == "/" and msg['chat']['username'] == self.search_user(msg['chat']['id']) ):
				print(mensagem_Lowercase[:1])
				### Simplify the text msg
				commandMsg = re.sub("/", "", mensagem_Lowercase)
				commandMsg = commandMsg.split(" ")

				commandkeyDB = commandMsg[0]  # /COMMAND

				answerMsg = self.database.searchMsg(commandkeyDB, "commands", "comando", "arguments")
				print("answermsg founded", answerMsg[0][0])
				if len(commandMsg) == int(answerMsg[0][0])+1:
					try:

						keyA = commandMsg[1]
						keyB = commandMsg[2]
						answerMsg = self.database.searchMsg(commandkeyDB, "commands", "comando", "resultado")
						answerMsg = self.list_to_str_msg(answerMsg)
						answerMsg= answerMsg.format(commandMsg[1], commandMsg[2])

					except Exception as e:
						print(e)
						return

					##TENTA EXECUTAR COMANDO DO MYSQL
					print(answerMsg)
					try:
						eval(answerMsg)
						pass
					except Exception as e:
						print("there is an error! > " + e)
					pass

				else:
					return


			### IT´S A MSG
			else:
				answerMsg = self.database.searchMsg(mensagem_Lowercase, "dicionario", "key-answer")
				try:
					answerMsg = answerMsg[0][1]
				except Exception as e:
					answerMsg = ""

				if len(answerMsg)>1:
					self.Telegram_Bot.sendMessage(ChatId, answerMsg)
					print("Resposta encontrada Enviada para o chat:")
					print(answerMsg)

				else:
					if msg['chat']['username'] == 'GabrielGollo':
						answerMsg = "Resposta nao encontrada deseja adicionar uma?"
						print(answerMsg+"\n")
						self.Telegram_Bot.sendMessage(ChatId, answerMsg)

						self.Telegram_Bot.getUpdates()
						if msg['text'].lower() == 'sim':
							self.database.imprimir()

		else:
			print("FAILED TO CONNECT TO DATABASE")
			self.database.reconnect()
			self.received_msg(self, msg)
			return 0
			exit()

		self.database.close()
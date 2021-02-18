import telepot
from DBconnect import MyDatabase

class Telegram_MSG:
	def __init__(self, Telegram_Bot):
		self.database = MyDatabase()
		self.Telegram_Bot= Telegram_Bot
		self.connection = self.database.connected
		self.lastmsg={}

	def received_msg(self, msg):

		if self.connection:
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
				answerMsg = self.database.searchMsg(mensagem_Lowercase[0:], "commands", "comando")
				pass

			else: # IT´S A MSG
				answerMsg = self.database.searchMsg(mensagem_Lowercase, "dicionario", "key-answer")
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
			self.database.Reconnect()
		self.database.close()
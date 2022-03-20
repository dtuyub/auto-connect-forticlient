import imaplib
import email
import time
from config import Config
from email.header import decode_header

class MailMsg:
	def __init__(self, subject, sender):
		self.subject = subject
		self.sender = sender

class MailHelper:

	def get_messages(self):
		print("Creando conexión a cuenta de correo")
		client = self.create_imap_client()

		time.sleep(Config.mail_seconds_before_read)

		status, messages = client.select(Config.mail_folder_to_sniff)
		numer_of_messages = Config.mail_top_messages
		messages = int(messages[0])
		msgs = []

		print("Leyendo últimos {0} correos".format(numer_of_messages))
		for i in range(messages, messages-numer_of_messages, -1):
			res, msg = client.fetch(str(i), "(RFC822)")
			for response in msg:
				if isinstance(response, tuple):
					msg = email.message_from_bytes(response[1])
					subject, encoding = decode_header(msg["Subject"])[0]
					if isinstance(subject, bytes):
							subject = subject.decode(encoding)
					From, encoding = decode_header(msg.get("From"))[0]
					if isinstance(From, bytes):
						From = From.decode(encoding)
					msgs.append(MailMsg(subject, From))

		print("Cerrando conexión imap")
		client.close()
		client.logout()

		return msgs

	def create_imap_client(self):
		username = Config.mail_username
		password = Config.mail_password

		imap = imaplib.IMAP4_SSL(Config.mail_imap_server)
		imap.login(username, password)
		return imap

	def get_token(self):
		"""
		Retorna el token generado
		"""
		emails_founded = []
		token = ""

		while len(emails_founded)==0:

			print("Leyendo mensajes")
			messages = self.get_messages()
			emails_founded = list(filter(lambda m: m.sender == Config.mail_sender_name_filter, messages))
			
			if len(emails_founded) > 0:
				mail = emails_founded[0]
				token = mail.subject.split(' ')[1]
				
				print("Se encontró información de token. Valor: {0}".format(token))
				return token

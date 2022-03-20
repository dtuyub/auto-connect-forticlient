"""
Contiene información de la configuración global para la aplicación
"""
from dotenv import dotenv_values

original_config = dotenv_values(".env")

class Config:
	mail_username = original_config["MAIL_USERNAME"] or ""
	mail_password = original_config["MAIL_PASSWORD"] or ""
	mail_imap_server = original_config["MAIL_IMAP_SERVER"] or ""
	mail_sender_name_filter = original_config["MAIL_SENDER_NAME_FILTER"] or ""
	mail_top_messages = int(original_config["MAIL_TOP_MESSAGES"]) or 10
	mail_seconds_before_every_try = int(original_config["MAIL_SECONDS_BEFORE_EVERY_TRY"]) or 5
	mail_folder_to_sniff = original_config["MAIL_FOLDER_TO_SNIFF"] or "INBOX"
	mail_seconds_before_read = int(original_config["MAIL_SECONDS_BEFORE_READ"]) or 5
	exe_fortinet_dir = original_config["EXE_FORTINET_DIR"] or ""
	seconds_before_click_connect = int(original_config["SECONDS_BEFORE_CLICK_CONNECT"]) or 7

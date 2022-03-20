import time
from pywinauto import Application, findbestmatch
from bin.emailh import MailHelper
from config import Config

def openFortinet():
	try:
		app = Application("uia").connect(best_match="FortiClient")
	except findbestmatch.MatchError:
		app = Application("uia").start(Config.exe_fortinet_dir)

	wind = app.window(best_match="FortiClient")
	doc = wind.child_window(class_name="Chrome_RenderWidgetHostHWND")
	mail_helper = MailHelper()

	print("Click en conectar")
	doc.Connect.click()

	time.sleep(Config.seconds_before_click_connect)

	tokenEdit = wind.child_window(auto_id='vpn-token')
	okButton = wind.child_window(auto_id='vpn-ok-button')

	token = mail_helper.get_token()
	tokenEdit.set_text(token)

	okButton.click()
	print("Click en botón Ok")

	titleBar = wind.child_window(control_type="TitleBar")
	titleBar.Cerrar.click()
	print("Cerrando")

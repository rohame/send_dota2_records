import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(text):
 
	text+='\n\n\n\t抵制不良游戏，拒绝盗版游戏。\n\t注意自我保护，谨防受骗上当。\n\t适度游戏益脑，沉迷游戏伤身。\n\t合理安排时间，享受健康生活。'
	text+='\n\n\n Sent by python.'
	send_to=input('输入收件邮箱：')
	send_from=input('输入发件邮箱（163.com）：')
	passcode=input('输入密码：')
	msg = MIMEText(text, 'plain', 'utf-8')
	msg['Subject'] = Header('DOTA2 records', 'utf-8').encode()
	msg['from'] = send_from
	msg['to'] = send_to
	 
	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com", 25)
	smtp.set_debuglevel(1)
	 
	smtp.login(send_from, passcode)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.quit()
	print("MAIL SENT SUCCESS")

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(text):
 
	text+='\n\n\n\t抵制不良游戏，拒绝盗版游戏。\n\t注意自我保护，谨防受骗上当。\n\t适度游戏益脑，沉迷游戏伤身。\n\t合理安排时间，享受健康生活。'
	text+='\n\n\n Sent by python.'
	send_to=input('输入收件邮箱：')
	msg = MIMEText(text, 'plain', 'utf-8')
	msg['Subject'] = Header('DOTA2 records', 'utf-8').encode()
	msg['from'] = "rohame@163.com"
	msg['to'] = send_to
	 
	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com", 25)
	smtp.set_debuglevel(1)
	 
	smtp.login('rohame@163.com', 'L44o25V84e5')
	smtp.sendmail("rohame@163.com", send_to, msg.as_string())
	smtp.quit()
	print("MAIL SENT SUCCESS")
	
# ~ import smtplib
# ~ from email.mime.text import MIMEText
# ~ from email.header import Header
 
# ~ msg = MIMEText('Hi, this is a mail sent by python, thanks, bye!', 'plain', 'utf-8')
# ~ msg['Subject'] = Header('Python SMTP 测试', 'utf-8').encode()
# ~ msg['from'] = "rohame@163.com"
# ~ msg['to'] = '490001613@qq.com'
 
# ~ smtp = smtplib.SMTP()
# ~ smtp.connect("smtp.163.com", 25)
# ~ smtp.set_debuglevel(1)
 
# ~ smtp.login('rohame@163.com', 'L44o25V84e5')
# ~ smtp.sendmail("rohame@163.com", '490001613@qq.com', msg.as_string())
# ~ smtp.quit()
# ~ print("MAIL SENT SUCCESS")

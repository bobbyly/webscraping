import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
 
fromaddr = "bobby.ly@kmart.com.au"
toaddr = "bobby.ly@kmart.com.au"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test html email"
 
body = "will it html?"
msg.attach(MIMEText(body, 'plain'))
filepath = "\\\\cifs\\home\\bly6\\Signatures\\"
filename = "Signoff.txt"
attachment = open(filepath+filename, "r")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(fromaddr, input('pw: '))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


#!/usr/bin/python3
# Install required libraries

import smtplib
from datetime import datetime
from requests import get
import socket
import time
import os
from time import sleep
from string import Template
import set_time

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'tal.turtlebot.mail@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'djoryeuwpxxkklaq' #change this to match your gmail app-password

now = datetime.now()
current_time = now.strftime("%d/%m/%y %H:%M")

user_name = os.getlogin()

def is_connected():
  REMOTE_SERVER = "1.1.1.1"
  try:
    # See if we can resolve the host name - tells us if there is
    # A DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # Connect to the host - tells us if the host is actually reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except Exception:
     pass # We ignore any errors, returning False
  return False

class Emailer:
	def sendmail(self, recipient, subject, content):
		#Create Headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

	    	#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()

	    #Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

	    #Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit

class IP_print:

	def __init__(self, log):
		self.logger = log

	def get_external_ip(self):
		external_ip = get('https://api.ipify.org').content.decode('utf8')
		return external_ip

	def get_local_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			# doesn't even have to be reachable
			s.connect(('192.255.255.255', 1))
			IP = s.getsockname()[0]
		except:
			IP = '127.0.0.1'
		finally:
			s.close()
		return IP

	def get_ip(self):
		try:
			IP_local_addr = self.get_local_ip()
			IP_external_addr = self.get_external_ip()

			return IP_local_addr, IP_external_addr

		except Exception as e:
			self.logger.print("Error getting IP -")
			self.logger.print(e)
			# print("Quiting")
			# exit(1)
			return "", ""

class Log:
	def __init__(self, filename_path, filename_prefix, term_print = True):
		from datetime import datetime
		import os
		# home_folder = os.path.expanduser('~')
		home_folder = "/home/t-pi"
		log_folder = "{}/{}/{}".format(home_folder, filename_path, "logs")

		isExist = os.path.exists(log_folder)
		if not isExist:
			os.makedirs(log_folder)

		filename_full = str(datetime.now().strftime("{}/%y_%m_%d__%H_%M_{}.log".format(log_folder, filename_prefix)))
		print("Log file: {}".format(filename_full))

		self.file = open(filename_full, "w")
		self.term_print = term_print

	def write(self, data):
		self.file.write(data)
		self.file.flush()
		if self.term_print:
			print(data, end = ' ')

	def print(self, data, end = '\n', flush = True):
		self.write("{}{}".format(data, end))

	def close(self):
		print("Closing file.")
		self.file.close()

	def __del__(self):
		self.close()



def main():
	# first, check and update time
	internet_time = set_time.get_internet_time()
	if internet_time:
		system_time = set_time.get_system_time(internet_time)
		print("Internet time:", internet_time)
		print("System time:", system_time)
		if internet_time != system_time:
			set_time.update_system_time(internet_time)
		else:
			print("Failed to retrieve internet time.")
	
	logger = Log("scripts", "send_ip_2_email")
	logger.print("Ubuntu username:{}".format(user_name))

	start_time = time.time()
	logger.print('Waiting for internet connection ', end = " ", flush=True)

	while not is_connected():
		curr_time = time.time()
		time.sleep(1)
		logger.print(".", end = " ", flush=True)
	logger.print("Connected!\n")

	IP_class = IP_print(logger)
	IP_local, IP_external = "blank", "blank"
	# email_reason = "new connection"

	while (True):
		IP_local_new, IP_external_new = IP_class.get_ip()

		# logger.print('My public IP address is: {}'.format(IP_external))
		# logger.print('My local IP address is: {}\n'.format(IP_local))

		if IP_local != IP_local_new or IP_external != IP_external_new:

			if IP_local == "blank":
				email_reason = "new connection"
			else:
				email_reason = "IP changed"

			IP_local = IP_local_new
			IP_external = IP_external_new

			logger.print('Reason: {}'.format(email_reason))
			logger.print('My public IP address is: {}'.format(IP_external))
			logger.print('My local IP address is: {}\n'.format(IP_local))

			if IP_local != "" or IP_external != "":
				try:

					emailSubject = "TB3 IP:{} [{}]".format(IP_local, current_time)	
					emailContent_txt = '''
    <!DOCTYPE html>
    <html>
    <head>
        
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style type="text/css">
          h1{font-size:56px}
          h2{font-size:28px}
		  h3{font-size:28px;font-weight:bold}
		  t1{font-size:24px}
          p{font-weight:100}
          td{vertical-align:top}
          #email{margin:auto;width:1000px;background-color:#fff}
        </style>
		<style>
        	.tab {
            display: inline-block;
            margin-left: 40px;
        	}
    	</style>
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Georgia, serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#00A4BD" align="center" style="color: white;">
                    <h1> $TITLE </h1>
                </td>
        </table>
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>$TITLE_MSG</h2>
					<t1>
						<p>
							<br><strong>$IP_LOCAL</strong><span class="tab"></span><<span class="tab"></span> internal IP
							<br>$IP_EXTERNAL<span class="tab"></span><<span class="tab"></span> external IP
							<br><br>ssh t-pi@$IP_LOCAL
							<br><br>$CURR_TIME
							<br>Reason: $EMAIL_REASON
							</div>
							<br><br>
						</p>
					</t1>
					script file: $OS_PATH
                </td>
            </tr>
        </table>
    </div>
    </body>
    </html>
'''



					emailContentTemplate = Template(emailContent_txt)
					emailContent = emailContentTemplate.safe_substitute(TITLE='Hello !',
														 TITLE_MSG="This is an automated email from Raspberry Pi",
														 IP_LOCAL=IP_local,
														 IP_EXTERNAL=IP_external,
														 CURR_TIME=current_time,
														 EMAIL_REASON=email_reason,
														 OS_PATH=os.path.abspath(__file__))

					#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
					sendTo = 'talzoor@gmail.com'
					sender = Emailer()
					sender.sendmail(sendTo, emailSubject, emailContent)

					logger.print("email sent!\n")

					#sendTo = 'kashim@post.bgu.ac.il'
					#sender = Emailer()
					#sender.sendmail(sendTo, emailSubject, emailContent)


				except Exception as e:
					logger.print("Error sending email -")
					logger.print(e)
					# print("Quiting")
					# exit(1)
		sleep(10)

	logger.print("Done.")

if __name__ == "__main__":
	main()

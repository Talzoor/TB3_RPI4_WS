#!/usr/bin/python3
# Install required libraries

import smtplib
from datetime import datetime
from requests import get
import socket
import time
import os
from time import sleep

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
	logger = Log("scripts", "send_ip_2_email")
	logger.print("Ubuntu username:{}".format(user_name))

	start_time = time.time()
	logger.print('Waiting for internet connection ', end = " ", flush=True)

	while not is_connected():
		curr_time = time.time()
		# if curr_time - start_time > 60:
			# print("Error getting IP. Network down. quiting!")
			# exit(1)
			# break
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
					emailContent = "<div style=""font-size:30px; padding:0 10px;"">" \
								+ "<br><strong>{}</strong> \t\t<\t internal IP".format(IP_local) \
								+ "<br>{} \t\t<\t external IP".format(IP_external) \
								+ "<br>ssh t-pi@{}".format(IP_local) \
								+ "<br><br>{}".format(current_time) \
								+ "<br>Reason: {}".format(email_reason) \
								+ "</div>" \
								+ "<br><br>script file:	{}".format(os.path.abspath(__file__)) \
								+ " "
								# + "ssh {}@{}".format(user_name, IP_local)

					#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
					sendTo = 'talzoor@gmail.com'
					sender = Emailer()
					sender.sendmail(sendTo, emailSubject, emailContent)

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

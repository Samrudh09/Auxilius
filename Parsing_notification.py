from datetime import *
import time 
import pandas as pd 
df=pd.read_csv('user_input_pres.csv')
# print df['name']
reg_date=[]
exp_date=[]
name=[]
frq=[]
med_name=[]
med_notif=[]
FMT = '%d:%m:%Y:%H'

def data_parser(x1,x2,x3,x4,x5):
	for _ in x1:
		 reg_date.append(datetime.strptime(_, FMT))
	for _ in x2:
		 exp_date.append(datetime.strptime(_, FMT))
	for _ in x3:
		name.append(_)
	for _ in x4:
		frq.append(_)
	for _ in x5:
		med_name.append(_)
	for i in range(len(exp_date)):
		notif_time=exp_date[i]-reg_date[i]
		med_notif.append(notif_time)

def sim():
	start_t=time.time()
	end_t=start_t+10
	print start_t,end_t
	while 1:
		if time.time()==end_t:
			print "now"
			send_email('auxiliusnotification1@gmail.com','','auxiliusnotification1@gmail.com','Test','Testing')


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


data_parser(df['reg_date'],df['exp_date'],df['name'],df['frq'],df['med_name'])
sim()







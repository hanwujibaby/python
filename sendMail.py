#! /usr/local/bin/python2.7
#coding: UTF-8
import os
import sys
import MySQLdb
import datetime
import smtplib  
from email.MIMEText import MIMEText  
from email.Header import Header  

today=datetime.date.today()
deltaDay=datetime.timedelta(days=1)
yesterday=today-deltaDay

IOSFORMAT='%Y-%m-%d'
print today.strftime(IOSFORMAT)
print yesterday.strftime(IOSFORMAT)

db = MySQLdb.connect("$ip","username","password","dbname",charset="utf8")
cursor = db.cursor()
sql=""
s=cursor.execute(sql)
result=cursor.fetchone()
tcount=result[0]

sql=""
s=cursor.execute(sql)
count=cursor.fetchone()
vcount=count[0]


sender = 'sss@163.com'  
receiver = 'ss@socom'  
subject = 'subetc'  
smtpserver = 'smtp.163.com'  
username = 'wei4liverss@163.com'  
password = 'ss'  
  
msg = MIMEText('完成任务数：'+str(tcount)+'\n覆盖视频数：'+str(vcount),'plain','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

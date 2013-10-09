#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import smtplib
import time

def send_mail(name, phoneNumber, messageReal, clientGmail, clientPassword):
 sender = name
 receivers = [phoneNumber+'@vtext.com', phoneNumber+'@txt.att.net', phoneNumber+'messaging.sprintpcs.com', phoneNumber+'tmomail.net']
 message = messageReal

 if(clientGmail=="" and clientPassword==""):  
  try:
   server = smtplib.SMTP('smtp.gmail.com:587')  
   server.starttls()  
   server.login('email','password')  
   server.sendmail(sender, receivers, message)  
   server.quit()        
   print 'Successfully sent message'

  except smtplib.SMTPException:
   print "Error: cant send email"

 else:
  try:
   server = smtplib.SMTP('smtp.gmail.com:587')  
   server.starttls()  
   server.login(clientGmail,clientPassword)  
   server.sendmail(sender, receivers, message)  
   server.quit()        
   print 'Successfully sent email'

  except smtplib.SMTPException:
   print "Error: cant send email"

print "Process initialization: successful";
while(True):
 try:
  con = mdb.connect  ("host name","userName","password","databaseName");

  cur = con.cursor()
  cur.execute("SELECT * FROM clients")

  rows=cur.fetchall()

  for row in rows:
   send_mail(row[0], row[1], row[2], row[3], row[4])
   query="DELETE FROM clients WHERE name='"+row[0]+"'"
   cur.execute(query)


    
 except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

 time.sleep(10)


    


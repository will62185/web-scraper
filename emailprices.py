# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 17:27:28 2019

@author: srada
"""
import smtplib
import os
from datetime import date

today = date.today()
today = today.strftime("%d/%m/%Y")


def emailprices(df):
    #sets the username and password as environment variables... do this outside of this program
    #os.environ['username'] = ''
    #os.environ['password'] = ''
    #get the username and password from the environment variables
    user = os.getenv('username')
    password = os.getenv('password')
    
    FROM = user
    TO = ''
    #Sets teh subject of the email
    SUBJECT = "Prices - " + today
    #Sets the passed in dataframes as the body of the message
    TEXT = df
    
    #Connects to the google server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #Connects to the server using credentials
    server.login(user, password)
    #Sends the email
    server.sendmail(
      FROM, 
      TO, 
      'Subject: {}\n\n{}'.format(SUBJECT, TEXT))
    #quits the server
    server.quit()      
   
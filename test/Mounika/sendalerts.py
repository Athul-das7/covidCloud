import sendMail   #file form athul->test->sendmail to send alert
from chcking import *   #file from athul->test->chcking after validation of roll no
# noinspection PyUnresolvedReferences
import smtplib as sl
roll_no  #= function to get roll no in string format
temp   #= t0 get temp from the file which scans temp

if(temp>98.6)
    #create a class instantiate
    # in file sendMail put the whole code under a function so that this function can send roll no. as parameter
    #  def  sendmail(roll)   # the roll to whom to be sent
    #  this will call that - sendmail(roll_no+"@vce.ac.in")  and mail is sent
# to send urgent alerts  this program can be written while getting temp from scanner and checking at that instant
#to send mail
# another file for weekly_alerts will be written


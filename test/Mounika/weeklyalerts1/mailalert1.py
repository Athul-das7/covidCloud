import smtplib as sl

def send_alert(row):
    smtpobj = sl.SMTP('smtp-mail.outlook.com', 587)
    print(smtpobj.ehlo())  # this establishes the connection with the server
    print(smtpobj.starttls())  # this start the ttls encryption in the server
    pswd = input("enter password")
    print(smtpobj.login('1602-19-735-091@vce.ac.in', pswd))  # login in to the smtp server
    print(row)
    print(type(row))
    SUBJECT = 'weekly report'
    TEXT = f''' Hi {row[0]}\nReport for this week \nday1: {row[2]} celcius , day2: {row[3]} celcius, day3: {row[4]} celcius,
                    day4: {row[5]} celcius, day5: {row[6]} celcius, day6: {row[7]} celcius, day7: {row[8]} celcius
    '''  # body of the mail

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

    smtpobj.sendmail('1602-19-735-091@vce.ac.in', row[1], message)
    # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body

    smtpobj.quit()  # quiting the smtp server and deleting the object
# mail must be sent from the newly created google account


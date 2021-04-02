import smtplib as sl

def send_alert(row):
    #smtpobj = sl.SMTP('smtp.gmail.com', 465)
    #smtpobj = sl.SMTP('smtp-mail.outlook.com', 587)
    smtpobj = sl.SMTP_SSL('smtp.gmail.com', 465)
    print(smtpobj.ehlo())  # this establishes the connection with the server
    #print(smtpobj.starttls())  # this start the ttls encryption in the server
    pswd = input("enter password")
    print(smtpobj.login('covidCloudmp@gmail.com', pswd))  # login in to the smtp server
    SUBJECT = 'weekly report'
    TEXT = f''' Hi {row[0]}\nReport for this week \nday1: {row[2]} celcius , day2: {row[3]} celcius, day3: {row[4]} celcius,
                    day4: {row[5]} celcius, day5: {row[6]} celcius, day6: {row[7]} celcius, day7: {row[8]} celcius
    '''  # body of the mail

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  # concating the strings using string formatting

    smtpobj.sendmail('covidCloudmp@gmail.com', row[1], message)
    # sending the mail from us to the reciever; 071 = user; 091 = reciever; message = subject + body

    smtpobj.quit()  # quiting the smtp server and deleting the object
# mail must be sent from the newly created google account


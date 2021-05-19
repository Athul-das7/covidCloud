import threading
import prototypeRasp as p
import prototypeCloud as pc
import time
import gui3 as G

pastTime = round(time.time())
while True:      #It must always run
    test = p.covidCloud()
    test1 = pc.cloudPrediction()
    testgui=G.details()
    testgui.message1()
    rnum = test.readBarcode()       #the rollno must be entered in the terminal
    print(rnum)
    test.checkRollNo(rnum)
    detail=test.readDbms(rnum)
    print(detail)

    nowTime = round(time.time())   #for the sending data to gss
    if nowTime - pastTime >= 30*60:
        t2 = threading.Thread(target=test.sendArrangeData)
        t2.start()
        pastTime = round(time.time())
        nowTime = round(time.time())

    print("media\\{}".format(detail[4]))
    print(f'Name:  {detail[1]}\nRoll No.:  {detail[0]}\nBranch:  {detail[2]} {detail[3]}')
    testgui.det_image(detail)

    time.sleep(3)
    ckdis = False
    dist = 2.00
    temp=0
    while ckdis!=True:
        dist = test.readDistance()

        print(dist, " cm")
        ckdis = test.checkDistance(dist)
        if ckdis == True:
            temp=test.readTemperature()
            with open('TempRoll.txt', 'a') as f:  # saves the student data in TempRoll.txt
                f.write(f'{rnum}: {temp}\n')
            print(test.checkTemperature(temp))
            testgui.det_temp(detail, temp)
            if temp > 100:  #sending mail sms and playing alarm if temp greater than 100
                t1 = threading.Thread(target=test.mailandsms, args=(rnum, temp))
                t1.start()
                test.Alarm()
                # self.sendMail(rn,temp)
                # self.sendSMS(rn,temp)
                #t1.join()
                print('Alarm mail and sms sent')


        else:
            testgui.message3()
            print(" please put your hand closer to the sensor")
            time.sleep(2)
            continue

    print("media\\{}".format(detail[4]))
    print(f'Name:  {detail[1]}\nRoll No.:  {detail[0]}\nBranch:  {detail[2]} {detail[3]}')
#    testgui.det_image(detail)



    print(temp)
# test1.predict()

# # det=['1602-19-735-071', 'KUMARANKANDATH ATHUL DAS', 'ECE', 'B', 'media\\71.jpg']
# from time import sleep
# import threading
# from tkinter import *
#
# serialdata = []
# data = True
#
# class SensorThread(threading.Thread):
#     def run(self):
#         try:
#             i = 0
#             while True:
#                 serialdata.append("Hello %d" % i)
#                 i += 1
#                 sleep(1)
#         except KeyboardInterrupt:
#             exit()
#
# class Gui(object):
#     def __init__(self):
#         self.root = Tk()
#         self.lbl = Label(self.root, text="")
#         self.updateGUI()
#         self.readSensor()
#
#     def run(self):
#         self.lbl.pack()
#         self.lbl.after(1000, self.updateGUI)
#         self.root.mainloop()
#
#     def updateGUI(self):
#         msg = "Data is True" if data else "Data is False"
#         self.lbl["text"] = msg
#         self.root.update()
#         self.lbl.after(1000, self.updateGUI)
#
#     def readSensor(self):
#         self.lbl["text"] = serialdata[-1]
#         self.root.update()
#         self.root.after(527, self.readSensor)
#
# if __name__ == "__main__":
#     SensorThread().start()
#     Gui().run()
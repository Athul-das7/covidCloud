import prototypeRasp as p
import prototypeCloud as pc
import time
import gui3 as G

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
    # print("D:\\CovidCloud_project\\covidCloud\\main\\prototype\\media\\{}".format(detail[4]))
    print(f'Name:  {detail[1]}\nRoll No.:  {detail[0]}\nBranch:  {detail[2]} {detail[3]}')
    testgui.det_image(detail)

    test = p.covidCloud()
    test1 = pc.cloudPrediction()
    testgui=G.details()
    testgui.message1()
    rnum = test.readBarcode()       #the rollno must be entered in the terminal
    print(rnum)
    test.checkRollNo(rnum)
    detail=test.readDbms(rnum)
    print(detail)
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
            testgui.det_temp(detail,temp)
            print(test.checkTemperature(temp))
            if test.checkTemperature(temp):
                print("Hello world")
        else:
            testgui.message3()
            print(" please put your hand closer to the sensor")
            time.sleep(2)
            continue

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
            testgui.det_temp(detail,temp)
            print(test.checkTemperature(temp))
            if test.checkTemperature(temp):
                print("Hello world")
        else:
            testgui.message3()
            print(" please put your hand closer to the sensor")
            time.sleep(2)
            continue

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
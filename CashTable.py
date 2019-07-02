import time
import threading

dataArr=[]
timeArr=[]
boolArr=[]
class MyThread(threading.Thread):
    def run(self):
        #print("thread started")
        i= len(dataArr)-1
        time.sleep(timeArr[i])
        boolArr[i]=False
        #print("an item has been expired")

while True:
    i=int(input("please choose one \n1. enter new val \n2. check for old val \n3. exit"))
    if i==1:
        dataArr.append(input("enter a value"))
        timeArr.append(float(input("enter time")))
        boolArr.append(True)
        thr=MyThread()
        thr.start()
        continue
    elif i==2:
        data=input("enter a value")
        if data in dataArr:
            if boolArr[dataArr.index(data)]:
                print("item  exist ")
            else:
                print("item expired")
        else:
            print("item not exist")
    elif i==3:
        break
    else:
        print("pls try again")


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

def addCash(v,t):
    dataArr.append(v)
    timeArr.append(t)
    boolArr.append(True)
    thr = MyThread()
    thr.start()
def CheckCash(data):
    if data in dataArr:
        if boolArr[dataArr.index(data)]:
            return "item  exist "
        else:
            return "item expired"
    else:
        return "item not exist"
if __name__ == '__main__':
    while True:
        i = int(input("please choose one \n1. enter new val \n2. check for old val \n3. exit"))
        if i == 1:
            addCash(input("enter a value"), float(input("enter time")))
        elif i == 2:
            data = input("enter a value")
            print(CheckCash(data))

        elif i == 3:
            break
        else:
            print("pls try again")


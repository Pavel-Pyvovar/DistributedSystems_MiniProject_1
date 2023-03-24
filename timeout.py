import threading
import time

class Demo:
    def __init__(self):
        self._KillTask = False

    def OnTimeout(self):
        self._KillTask = True
        print("Timeout!")
    
    def Counter(self,timeout):
        print("Counter() starts!")
        totalSleepTime = 0
        while(self._KillTask is False):
            totalSleepTime = totalSleepTime + 1
            time.sleep(1)
            if totalSleepTime == timeout:
                self.OnTimeout()
    
    def Function(self):
        while self._KillTask is False:
            #do any logic here
            print("Function is running till it timeout..")
            time.sleep(0.5) #  just a demo delay for the printed log on the terminal 
        print("Function() timed out!")
        self._KillTask = True


if __name__=='__main__':
    ## Main starts here
    print("Demo for Timeout - by Omar")
    Obj = Demo()
    
    ## Start thread2 
    thread2 = threading.Thread(target = Obj.Counter, args =(10,))
    try:
        thread2.start()
    except Exception:
        print ("Error Starting the Thread")
    
    ## Proceed with the logic of thread 1 -(Main thread)
    Obj.Function()
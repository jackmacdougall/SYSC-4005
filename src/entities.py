import simpy
import random
from simpy.resources import container
import rng
import threading

queueC1W1WaitTimeList = []
queueC1W2WaitTimeList = []
queueC1W3WaitTimeList = []
queueC2W2WaitTimeList = []
queueC3W3WaitTimeList = []

queueC1W1WaitToggle = True
queueC1W1StartTime1 = 0.0
queueC1W1StartTime2 = 0.0
queueC1W1ArrivalCount = 0

queueC1W2WaitToggle = True
queueC1W2StartTime1 = 0.0
queueC1W2StartTime2 = 0.0
queueC1W2ArrivalCount = 0

queueC1W3WaitToggle = True
queueC1W3StartTime1 = 0.0
queueC1W3StartTime2 = 0.0
queueC1W3ArrivalCount = 0

queueC2W2WaitToggle = True
queueC2W2StartTime1 = 0.0
queueC2W2StartTime2 = 0.0
queueC2W2ArrivalCount = 0

queueC3W3WaitToggle = True
queueC3W3StartTime1 = 0.0
queueC3W3StartTime2 = 0.0
queueC3W3ArrivalCount = 0




class Inspector1:
    
    def __init__(self, env, station1, station2, station3):
        self.env = env
        self.name = "Inspector 1"
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.systemTime = 0.0
        self.blockTime = 0.0
        self.componentCount = 0
        self.arrivalCount = 0
        self.isWorkstation = False
        self.action = env.process(self.run())
             
    def run(self):
        global queueC1W1WaitToggle, queueC1W1StartTime1, queueC1W1StartTime2, queueC1W1ArrivalCount 
        global queueC1W2WaitToggle, queueC1W2StartTime1, queueC1W2StartTime2, queueC1W2ArrivalCount
        global queueC1W3WaitToggle, queueC1W3StartTime1, queueC1W3StartTime2, queueC1W3ArrivalCount
        while True: 
            serviceTime = rng.inspector1_component1_rng()
            self.arrivalCount += 1
            yield self.env.timeout(float(serviceTime))
            self.systemTime += float(serviceTime)
            self.componentCount = self.componentCount + 1
            print("Inspector 1 finished assembling component 1")
            if self.station1.buffer1.level <= self.station2.buffer1.level and self.station1.buffer1.level <= self.station3.buffer1.level:
                yield self.station1.buffer1.put(1)
                if queueC1W1WaitToggle:
                    queueC1W1StartTime1 = self.env.now
                    queueC1W1WaitToggle = False
                else:
                    queueC1W1StartTime2 = self.env.now
                    queueC1W1WaitToggle = True
                queueC1W1ArrivalCount += 1
                print("Component 1 sent to Workstation 1")
            elif self.station2.buffer1.level <= self.station3.buffer1.level:
                yield self.station2.buffer1.put(1)              
                if queueC1W2WaitToggle:
                    queueC1W2StartTime1 = self.env.now
                    queueC1W2WaitToggle = False
                else:
                    queueC1W2StartTime2 = self.env.now
                    queueC1W2WaitToggle = True    
                queueC1W2ArrivalCount += 1
                print("Component 1 sent to Workstation 2")
            else:
                yield self.station3.buffer1.put(1)
                if queueC1W3WaitToggle:
                    queueC1W3StartTime1 = self.env.now
                    queueC1W3WaitToggle = False
                else:
                    queueC1W3StartTime2 = self.env.now
                    queueC1W3WaitToggle = True
                queueC1W3ArrivalCount += 1
                print("Component 1 sent to Workstation 3")
        
        
class Inspector2:
    
    def __init__(self, env, station2, station3):
        self.env = env
        self.name = "Inspector 2"
        self.station2 = station2
        self.station3 = station3
        self.systemTime = 0.0
        self.blockTime = 0.0
        self.componentCount = 0
        self.arrivalCount = 0
        self.isWorkstation = False
        self.action = env.process(self.run())
        
    def run(self):
        global queueC2W2WaitToggle, queueC2W2StartTime1, queueC2W2StartTime2, queueC2W2ArrivalCount
        global queueC3W3WaitToggle, queueC3W3StartTime1, queueC3W3StartTime2, queueC3W3ArrivalCount
        while True:
            if (random.randint(2, 3) == 2):
                serviceTime = rng.inspector2_component2_rng()
                self.arrivalCount += 1   
                yield self.env.timeout(float(serviceTime))
                self.systemTime += float(serviceTime)
                self.componentCount = self.componentCount + 1
                print("Inspector 2 finished assembling component 2") 
                yield self.station2.buffer2.put(1)
                if queueC2W2WaitToggle:
                    queueC2W2StartTime1 = self.env.now
                    queueC2W2WaitToggle = False
                else:
                    queueC2W2StartTime2 = self.env.now
                    queueC2W2WaitToggle = True        
                queueC2W2ArrivalCount += 1
                print("Component 2 sent to Workstation 2")
            else:
                serviceTime = rng.inspector2_component3_rng()
                self.arrivalCount = self.arrivalCount + 1   
                yield self.env.timeout(float(serviceTime))
                self.systemTime += float(serviceTime)
                self.componentCount = self.componentCount + 1
                print("Inspector 2 finished assembling component 3") 
                yield self.station3.buffer3.put(1)
                if queueC3W3WaitToggle:
                    queueC3W3StartTime1 = self.env.now
                    queueC3W3WaitToggle = False
                else:
                    queueC3W3StartTime2 = self.env.now
                    queueC3W3WaitToggle = True 
                queueC3W3ArrivalCount += 1
                print("Component 3 sent to Workstation 3")
               
        
class Workstation1:
    
    def __init__(self, env):
        global queueC1W1WaitToggle, queueC1W1StartTime1, queueC1W1StartTime2      
        self.env = env
        self.name = "Workstation 1"
        self.product = "P1"
        self.buffer1 = container.Container(self.env, 2)
        self.productCount = 0
        self.arrivalCount = 0
        self.componentCount = 0
        self.systemTime = 0.0
        self.waitTime = 0.0
        self.isWorkstation = True
        self.action = env.process(self.run())
    
    def run(self):
        global queueC1W1WaitToggle, queueC1W1StartTime1, queueC1W1StartTime2       
        while True:
            yield self.buffer1.get(1)
            if queueC1W1WaitToggle:
                queueC1W1WaitTimeList.append(self.env.now - queueC1W1StartTime2)          
            else:      
                queueC1W1WaitTimeList.append(self.env.now - queueC1W1StartTime1)    
                queueC1W1WaitToggle = True
                
            print("Workstation 1 recieved required components")
            self.componentCount = self.componentCount + 1
            serviceTime = rng.workstation1_rng()   
            self.arrivalCount = self.arrivalCount + 1    
            yield self.env.timeout(float(serviceTime))
            self.productCount = self.productCount + 1
            self.systemTime += float(serviceTime)
            print("Workstation 1 finished assembling product 1")
        

class Workstation2:
    def __init__(self, env):
        self.env = env
        self.name = "Workstation 2"
        self.product = "P2"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer2 = container.Container(self.env, 2)
        self.productCount = 0
        self.arrivalCount = 0
        self.componentCount = 0
        self.systemTime = 0.0
        self.waitTime = 0.0
        self.isWorkstation = True
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            yield self.env.process(self.C1W2Process()) & self.env.process(self.C2W2Process())
            print("Workstation 2 recieved required components")
            
            serviceTime = rng.workstation2_rng()
            
            yield self.env.timeout(float(serviceTime))
            self.productCount = self.productCount + 1
            print("Workstation 2 finished assembling product 2")         
 
    def C1W2Process(self):
        global queueC1W2WaitToggle, queueC1W2StartTime1, queueC1W2StartTime2 
        yield self.buffer1.get(1)
        if queueC1W2WaitToggle:
            queueC1W2WaitTimeList.append(self.env.now - queueC1W2StartTime2)          
        else:      
            queueC1W2WaitTimeList.append(self.env.now - queueC1W2StartTime1)    
            queueC1W2WaitToggle = True     
                        
    def C2W2Process(self):
        global queueC2W2WaitToggle, queueC2W2StartTime1, queueC2W2StartTime2
        yield self.buffer2.get(1)
        if queueC2W2WaitToggle:
            queueC2W2WaitTimeList.append(self.env.now - queueC2W2StartTime2)          
        else:      
            queueC2W2WaitTimeList.append(self.env.now - queueC2W2StartTime1)    
            queueC2W2WaitToggle = True 
            
            
class Workstation3:
    def __init__(self, env):
        self.env = env
        self.name = "Workstation 3"
        self.product = "P3"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer3 = container.Container(self.env, 2)
        self.productCount = 0
        self.systemTime = 0.0
        self.waitTime = 0.0
        self.arrivalCount = 0
        self.componentCount = 0
        self.isWorkstation = True
        self.action = env.process(self.run())
        
    def run(self):
        while True:
            yield self.env.process(self.C1W3Process()) & self.env.process(self.C3W3Process())
       
            print("Workstation 3 recieved required components")
                
            serviceTime = rng.workstation3_rng()   
                        
            yield self.env.timeout(float(serviceTime))
            self.productCount = self.productCount + 1
            print("Workstation 3 finished assembling product 3")  
                    
    def C1W3Process(self):
        global queueC1W3WaitToggle, queueC1W3StartTime1, queueC1W3StartTime2
        yield self.buffer1.get(1)
        if queueC1W3WaitToggle:
            queueC1W3WaitTimeList.append(self.env.now - queueC1W3StartTime2)          
        else:      
            queueC1W3WaitTimeList.append(self.env.now - queueC1W3StartTime1)    
            queueC2W2WaitToggle = True     
        
    def C3W3Process(self):
        global queueC3W3WaitToggle, queueC3W3StartTime1, queueC3W3StartTime2
        yield self.buffer3.get(1)
        if queueC3W3WaitToggle:
            queueC3W3WaitTimeList.append(self.env.now - queueC3W3StartTime2)          
        else:      
            queueC3W3WaitTimeList.append(self.env.now - queueC3W3StartTime1)    
            queueC3W3WaitToggle = True   
            

     
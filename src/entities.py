import simpy
import random
from simpy.resources import container
import rng
import threading
import sim

queueC1W1WaitTimeList = []
queueC1W2WaitTimeList = []
queueC1W3WaitTimeList = []
queueC2W2WaitTimeList = []
queueC3W3WaitTimeList = []

queueC1W1CapacityList = []
queueC1W2CapacityList = []
queueC1W3CapacityList = []
queueC2W2CapacityList = []
queueC3W3CapacityList = []

queueC1W1WaitToggle = True
queueC1W1StartTime1 = 0.0
queueC1W1StartTime2 = 0.0
queueC1W1ArrivalCount = 0
queueC1W1DepartureCount = 0
queueC1W1CapacityStart = 0.0

queueC1W2WaitToggle = True
queueC1W2StartTime1 = 0.0
queueC1W2StartTime2 = 0.0
queueC1W2ArrivalCount = 0
queueC1W2DepartureCount = 0
queueC1W2CapacityStart = 0.0

queueC1W3WaitToggle = True
queueC1W3StartTime1 = 0.0
queueC1W3StartTime2 = 0.0
queueC1W3ArrivalCount = 0
queueC1W3DepartureCount = 0
queueC1W3CapacityStart = 0.0

queueC2W2WaitToggle = True
queueC2W2StartTime1 = 0.0
queueC2W2StartTime2 = 0.0
queueC2W2ArrivalCount = 0
queueC2W2DepartureCount = 0
queueC2W2CapacityStart = 0.0

queueC3W3WaitToggle = True
queueC3W3StartTime1 = 0.0
queueC3W3StartTime2 = 0.0
queueC3W3ArrivalCount = 0
queueC3W3DepartureCount = 0
queueC3W3CapacityStart = 0.0

initialize_time = 175.0


class Inspector1:
    
    def __init__(self, env, station1, station2, station3):
        self.env = env
        self.name = "Inspector 1"
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.systemTime = 0.0
        self.idleTime = 0.0
        self.componentCount = 0
        self.arrivalCount = 0
        self.isWorkstation = False
        self.action = env.process(self.run())
             
    def run(self):
        global queueC1W1WaitToggle, queueC1W1StartTime1, queueC1W1StartTime2, queueC1W1ArrivalCount, queueC1W1CapacityList, queueC1W1CapacityStart
        global queueC1W2WaitToggle, queueC1W2StartTime1, queueC1W2StartTime2, queueC1W2ArrivalCount, queueC1W2CapacityList, queueC1W2CapacityStart
        global queueC1W3WaitToggle, queueC1W3StartTime1, queueC1W3StartTime2, queueC1W3ArrivalCount, queueC1W3CapacityList, queueC1W3CapacityStart
        
        queueC1W1CapacityStart = self.env.now
        queueC1W2CapacityStart = self.env.now
        queueC1W3CapacityStart = self.env.now
        while True:  
            serviceTime = rng.inspector1_component1_rng()
            if(initializeCheck(self)):
                self.arrivalCount += 1
            yield self.env.timeout(float(serviceTime))
            self.systemTime += float(serviceTime)
            if(initializeCheck(self)):
                self.componentCount = self.componentCount + 1
            print("Inspector 1 finished assembling component 1")
            if self.station1.buffer1.level <= self.station2.buffer1.level and self.station1.buffer1.level <= self.station3.buffer1.level:
                idle1Start = self.env.now
                yield self.station1.buffer1.put(1)
                if(initializeCheck(self)):
                    self.idleTime += self.env.now - idle1Start
                    if(self.station1.buffer1.level == 0):
                        queueC1W1CapacityList.append(tuple((self.station1.buffer1.level,self.env.now - queueC1W1CapacityStart, "put")))
                    else:
                        queueC1W1CapacityList.append(tuple((self.station1.buffer1.level - 1, self.env.now - queueC1W1CapacityStart, "put")))
                if queueC1W1WaitToggle:
                    queueC1W1StartTime1 = self.env.now
                    queueC1W1WaitToggle = False
                else:
                    queueC1W1StartTime2 = self.env.now
                    queueC1W1WaitToggle = True
                if(initializeCheck(self)):
                    queueC1W1ArrivalCount += 1
                queueC1W1CapacityStart = self.env.now
                print("Component 1 sent to Workstation 1")
            elif self.station2.buffer1.level <= self.station3.buffer1.level:
                idle2Start = self.env.now
                yield self.station2.buffer1.put(1)
                if(initializeCheck(self)):
                    self.idleTime += self.env.now - idle2Start
                    if(self.station2.buffer1.level == 0):
                        queueC1W2CapacityList.append(tuple((self.station2.buffer1.level, self.env.now - queueC1W2CapacityStart, "put")))
                    else:
                        queueC1W2CapacityList.append(tuple((self.station2.buffer1.level - 1, self.env.now - queueC1W2CapacityStart, "put")))
                if queueC1W2WaitToggle:
                    queueC1W2StartTime1 = self.env.now
                    queueC1W2WaitToggle = False
                else:
                    queueC1W2StartTime2 = self.env.now
                    queueC1W2WaitToggle = True 
                if(initializeCheck(self)):
                    queueC1W2ArrivalCount += 1
                queueC1W2CapacityStart = self.env.now
                print("Component 1 sent to Workstation 2")
            else:
                idle3Start = self.env.now
                yield self.station3.buffer1.put(1)
                if(initializeCheck(self)):
                    self.idleTime += self.env.now - idle3Start
                    if(self.station3.buffer1.level == 0):
                        queueC1W3CapacityList.append(tuple((self.station3.buffer1.level, self.env.now - queueC1W3CapacityStart, "put")))
                    else:
                        queueC1W3CapacityList.append(tuple((self.station3.buffer1.level - 1, self.env.now - queueC1W3CapacityStart, "put")))
                if queueC1W3WaitToggle:
                    queueC1W3StartTime1 = self.env.now
                    queueC1W3WaitToggle = False
                else:
                    queueC1W3StartTime2 = self.env.now
                    queueC1W3WaitToggle = True
                if(initializeCheck(self)):
                    queueC1W3ArrivalCount += 1
                queueC1W3CapacityStart = self.env.now
                print("Component 1 sent to Workstation 3")
        
        
class Inspector2:
    
    def __init__(self, env, station2, station3):
        self.env = env
        self.name = "Inspector 2"
        self.station2 = station2
        self.station3 = station3
        self.systemTime = 0.0
        self.idleTime = 0.0
        self.component2Count = 0
        self.component3Count = 0
        self.arrivalCount = 0
        self.isWorkstation = False
        self.action = env.process(self.run())
        
    def run(self):
        global queueC2W2WaitToggle, queueC2W2StartTime1, queueC2W2StartTime2, queueC2W2ArrivalCount, queueC2W2CapacityList, queueC2W2CapacityStart
        global queueC3W3WaitToggle, queueC3W3StartTime1, queueC3W3StartTime2, queueC3W3ArrivalCount, queueC3W3CapacityList, queueC3W3CapacityStart
        
        queueC2W2CapacityStart = self.env.now
        queueC3W3CapacityStart = self.env.now
        while True:
            if (random.randint(2, 3) == 2):
                serviceTime = rng.inspector2_component2_rng()
                if(initializeCheck(self)):
                    self.arrivalCount += 1   
                yield self.env.timeout(float(serviceTime))
                self.systemTime += float(serviceTime)
                if(initializeCheck(self)):
                    self.component2Count += 1
                print("Inspector 2 finished assembling component 2") 
                idleC2Start = self.env.now
                yield self.station2.buffer2.put(1)
                if(initializeCheck(self)):
                    self.idleTime += self.env.now - idleC2Start
                    if(self.station2.buffer2.level == 0):
                        queueC2W2CapacityList.append(tuple((self.station2.buffer2.level, self.env.now - queueC2W2CapacityStart, "put")))
                    else:
                        queueC2W2CapacityList.append(tuple((self.station2.buffer2.level - 1, self.env.now - queueC2W2CapacityStart, "put")))
                if queueC2W2WaitToggle:
                    queueC2W2StartTime1 = self.env.now
                    queueC2W2WaitToggle = False
                else:
                    queueC2W2StartTime2 = self.env.now
                    queueC2W2WaitToggle = True    
                if(initializeCheck(self)):
                    queueC2W2ArrivalCount += 1
                print("Component 2 sent to Workstation 2")
                queueC2W2CapacityStart = self.env.now
            else:
                serviceTime = rng.inspector2_component3_rng()
                if(initializeCheck(self)):
                    self.arrivalCount = self.arrivalCount + 1   
                yield self.env.timeout(float(serviceTime))      
                self.systemTime += float(serviceTime)
                if(initializeCheck(self)):
                    self.component3Count += 1
                print("Inspector 2 finished assembling component 3") 
                idleC3Start = self.env.now
                yield self.station3.buffer3.put(1)
                if(initializeCheck(self)):
                    self.idleTime += self.env.now - idleC3Start
                    if(self.station3.buffer3.level == 0):          
                        queueC3W3CapacityList.append(tuple((self.station3.buffer3.level, self.env.now - queueC3W3CapacityStart, "put")))
                    else:
                        queueC3W3CapacityList.append(tuple((self.station3.buffer3.level - 1, self.env.now - queueC3W3CapacityStart, "put")))
                if queueC3W3WaitToggle:
                    queueC3W3StartTime1 = self.env.now
                    queueC3W3WaitToggle = False
                else:
                    queueC3W3StartTime2 = self.env.now
                    queueC3W3WaitToggle = True 
                if(initializeCheck(self)):
                    queueC3W3ArrivalCount += 1
                print("Component 3 sent to Workstation 3")
                queueC3W3CapacityStart = self.env.now
               
        
class Workstation1:
    
    def __init__(self, env):    
        self.env = env
        self.name = "Workstation 1"
        self.product = "P1"
        self.buffer1 = container.Container(self.env, 2)
        self.productCount = 0
        self.arrivalCount = 0
        self.componentCount = 0
        self.systemTime = 0.0
        self.waitTime = 0.0
        self.idleTime = 0.0
        self.isWorkstation = True
        self.action = env.process(self.run())
    
    def run(self):
        global queueC1W1WaitToggle, queueC1W1StartTime1, queueC1W1StartTime2, queueC1W1DepartureCount, queueC1W1CapacityStart          
        queueC1W1DepartureCount = 0
        while True:
            idleW1 = self.env.now
            yield self.buffer1.get(1)
            if(initializeCheck(self)):
                self.idleTime += self.env.now - idleW1
                if(self.buffer1.level == 2):
                    queueC1W1CapacityList.append(tuple((self.buffer1.level, self.env.now - queueC1W1CapacityStart, "get")))
                else:
                    queueC1W1CapacityList.append(tuple((self.buffer1.level + 1, self.env.now - queueC1W1CapacityStart, "get")))
                queueC1W1DepartureCount += 1
            queueC1W1CapacityStart = self.env.now
            if queueC1W1WaitToggle:
                queueC1W1WaitTimeList.append(self.env.now - queueC1W1StartTime2)          
            else:      
                queueC1W1WaitTimeList.append(self.env.now - queueC1W1StartTime1)    
                queueC1W1WaitToggle = True
                
            print("Workstation 1 recieved required components")
            serviceTime = rng.workstation1_rng() 
            self.componentCount = self.componentCount + 1  
            if(initializeCheck(self)):
                self.componentCount = self.componentCount + 1  
                self.arrivalCount = self.arrivalCount + 1    
            yield self.env.timeout(float(serviceTime))
            if(initializeCheck(self)):
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
        self.idleTime = 0.0
        self.isWorkstation = True
        self.action = env.process(self.run())
    
    def run(self):
        global queueC1W2DepartureCount, queueC2W2DepartureCount
        queueC1W2DepartureCount = 0
        queueC2W2DepartureCount = 0
        while True:
            idleW2 = self.env.now 
            yield self.env.process(self.C1W2Process()) & self.env.process(self.C2W2Process())
            if (initializeCheck(self)):
                self.idleTime += self.env.now - idleW2
            print("Workstation 2 recieved required components")
            
            serviceTime = rng.workstation2_rng()
            
            yield self.env.timeout(float(serviceTime))
            if(initializeCheck(self)):
                self.productCount = self.productCount + 1
            print("Workstation 2 finished assembling product 2")         
 
    def C1W2Process(self):
        global queueC1W2WaitToggle, queueC1W2StartTime1, queueC1W2StartTime2, queueC1W2DepartureCount, queueC1W2CapacityList, queueC1W2CapacityStart
        yield self.buffer1.get(1)
        if(initializeCheck(self)):
            if(self.buffer1.level == 2):
                queueC1W2CapacityList.append(tuple((self.buffer1.level, self.env.now - queueC1W2CapacityStart, "get")))
            else:
                queueC1W2CapacityList.append(tuple((self.buffer1.level + 1, self.env.now - queueC1W2CapacityStart, "get")))
            queueC1W2DepartureCount += 1
        queueC1W2CapacityStart = self.env.now
        if queueC1W2WaitToggle:
            queueC1W2WaitTimeList.append(self.env.now - queueC1W2StartTime2)          
        else:      
            queueC1W2WaitTimeList.append(self.env.now - queueC1W2StartTime1)    
            queueC1W2WaitToggle = True     
                        
    def C2W2Process(self):
        global queueC2W2WaitToggle, queueC2W2StartTime1, queueC2W2StartTime2, queueC2W2DepartureCount, queueC2W2CapacityList, queueC2W2CapacityStart
        yield self.buffer2.get(1)
        if(initializeCheck(self)):
            if(self.buffer2.level == 2):
                queueC2W2CapacityList.append(tuple((self.buffer2.level, self.env.now - queueC2W2CapacityStart, "get")))
            else:
                queueC2W2CapacityList.append(tuple((self.buffer2.level + 1, self.env.now - queueC2W2CapacityStart, "get")))
            queueC2W2DepartureCount += 1
        queueC2W2CapacityStart = self.env.now
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
        self.idleTime = 0.0
        self.arrivalCount = 0
        self.componentCount = 0
        self.isWorkstation = True
        self.action = env.process(self.run())
        
    def run(self):
        global queueC1W3DepartureCount, queueC3W3DepartureCount
        queueC1W3DepartureCount = 0
        queueC3W3DepartureCount = 0        
        while True:
            idleW3 = self.env.now
            yield self.env.process(self.C1W3Process()) & self.env.process(self.C3W3Process())
            if (initializeCheck(self)):
                self.idleTime += self.env.now - idleW3           
            print("Workstation 3 recieved required components")
                
            serviceTime = rng.workstation3_rng()   
                        
            yield self.env.timeout(float(serviceTime))
            if(initializeCheck(self)):
                self.productCount = self.productCount + 1
            print("Workstation 3 finished assembling product 3")  
                    
    def C1W3Process(self):
        global queueC1W3WaitToggle, queueC1W3StartTime1, queueC1W3StartTime2, queueC1W3DepartureCount, queueC1W3CapacityList, queueC1W3CapacityStart
        yield self.buffer1.get(1)
        if(initializeCheck(self)):
            if(self.buffer1.level == 2):
                queueC1W3CapacityList.append(tuple((self.buffer1.level, self.env.now - queueC1W3CapacityStart, "get")))
            else:
                queueC1W3CapacityList.append(tuple((self.buffer1.level + 1, self.env.now - queueC1W3CapacityStart, "get")))        
            queueC1W3DepartureCount += 1
        queueC1W3CapacityStart = self.env.now
        if queueC1W3WaitToggle:
            queueC1W3WaitTimeList.append(self.env.now - queueC1W3StartTime2)          
        else:      
            queueC1W3WaitTimeList.append(self.env.now - queueC1W3StartTime1)    
            queueC1W3WaitToggle = True     
        
    def C3W3Process(self):
        global queueC3W3WaitToggle, queueC3W3StartTime1, queueC3W3StartTime2, queueC3W3DepartureCount, queueC3W3CapacityList, queueC3W3CapacityStart
        yield self.buffer3.get(1)
        if(initializeCheck(self)):
            if(self.buffer3.level == 2):
                queueC3W3CapacityList.append(tuple((self.buffer3.level, self.env.now - queueC3W3CapacityStart, "get")))
            else:
                queueC3W3CapacityList.append(tuple((self.buffer3.level + 1, self.env.now - queueC3W3CapacityStart, "get")))         
            queueC3W3DepartureCount += 1
        queueC3W3CapacityStart = self.env.now
        if queueC3W3WaitToggle:
            queueC3W3WaitTimeList.append(self.env.now - queueC3W3StartTime2)          
        else:      
            queueC3W3WaitTimeList.append(self.env.now - queueC3W3StartTime1)    
            queueC3W3WaitToggle = True   
            
def initializeCheck(self):
    global initialize_time
    return ((not sim.isProductionRun()) or system.env.now > initialize_time)

     
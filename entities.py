import simpy
import random
from simpy.resources import container

class Inspector1:
    
    def _init_(self, env, station1, station2, station3):
        self.env = env
        self.name = "I1"
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.serviceTimes = open('servinsp1.dat').read.splitlines()
        self.serviceTimeIndex = 0
        self.action = env.process(self.run())
             
    def run(self):
        print("Inspector 1 Start")
        while True:
            serviceTime = self.serviceTimes[serviceTimeIndex]
            if serviceTimeIndex == len(self.serviceTimes) - 1:
                serviceTimeIndex = 0         
            else:
                serviceTimeIndex = serviceTimeIndex + 1
          
            yield self.env.timeout(serviceTime)
            print("Inspector 1 finished assembling component 1")
            if self.station1.buffer1.level <= self.station2.buffer1.level and self.station1.buffer1.level <= self.station3.buffer1.level:
                yield self.station1.buffer1.put(1)
                print("Component 1 sent to WorkStation 1")
            elif self.station2.buffer1.level <= self.station3.buffer1.level:
                yield self.station2.buffer1.put(1)
                print("Component 1 sent to WorkStation 2")
            else:
                yield self.station3.buffer1.put(1)
                print("Component 1 sent to WorkStation 3")
        
        
class Inspector2:
    
    def _init_(self, env, station2, station3):
        self.env = env
        self.name = "I2"
        self.station2 = station2
        self.station3 = station3
        self.serviceTimes2 = open('servinsp22.dat').read.splitlines()
        self.serviceTimes3 = open('servinsp23.dat').read.splitlines()
        self.serviceTimeIndex = 0
        self.action = env.process(self.run())
        
    def run(self):
        print("Inspector 2 Start")
        while True:
            if (random.radint(2, 3) == 2):
                serviceTime = self.serviceTimes2[serviceTimeIndex]
                if serviceTimeIndex == len(self.serviceTimes2) - 1:
                    serviceTimeIndex = 0         
                else:
                    serviceTimeIndex = serviceTimeIndex + 1
                    
                yield self.env.timeout(serviceTime)
                print("Component 2 sent to WorkStation 2")
                yield self.station2.buffer2.put(1)
            else:
                serviceTime = self.serviceTimes3[serviceTimeIndex]
                if serviceTimeIndex == len(self.serviceTimes3) - 1:
                    serviceTimeIndex = 0         
                else:
                    serviceTimeIndex = serviceTimeIndex + 1
                    
                yield self.env.timeout(serviceTime)
                print("Component 3 sent to WorkStation 3")
                yield self.station3.buffer3.put(1)
        

class WorkStation1:
    
    def _init_(self, env):
        self.env = env
        self.name = "W1"
        self.product = "P1"
        self.buffer1 = container.Container(self.env, 2)
        self.serviceTimes = open('w1.dat').read.splitlines()
        self.serviceTimeIndex = 0
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            yield self.buffer1.get(1)
            print("WorkStation 1 recieved required components")
            
            serviceTime = self.serviceTimes[serviceTimeIndex]
            serviceTimeIndex = serviceTimeIndex + 1
            if serviceTimeIndex == len(self.serviceTimes) - 1:
                serviceTimeIndex = 0         
            else:
                serviceTimeIndex = serviceTimeIndex + 1    
                
            yield self.env.timeout(serviceTime)
            print("WorkStation 1 finished assembling product 1")
        

class WorkStation2:
    def _init_(self, env):
        self.env = env
        self.name = "W2"
        self.product = "P2"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer2 = container.Container(self.env, 2)
        self.serviceTimes = open('w2.dat').read.splitlines()
        self.serviceTimeIndex = 0
    
    def run(self):
        while True:
            yield self.buffer1.get(1) & self.buffer2.get(1)
            print("WorkStation 1 recieved required components")
            
            serviceTime = self.serviceTimes[serviceTimeIndex]
            serviceTimeIndex = serviceTimeIndex + 1
            if serviceTimeIndex == len(self.serviceTimes) - 1:
                serviceTimeIndex = 0         
            else:
                serviceTimeIndex = serviceTimeIndex + 1    
                
            yield self.env.timeout(serviceTime)
            print("WorkStation 2 finished assembling product 2")            
        
class WorkStation3:
    def _init_(self, env):
        self.env = env
        self.name = "W3"
        self.product = "P3"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer3 = container.Container(self.env, 2)
        self.serviceTimes = open('w3.dat').read.splitlines()
        self.serviceTimeIndex = 0
        self.canReceive = True  
        
    def run(self):
            while True:
                yield self.buffer2.get(1) & self.buffer3.get(1)
                print("WorkStation 3 recieved required components")
                    
                serviceTime = self.serviceTimes[serviceTimeIndex]
                serviceTimeIndex = serviceTimeIndex + 1
                if serviceTimeIndex == len(self.serviceTimes) - 1:
                    serviceTimeIndex = 0         
                else:
                    serviceTimeIndex = serviceTimeIndex + 1    
                        
                yield self.env.timeout(serviceTime)
                print("WorkStation 3 finished assembling product 3")        

        
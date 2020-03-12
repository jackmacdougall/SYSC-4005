import simpy
import random
from simpy.resources import container
import rng

class Inspector1:
    
    def __init__(self, env, station1, station2, station3):
        self.env = env
        self.name = "I1"
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.action = env.process(self.run())
             
    def run(self):
        while True:
            serviceTime = rng.inspector1_component1_rng()
          
            yield self.env.timeout(float(serviceTime))
            print("Inspector 1 finished assembling component 1")
            if self.station1.buffer1.level <= self.station2.buffer1.level and self.station1.buffer1.level <= self.station3.buffer1.level:
                yield self.station1.buffer1.put(1)
                print("Component 1 sent to Workstation 1")
            elif self.station2.buffer1.level <= self.station3.buffer1.level:
                yield self.station2.buffer1.put(1)
                print("Component 1 sent to Workstation 2")
            else:
                yield self.station3.buffer1.put(1)
                print("Component 1 sent to Workstation 3")
        
        
class Inspector2:
    
    def __init__(self, env, station2, station3):
        self.env = env
        self.name = "I2"
        self.station2 = station2
        self.station3 = station3
        self.action = env.process(self.run())
        
    def run(self):
        while True:
            if (random.randint(2, 3) == 2):
                serviceTime = rng.inspector2_component2_rng()
                    
                yield self.env.timeout(float(serviceTime))
                print("Inspector 2 finished assembling component 2")               
                yield self.station2.buffer2.put(1)
                print("Component 2 sent to Workstation 2")
            else:
                serviceTime = rng.inspector2_component3_rng()
                    
                yield self.env.timeout(float(serviceTime))
                print("Inspector 2 finished assembling component 3") 
                yield self.station3.buffer3.put(1)
                print("Component 3 sent to Workstation 3")
               
        
class Workstation1:
    
    def __init__(self, env):
        self.env = env
        self.name = "W1"
        self.product = "P1"
        self.buffer1 = container.Container(self.env, 2)
        self.serviceTimeIndex = 0
        self.productCount = 0
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            yield self.buffer1.get(1)
            print("Workstation 1 recieved required components")
            
            serviceTime = rng.workstation1_rng()   
                
            yield self.env.timeout(float(serviceTime))
            self.productCount = self.productCount + 1
            print("Workstation 1 finished assembling product 1")
        

class Workstation2:
    def __init__(self, env):
        self.env = env
        self.name = "W2"
        self.product = "P2"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer2 = container.Container(self.env, 2)
        self.serviceTimeIndex = 0
        self.productCount = 0
        self.action = env.process(self.run())
    
    def run(self):
        while True:
            yield self.buffer1.get(1) & self.buffer2.get(1)
            print("Workstation 1 recieved required components")
            
            serviceTime = rng.workstation2_rng()
                
            yield self.env.timeout(float(serviceTime))
            self.productCount = self.productCount + 1
            print("Workstation 2 finished assembling product 2")            
        
class Workstation3:
    def __init__(self, env):
        self.env = env
        self.name = "W3"
        self.product = "P3"
        self.buffer1 = container.Container(self.env, 2)
        self.buffer3 = container.Container(self.env, 2)
        self.serviceTimeIndex = 0
        self.productCount = 0
        self.action = env.process(self.run())
        
    def run(self):
            while True:
                yield self.buffer1.get(1) & self.buffer3.get(1)
                print("Workstation 3 recieved required components")
                    
                serviceTime = rng.workstation3_rng()   
                        
                yield self.env.timeout(float(serviceTime))
                self.productCount = self.productCount + 1
                print("Workstation 3 finished assembling product 3")        

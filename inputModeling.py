import matplotlib.pyplot as plt
import numpy as np

def histogramInspector1():
    readData = np.array(open('data/servinsp1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Inspector 1 service times")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()
    
def histogramInspector2Component2():
    readData = np.array(open('data/servinsp22.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Inspector 2 service times for Component 2")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()   
    
def histogramInspector2Component3():
    readData = np.array(open('data/servinsp23.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Inspector 2 service times for Component 3")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()    
    
def histogramWorkstation1():
    readData = np.array(open('data/ws1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Workstation 1 service times")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()   

def histogramWorkstation2():
    readData = np.array(open('data/ws2.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Workstation 2 service times")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()   

def histogramWorkstation3():
    readData = np.array(open('data/ws3.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    fig, axis = plt.subplots()
    axis.set_title(r"Histogram of Workstation 3 service times")
    axis.set_xlabel("x")
    axis.set_ylabel("service time")    
    axis.hist(floatData,  bins=15, normed=True)
    plt.show()   
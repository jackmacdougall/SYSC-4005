import math as math
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy
import scipy.stats as st
import warnings

def histogramAndQQInspector1():
    
    readData = np.array(open('../data/servinsp1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 1 inspection times")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
    
    plt.show()    
       
    performChiSquare(floatData, frequencies)
    
    
def histogramAndQQInspector2Component2():
    
    readData = np.array(open('../data/servinsp22.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 2 inspection times for Component 2")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
    
    plt.show()   
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
    
    plt.show()    
    
    performChiSquare(floatData, frequencies)
    
    
def histogramAndQQInspector2Component3():
    
    readData = np.array(open('../data/servinsp23.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 2 inspection times for Component 3")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
        
    plt.show()      
    
    performChiSquare(floatData, frequencies)
    
def histogramAndQQWorkstation1():
    readData = np.array(open('../data/ws1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1)    
    axis.set_title(r"Histogram of Workstation 1 assembly times")
    axis.set_xlabel("Assembly Time (Minutes)")
    axis.set_ylabel("Frequency")     
    axis.hist(floatData,  bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
            
    plt.show()
    
    performChiSquare(floatData, frequencies)
    
   
def histogramAndQQWorkstation2():
    readData = np.array(open('../data/ws2.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1) 
    axis.set_title(r"Histogram of Workstation 2 assembly times")
    axis.set_xlabel("Service Time")
    axis.set_ylabel("Assembly Time (Minutes)")     
    plt.hist(floatData, bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
                
    plt.show()  
    performChiSquare(floatData, frequencies)
    
def histogramAndQQWorkstation3():
    readData = np.array(open('../data/ws3.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(12,6))
    axis = plt.subplot(1,2,1)     
    axis.set_title(r"Histogram of Workstation 3 assembly times")
    axis.set_xlabel("Service Time")
    axis.set_ylabel("Assembly Time (Minutes)")   
    plt.hist(floatData,  bins=18)
    frequencies, bin_edges = np.histogram(floatData, bins=18)
  
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
                
    plt.show()      
    performChiSquare(floatData, frequencies)
    

def performChiSquare(data, frequencies):
    mean = np.mean(data)
    print("sample mean = " + str(mean))
    lam = 1.0/mean
    print("lambda = " + str(lam))
    max_value = max(data)
    print("max value = " + str(max_value))
    min_value = min(data)
    print("min value = " + str(min_value))
    data_range = max_value - min_value
    print("data range = " + str(data_range))
    bin_size = data_range/18
    print("bin width = " + str(bin_size))
    
    threshold_from_table = 26.296
    threshold_from_calculation = 0.0
    bin_number = 1
    
    for observed in frequencies:
        expected = ((1 - math.exp(lam * bin_number * bin_size * -1)) - (1 - math.exp(lam * (bin_number-1) * bin_size * -1))) * 300
        if(expected > 0.0):
            threshold_val = (math.pow(observed - expected, 2.0))/expected
            threshold_from_calculation = threshold_from_calculation + threshold_val
        bin_number = bin_number + 1

    if (threshold_from_calculation > threshold_from_table):
        print(str(threshold_from_calculation) + " > " + str(threshold_from_table))
        print("The hypothesis was rejected at the 0.05 level of significance")
        
    else:
        print(str(threshold_from_calculation) + " <= " + str(threshold_from_table))
        print("The hypothesis can be accepted at the 0.05 level of significance")        
    
    
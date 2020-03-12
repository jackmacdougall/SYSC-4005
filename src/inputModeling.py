import math as math
import matplotlib.pyplot as plt
import numpy as np
import pylab
import scipy
import scipy.stats as st
import warnings

def histogramAndQQInspector1Component1():
    
    readData = np.array(open('../data/servinsp1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 1 inspection times for Component 1")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
    
    plt.show()    
       
    performChiSquare(floatData, frequencies)
    
    
def histogramAndQQInspector2Component2():
    
    readData = np.array(open('../data/servinsp22.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
 
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 2 inspection times for Component 2")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
    
    plt.show()   
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
    
    plt.show()    
    
    performChiSquare(floatData, frequencies)
    
    
def histogramAndQQInspector2Component3():
    
    readData = np.array(open('../data/servinsp23.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
    axis = plt.subplot(1,2,1)
    axis.set_title(r"Histogram of Inspector 2 inspection times for Component 3")
    axis.set_xlabel("Inspection Time (Minutes)")
    axis.set_ylabel("Frequency")    
    plt.hist(floatData,  bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
        
    plt.show()      
    
    performChiSquare(floatData, frequencies)
    
def histogramAndQQWorkstation1():
    readData = np.array(open('../data/ws1.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
    axis = plt.subplot(1,2,1)    
    axis.set_title(r"Histogram of Workstation 1 assembly times")
    axis.set_xlabel("Assembly Time (Minutes)")
    axis.set_ylabel("Frequency")     
    axis.hist(floatData,  bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
            
    plt.show()
    
    performChiSquare(floatData, frequencies)
    
   
def histogramAndQQWorkstation2():
    readData = np.array(open('../data/ws2.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
    axis = plt.subplot(1,2,1) 
    axis.set_title(r"Histogram of Workstation 2 assembly times")
    axis.set_xlabel("Service Time")
    axis.set_ylabel("Assembly Time (Minutes)")     
    plt.hist(floatData, bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
    
    #QQ plot
    plt.subplot(1,2,2)
    res = st.probplot(floatData, dist="expon", plot=plt);
                
    plt.show()  
    performChiSquare(floatData, frequencies)
    
def histogramAndQQWorkstation3():
    readData = np.array(open('../data/ws3.dat').read().splitlines())
    floatData = readData[0:300].astype(np.float)
    plt.figure(figsize=(18,6))
    axis = plt.subplot(1,2,1)     
    axis.set_title(r"Histogram of Workstation 3 assembly times")
    axis.set_xlabel("Service Time")
    axis.set_ylabel("Assembly Time (Minutes)")   
    plt.hist(floatData,  bins=17)
    frequencies, bin_edges = np.histogram(floatData, bins=17)
  
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
    data_range = max_value - min_value
    interval_size = data_range/17
    
    threshold_from_table = 27.488
    print("Threshold Value from Table = " + str(threshold_from_table))
    threshold_from_calculation = 0.0
    interval_number = 1
    
    print("")
    
    for observed in frequencies:
        print("Bin: " + str(interval_number))
        
        if (interval_number == 17):
            print("Interval: " + str(interval_size * (interval_number-1)) + "-" + str(max_value))
        else:
            print("Interval: " + str(interval_size * (interval_number-1)) + "-" + str(interval_size * interval_number))
            
        print("Observed Frequency: " + str(observed))
        if (interval_number == 17):
            expected = ((1 - math.exp(lam * max_value * -1)) - (1 - math.exp(lam * (interval_number-1) * interval_size * -1))) * 300
        else:   
            expected = ((1 - math.exp(lam * interval_number * interval_size * -1)) - (1 - math.exp(lam * (interval_number-1) * interval_size * -1))) * 300
        print("Expected Frequency: " + str(expected))
        if(expected > 0.0):
            threshold_val = (math.pow(observed - expected, 2.0))/expected
            threshold_from_calculation = threshold_from_calculation + threshold_val
            print("Result: " + str(threshold_val))
        interval_number = interval_number + 1
        print("")

    print("Caluclated Threshold Value = " + str(threshold_from_calculation))
    if (threshold_from_calculation > threshold_from_table):
        print("Since " + str(threshold_from_calculation) + " > " + str(threshold_from_table))
        print("The hypothesis was rejected at the 0.05 level of significance")
        
    else:
        print("Since " + str(threshold_from_calculation) + " <= " + str(threshold_from_table))
        print("The hypothesis can be accepted at the 0.05 level of significance")        
        
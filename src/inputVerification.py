import entities as en

def littleLaw():
 
    CalculateL("C1W1", en.queueC1W1CapacityList, en.queueC1W1DepartureCount)
               
    total_wait_C1W1 = 0.0
    for wait in en.queueC1W1WaitTimeList:
        total_wait_C1W1 += wait
   
    avg_wait_C1W1 = total_wait_C1W1/len(en.queueC1W1WaitTimeList)
    print("Average wait time for C1W1 = ", avg_wait_C1W1, " minutes")
    
    arrival_rate_C1W1 = en.queueC1W1DepartureCount/2400
    print("Arrival Rate for C1W1 = ", arrival_rate_C1W1, " components per minute")
    
    little_law_C1W1 = avg_wait_C1W1 * arrival_rate_C1W1
    print("Little's Law calculation for C1W1 = ", little_law_C1W1)
    
    CalculateL("C1W2", en.queueC1W2CapacityList, en.queueC1W2DepartureCount)
    
    total_wait_C1W2 = 0.0
    for wait in en.queueC1W2WaitTimeList:
        total_wait_C1W2 += wait
    avg_wait_C1W2 = total_wait_C1W2/len(en.queueC1W2WaitTimeList)
    print("Average wait time for C1W2 = ", avg_wait_C1W2, " minutes")  
    
    arrival_rate_C1W2 = en.queueC1W2DepartureCount/2400
    print("Arrival Rate for C1W2 = ", arrival_rate_C1W2, " components per minute")
        
    little_law_C1W2 = avg_wait_C1W2 * arrival_rate_C1W2
    print("Little's Law calculation for C1W2 = ", little_law_C1W2)    

    CalculateL("C1W3", en.queueC1W3CapacityList, en.queueC1W3DepartureCount)
    
    total_wait_C1W3 = 0.0
    for wait in en.queueC1W3WaitTimeList:
        total_wait_C1W3 += wait
    avg_wait_C1W3 = total_wait_C1W3/len(en.queueC1W3WaitTimeList)
    print("Average wait time for C1W3 = ", avg_wait_C1W3, " minutes")
       
    arrival_rate_C1W3 = en.queueC1W3DepartureCount/2400
    print("Arrival Rate for C1W3 = ", arrival_rate_C1W3, " components per minute")
        
    little_law_C1W3 = avg_wait_C1W3 * arrival_rate_C1W3
    print("Little's Law calculation for C1W3 = ", little_law_C1W3)    

    CalculateL("C2W2", en.queueC2W2CapacityList, en.queueC2W2DepartureCount)
    
    total_wait_C2W2 = 0.0
    for wait in en.queueC2W2WaitTimeList:
        total_wait_C2W2 += wait
    avg_wait_C2W2 = total_wait_C2W2/len(en.queueC2W2WaitTimeList)
    print("Average wait time for C2W2 = ", avg_wait_C2W2, " minutes")
    
    arrival_rate_C2W2 = en.queueC2W2DepartureCount/2400
    print("Arrival Rate for C2W2 = ", arrival_rate_C2W2, " components per minute")
            
    little_law_C2W2 = avg_wait_C2W2 * arrival_rate_C2W2
    print("Little's Law calculation for C2W2 = ", little_law_C2W2)       
    
    CalculateL("C3W3", en.queueC3W3CapacityList, en.queueC3W3DepartureCount)
    
    total_wait_C3W3 = 0.0
    for wait in en.queueC3W3WaitTimeList:
        total_wait_C3W3 += wait
    avg_wait_C3W3 = total_wait_C3W3/len(en.queueC3W3WaitTimeList)

    print("Average wait time for C3W3 = ", avg_wait_C3W3, " minutes")
    
    arrival_rate_C3W3 = en.queueC3W3DepartureCount/2400
    print("Arrival Rate for C3W3 = ", arrival_rate_C3W3, " components per minute")
            
    little_law_C3W3 = avg_wait_C3W3 * arrival_rate_C3W3
    print("Little's Law calculation for C3W3 = ", little_law_C3W3)   

    #print(len(en.queueC1W1WaitTimeList))
    #print(len(en.queueC3W3CapacityList))
    #print(en.queueC3W3DepartureCount)
    
    for e in en.queueC3W3CapacityList:
        print(e[0], e[1], e[2])
     

def CalculateL(name, lst, threshold):
    oneTime = 0.0
    twoTime = 0.0
    total = 0.0
    counter = 0
    
    #for entry in lst:      
        #if counter < threshold:
            #if entry[0] == 1:
                #oneTime += entry[1]
            #elif entry[0] == 2:
                #twoTime += entry[1]
            #total += entry[1]
        #if entry[2] == "get":
            #counter += 1        
    #if(total > 0.0):          
        #avg = (((oneTime)+(twoTime * 2)))/total
        #print("L for ", name ," = ", avg)   
    #else:
        #print("L for ", name ," = 0.0")
    
    for entry in lst:  
        if entry[0] == 1:
            oneTime += entry[1]
        elif entry[0] == 2:
            twoTime += entry[1]
        total += entry[1]
        if entry[2] == "get":
            counter += 1  
        if counter >= threshold:
            break
        
    if(total > 0.0):          
        avg = (((oneTime)+(twoTime * 2)))/total
        print("L for ", name ,"= ", avg)   
    else:
        print("L for ", name ,"= 0.0")    
import entities as en

def littleLaw():
    total_wait_C1W1 = 0.0
    for wait in en.queueC1W1WaitTimeList:
        total_wait_C1W1 += wait
    avg_wait_C1W1 = total_wait_C1W1/len(en.queueC1W1WaitTimeList)
    print("Average wait time for C1W1 = ", avg_wait_C1W1, " minutes")
    
    arrival_rate_C1W1 = en.queueC1W1ArrivalCount/2400
    print("Arrival rate for C1W1 = ", arrival_rate_C1W1, " components per minute")
    
    total_wait_C1W2 = 0.0
    for wait in en.queueC1W2WaitTimeList:
        total_wait_C1W2 += wait
    avg_wait_C1W2 = total_wait_C1W2/len(en.queueC1W2WaitTimeList)
    print("Average wait time for C1W2 = ", avg_wait_C1W2, " minutes")    

    total_wait_C1W3 = 0.0
    for wait in en.queueC1W3WaitTimeList:
        total_wait_C1W3 += wait
    avg_wait_C1W3 = total_wait_C1W3/len(en.queueC1W3WaitTimeList)
    print("Average wait time for C1W3 = ", avg_wait_C1W3, " minutes")
    
    total_wait_C2W2 = 0.0
    for wait in en.queueC1W1WaitTimeList:
        total_wait_C2W2 += wait
    avg_wait_C2W2 = total_wait_C2W2/len(en.queueC2W2WaitTimeList)
    print("Average wait time for C2W2 = ", avg_wait_C2W2, " minutes")
    
    total_wait_C3W3 = 0.0
    for wait in en.queueC1W1WaitTimeList:
        total_wait_C3W3 += wait
    avg_wait_C3W3 = total_wait_C3W3/len(en.queueC3W3WaitTimeList)
    print("Average wait time for C2W2 = ", avg_wait_C3W3, " minutes")
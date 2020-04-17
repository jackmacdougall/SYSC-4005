import simpy
import entities
import inputVerification as iv
import numpy as np
import statistics as stat
import scipy.stats
import rng

initialize = False
prod_pass = True
alternative = False

def sim():
    simulation_env = simpy.Environment()
    workstation1 = entities.Workstation1(simulation_env, None)
    workstation2 = entities.Workstation2(simulation_env, None)
    workstation3 = entities.Workstation3(simulation_env, None)
    inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, False, None)
    inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, None, None, None)
    minutes = 2400
    simulation_env.run(minutes)
    
    print('Finished Simulation')
    
    print("Components 1 inspected ", inspector1.componentCount)
    print("Components 2 inspected ", inspector2.component2Count)
    print("Components 3 inspected ", inspector2.component3Count)
    
    print("Components 1 sent to W1 ", entities.queueC1W1DepartureCount)
    print("Components 1 sent to W2 ", entities.queueC1W2DepartureCount)
    print("Components 1 sent to W3 ", entities.queueC1W3DepartureCount)
    print("Components 2 sent to W2 ", entities.queueC2W2DepartureCount)
    print("Components 3 sent to W3 ", entities.queueC3W3DepartureCount)
    
    print("Products 1 assembled ", workstation1.productCount)
    print("Products 2 assembled ", workstation2.productCount)
    print("Products 3 assembled ", workstation3.productCount)

    
    iv.littleLaw()

def simProd(replications):
    global initialize, prod_pass
    initialize = True
    counter = 0
    
    component1Count = []
    component2Count = []
    component3Count = []
    component1ToW1Count = []
    component1ToW2Count = []
    component1ToW3Count = []
    component2ToW2Count = []
    component3ToW3Count = []
    product1Count = []
    product2Count = []
    product3Count = []
    idleTimeInspector1 = []
    idleTimeInspector2 = []
    idleTimeWorkstation1 = []
    idleTimeWorkstation2 = []
    idleTimeWorkstation3 = []
    product1Throughput = []
    product2Throughput = []
    product3Throughput = []
            
    
    while(counter < replications):
        simulation_env = simpy.Environment()
        workstation1 = entities.Workstation1(simulation_env, None)
        workstation2 = entities.Workstation2(simulation_env, None)
        workstation3 = entities.Workstation3(simulation_env, None)
        inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, False, None)
        inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, None, None, None)
        minutes = 2400
        simulation_env.run(minutes)
        
        component1Count.append(inspector1.componentCount)
        component2Count.append(inspector2.component2Count)
        component3Count.append(inspector2.component3Count)
        
        component1ToW1Count.append(entities.queueC1W1DepartureCount)
        component1ToW2Count.append(entities.queueC1W2DepartureCount)
        component1ToW3Count.append(entities.queueC1W3DepartureCount)
        component2ToW2Count.append(entities.queueC2W2DepartureCount)
        component3ToW3Count.append(entities.queueC3W3DepartureCount)
        
        product1Count.append(workstation1.productCount)
        product2Count.append(workstation2.productCount)
        product3Count.append(workstation3.productCount)
        
        idleTimeInspector1.append(inspector1.idleTime/(2400 - 175))
        idleTimeInspector2.append(inspector2.idleTime/(2400 - 175))
        idleTimeWorkstation1.append(workstation1.idleTime/(2400 - 175))
        idleTimeWorkstation2.append(workstation2.idleTime/(2400 - 175))
        idleTimeWorkstation3.append(workstation3.idleTime/(2400 - 175))
        
        product1Throughput.append(workstation1.productCount/(2400 - 175))
        product2Throughput.append(workstation2.productCount/(2400 - 175))
        product3Throughput.append(workstation3.productCount/(2400 - 175))
        
        counter += 1
    
    component1CountMean = np.mean(component1Count)
    component2CountMean = np.mean(component2Count)
    component3CountMean = np.mean(component3Count)
    component1CountVariance = stat.variance(component1Count)
    component2CountVariance = stat.variance(component2Count)
    component3CountVariance = stat.variance(component3Count)
    component1CountCI = mean_confidence_interval(component1Count)
    component2CountCI = mean_confidence_interval(component2Count)
    component3CountCI = mean_confidence_interval(component3Count)
    
    component1ToW1CountMean = np.mean(component1ToW1Count)
    component1ToW2CountMean = np.mean(component1ToW2Count)
    component1ToW3CountMean = np.mean(component1ToW3Count)
    component2ToW2CountMean = np.mean(component2ToW2Count)     
    component3ToW3CountMean = np.mean(component3ToW3Count)
    component1ToW1CountVariance = stat.variance(component1ToW1Count)
    component1ToW2CountVariance = stat.variance(component1ToW2Count)
    component1ToW3CountVariance = stat.variance(component1ToW3Count)
    component2ToW2CountVariance = stat.variance(component2ToW2Count)
    component3ToW3CountVariance = stat.variance(component3ToW3Count)
    component1ToW1CountCI = mean_confidence_interval(component1ToW1Count)
    component1ToW2CountCI = mean_confidence_interval(component1ToW2Count)
    component1ToW3CountCI = mean_confidence_interval(component1ToW3Count)
    component2ToW2CountCI = mean_confidence_interval(component2ToW2Count)    
    component3ToW3CountCI = mean_confidence_interval(component3ToW3Count)
                
    product1CountMean = np.mean(product1Count)
    product2CountMean = np.mean(product2Count)
    product3CountMean = np.mean(product3Count)
    product1CountVariance = stat.variance(product1Count)
    product2CountVariance = stat.variance(product2Count)
    product3CountVariance = stat.variance(product3Count)
    product1CountCI = mean_confidence_interval(product1Count)
    product2CountCI = mean_confidence_interval(product2Count)
    product3CountCI = mean_confidence_interval(product3Count)

    idleTimeInspector1Mean = np.mean(idleTimeInspector1)
    idleTimeInspector2Mean = np.mean(idleTimeInspector2)
    idleTimeWorkstation1Mean = np.mean(idleTimeWorkstation1)
    idleTimeWorkstation2Mean = np.mean(idleTimeWorkstation2)
    idleTimeWorkstation3Mean = np.mean(idleTimeWorkstation3)
    idleTimeInspector1Variance = stat.variance(idleTimeInspector1)
    idleTimeInspector2Variance = stat.variance(idleTimeInspector2)
    idleTimeWorkstation1Variance = stat.variance(idleTimeWorkstation1)
    idleTimeWorkstation2Variance = stat.variance(idleTimeWorkstation2)
    idleTimeWorkstation3Variance = stat.variance(idleTimeWorkstation3)
    idleTimeInspector1CI = mean_confidence_interval(idleTimeInspector1)
    idleTimeInspector2CI = mean_confidence_interval(idleTimeInspector2)
    idleTimeWorkstation1CI = mean_confidence_interval(idleTimeWorkstation1)
    idleTimeWorkstation2CI = mean_confidence_interval(idleTimeWorkstation2)
    idleTimeWorkstation3CI = mean_confidence_interval(idleTimeWorkstation3)
    
    product1ThroughputMean = np.mean(product1Throughput)
    product1ThroughputVariance = stat.variance(product1Throughput)
    product1ThroughputCI = mean_confidence_interval(product1Throughput)
    product2ThroughputMean = np.mean(product2Throughput)
    product2ThroughputVariance = stat.variance(product2Throughput)
    product2ThroughputCI = mean_confidence_interval(product2Throughput)  
    product3ThroughputMean = np.mean(product3Throughput)
    product3ThroughputVariance = stat.variance(product3Throughput)
    product3ThroughputCI = mean_confidence_interval(product3Throughput)  
    
    within_twenty(component1CountMean, component1CountCI)
    within_twenty(component2CountMean, component2CountCI)
    within_twenty(component3CountMean, component3CountCI)
    within_twenty(component1ToW1CountMean, component1ToW1CountCI)
    within_twenty(component1ToW2CountMean, component1ToW2CountCI)
    within_twenty(component1ToW3CountMean, component1ToW3CountCI)
    within_twenty(component2ToW2CountMean, component2ToW2CountCI)
    within_twenty(component3ToW3CountMean, component3ToW3CountCI)
    within_twenty(product1CountMean, product1CountCI)
    within_twenty(product2CountMean, product2CountCI)
    within_twenty(product3CountMean, product3CountCI)
    within_twenty(idleTimeInspector1Mean, idleTimeInspector1CI)
    within_twenty(idleTimeInspector2Mean, idleTimeInspector2CI)
    within_twenty(idleTimeWorkstation1Mean, idleTimeWorkstation1CI)
    within_twenty(idleTimeWorkstation2Mean, idleTimeWorkstation2CI)
    within_twenty(idleTimeWorkstation3Mean, idleTimeWorkstation3CI)
    within_twenty(product1ThroughputMean, product1ThroughputCI)
    within_twenty(product2ThroughputMean, product2ThroughputCI)
    within_twenty(product3ThroughputMean, product3ThroughputCI)
    
    
    if(prod_pass):
        print(replications, " replications is adequate")
        print("Component 1 Inspected - Mean: ", component1CountMean, ", Variance: ", component1CountVariance, ", CI: ", component1CountCI)
        print("Component 2 Inspected - Mean: ", component2CountMean, ", Variance: ", component2CountVariance, ", CI: ", component2CountCI)
        print("Component 3 Inspected - Mean: ", component3CountMean, ", Variance: ", component3CountVariance, ", CI: ", component3CountCI)
        print("Queue C1W1 Output - Mean: ", component1ToW1CountMean, ", Variance: ", component1ToW1CountVariance, ", CI: ", component1ToW1CountCI)
        print("Queue C1W2 Output - Mean: ", component1ToW2CountMean, ", Variance: ", component1ToW2CountVariance, ", CI: ", component1ToW2CountCI)
        print("Queue C1W3 Output - Mean: ", component1ToW3CountMean, ", Variance: ", component1ToW3CountVariance, ", CI: ", component1ToW3CountCI)
        print("Queue C2W2 Output - Mean: ", component2ToW2CountMean, ", Variance: ", component2ToW2CountVariance, ", CI: ", component2ToW2CountCI)
        print("Queue C3W3 Output - Mean: ", component3ToW3CountMean, ", Variance: ", component3ToW3CountVariance, ", CI: ", component3ToW3CountCI)
        print("Product 1 Produced - Mean: ", product1CountMean, ", Variance: ", product1CountVariance, ", CI: ", product1CountCI)
        print("Product 2 Produced - Mean: ", product2CountMean, ", Variance: ", product2CountVariance, ", CI: ", product2CountCI)
        print("Product 3 Produced - Mean: ", product3CountMean, ", Variance: ", product3CountVariance, ", CI: ", product3CountCI)
        print("Proportion Inspector1 Idle - Mean: ", idleTimeInspector1Mean, ", Variance: ", idleTimeInspector1Variance, ", CI: ", idleTimeInspector1CI)
        print("Proportion Inspector2 Idle - Mean: ", idleTimeInspector2Mean, ", Variance: ", idleTimeInspector2Variance, ", CI: ", idleTimeInspector2CI)
        print("Proportion Workstation1 Idle - Mean: ", idleTimeWorkstation1Mean, ", Variance: ", idleTimeWorkstation1Variance, ", CI: ", idleTimeWorkstation1CI)
        print("Proportion Workstation2 Idle - Mean: ", idleTimeWorkstation2Mean, ", Variance: ", idleTimeWorkstation2Variance, ", CI: ", idleTimeWorkstation2CI)
        print("Proportion Workstation3 Idle - Mean: ", idleTimeWorkstation3Mean, ", Variance: ", idleTimeWorkstation3Variance, ", CI: ", idleTimeWorkstation3CI)
        print("Product 1 Throughput - Mean: ", product1ThroughputMean, ", Variance: ", product1ThroughputVariance, ", CI: ", product1ThroughputCI)
        print("Product 2 Throughput - Mean: ", product2ThroughputMean, ", Variance: ", product2ThroughputVariance, ", CI: ", product2ThroughputCI)
        print("Product 3 Throughput - Mean: ", product3ThroughputMean, ", Variance: ", product3ThroughputVariance, ", CI: ", product3ThroughputCI)  
    else:
        print("need more replications to satisfy requirements")

def isProductionRun():
    global initialize
    return initialize

def isAlternative():
    global alternative
    return alternative


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(data)
    m, se = np.mean(data), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m-h, m+h

def within_twenty(mean, CI):
    global prod_pass
    if prod_pass:
        twenty_percent = mean * 0.20
        prod_pass = (mean - CI[0] <= twenty_percent and CI[1] - mean <= twenty_percent)

def simAlternative():
    inspector1component1_servicetimes = []
    inspector2component2_servicetimes = []
    inspector2component3_servicetimes = []
    workstation1_servicetimes = []
    workstation2_servicetimes = []
    workstation3_servicetimes = []
    random_2_3 = []
    
    for i in range(400):
        inspector1component1_servicetimes.append(rng.inspector1_component1_rng()) 
        inspector2component2_servicetimes.append(rng.inspector2_component2_rng())
        inspector2component3_servicetimes.append(rng.inspector2_component3_rng())
        workstation1_servicetimes.append(rng.workstation1_rng())
        workstation2_servicetimes.append(rng.workstation2_rng())
        workstation3_servicetimes.append(rng.workstation3_rng())  
        random_2_3.append(rng.random_2_3())
        
    simulation_env = simpy.Environment()
    workstation1 = entities.Workstation1(simulation_env, workstation1_servicetimes)
    workstation2 = entities.Workstation2(simulation_env, workstation2_servicetimes)
    workstation3 = entities.Workstation3(simulation_env, workstation3_servicetimes)
    inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, True, inspector1component1_servicetimes)
    inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, inspector2component2_servicetimes, inspector2component3_servicetimes, random_2_3)
    minutes = 2400
    simulation_env.run(minutes)    
    
    print('Finished Simulation')
    
    print("Components 1 inspected ", inspector1.componentCount)
    print("Components 2 inspected ", inspector2.component2Count)
    print("Components 3 inspected ", inspector2.component3Count)
    
    print("Components 1 sent to W1 ", entities.queueC1W1DepartureCount)
    print("Components 1 sent to W2 ", entities.queueC1W2DepartureCount)
    print("Components 1 sent to W3 ", entities.queueC1W3DepartureCount)
    print("Components 2 sent to W2 ", entities.queueC2W2DepartureCount)
    print("Components 3 sent to W3 ", entities.queueC3W3DepartureCount)
    
    print("Products 1 assembled ", workstation1.productCount)
    print("Products 2 assembled ", workstation2.productCount)
    print("Products 3 assembled ", workstation3.productCount)    

    iv.littleLaw()    

    #simulation_env = simpy.Environment()
    #workstation1 = entities.Workstation1(simulation_env, workstation1_servicetimes)
    #workstation2 = entities.Workstation2(simulation_env, workstation2_servicetimes)
    #workstation3 = entities.Workstation3(simulation_env, workstation3_servicetimes)
    #inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, False, inspector1component1_servicetimes)
    #inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, inspector2component2_servicetimes, inspector2component3_servicetimes, random_2_3)
    #minutes = 2400
    #simulation_env.run(minutes)
    
    
    
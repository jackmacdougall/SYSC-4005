import simpy
import entities
import inputVerification as iv
import numpy as np
import statistics as stat
import scipy.stats
import rng
import pylab as pyl
import matplotlib.pyplot as plt

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
    global initialize, prod_pass, alternative
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
    
    component1CountAlt = []
    component2CountAlt = []
    component3CountAlt = []
    component1ToW1CountAlt = []
    component1ToW2CountAlt = []
    component1ToW3CountAlt = []
    component2ToW2CountAlt = []
    component3ToW3CountAlt = []
    product1CountAlt = []
    product2CountAlt = []
    product3CountAlt = []
    idleTimeInspector1Alt = []
    idleTimeInspector2Alt = []
    idleTimeWorkstation1Alt = []
    idleTimeWorkstation2Alt = []
    idleTimeWorkstation3Alt = []
    product1ThroughputAlt = []
    product2ThroughputAlt = []
    product3ThroughputAlt = [] 
    
    component1CountDiff = []
    component2CountDiff = []
    component3CountDiff = []
    component1ToW1CountDiff = []
    component1ToW2CountDiff = []
    component1ToW3CountDiff = []
    component2ToW2CountDiff = []
    component3ToW3CountDiff = []
    product1CountDiff = []
    product2CountDiff = []
    product3CountDiff = []
    idleTimeInspector1Diff = []
    idleTimeInspector2Diff = []
    idleTimeWorkstation1Diff = []
    idleTimeWorkstation2Diff = []
    idleTimeWorkstation3Diff = []
    product1ThroughputDiff = []
    product2ThroughputDiff = []
    product3ThroughputDiff = []      
            
    
    while(counter < replications):
        inspector1component1_servicetimes = []
        inspector2component2_servicetimes = []
        inspector2component3_servicetimes = []
        workstation1_servicetimes = []
        workstation2_servicetimes = []
        workstation3_servicetimes = []
        random_2_3 = []
        
        for i in range(500):
            inspector1component1_servicetimes.append(rng.inspector1_component1_rng()) 
            inspector2component2_servicetimes.append(rng.inspector2_component2_rng())
            inspector2component3_servicetimes.append(rng.inspector2_component3_rng())
            workstation1_servicetimes.append(rng.workstation1_rng())
            workstation2_servicetimes.append(rng.workstation2_rng())
            workstation3_servicetimes.append(rng.workstation3_rng())  
            random_2_3.append(rng.random_2_3())        
        
        alternative = False
        simulation_env = simpy.Environment()
        workstation1 = entities.Workstation1(simulation_env, workstation1_servicetimes)
        workstation2 = entities.Workstation2(simulation_env, workstation2_servicetimes)
        workstation3 = entities.Workstation3(simulation_env, workstation3_servicetimes)
        inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, False, inspector1component1_servicetimes)
        inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, inspector2component2_servicetimes, inspector2component3_servicetimes, random_2_3)
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
        
        entities.resetVariables()
        
        alternative = True
        simulation_env = simpy.Environment()
        workstation1 = entities.Workstation1(simulation_env, workstation1_servicetimes)
        workstation2 = entities.Workstation2(simulation_env, workstation2_servicetimes)
        workstation3 = entities.Workstation3(simulation_env, workstation3_servicetimes)
        inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, True, inspector1component1_servicetimes)
        inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, inspector2component2_servicetimes, inspector2component3_servicetimes, random_2_3)
        minutes = 2400
        simulation_env.run(minutes)
        
        component1CountAlt.append(inspector1.componentCount)
        component2CountAlt.append(inspector2.component2Count)
        component3CountAlt.append(inspector2.component3Count)
        
        component1ToW1CountAlt.append(entities.queueC1W1DepartureCount)
        component1ToW2CountAlt.append(entities.queueC1W2DepartureCount)
        component1ToW3CountAlt.append(entities.queueC1W3DepartureCount)
        component2ToW2CountAlt.append(entities.queueC2W2DepartureCount)
        component3ToW3CountAlt.append(entities.queueC3W3DepartureCount)
        
        product1CountAlt.append(workstation1.productCount)
        product2CountAlt.append(workstation2.productCount)
        product3CountAlt.append(workstation3.productCount)
        
        idleTimeInspector1Alt.append(inspector1.idleTime/(2400 - 100))
        idleTimeInspector2Alt.append(inspector2.idleTime/(2400 - 100))
        idleTimeWorkstation1Alt.append(workstation1.idleTime/(2400 - 100))
        idleTimeWorkstation2Alt.append(workstation2.idleTime/(2400 - 100))
        idleTimeWorkstation3Alt.append(workstation3.idleTime/(2400 - 100))
        
        product1ThroughputAlt.append(workstation1.productCount/(2400 - 100))
        product2ThroughputAlt.append(workstation2.productCount/(2400 - 100))
        product3ThroughputAlt.append(workstation3.productCount/(2400 - 100))
        
        component1CountDiff.append(component1CountAlt[counter] - component1Count[counter])
        component2CountDiff.append(component2CountAlt[counter] - component2Count[counter])
        component3CountDiff.append(component3CountAlt[counter] - component3Count[counter])
        component1ToW1CountDiff.append(component1ToW1CountAlt[counter] - component1ToW1Count[counter])
        component1ToW2CountDiff.append(component1ToW2CountAlt[counter] - component1ToW2Count[counter])
        component1ToW3CountDiff.append(component1ToW3CountAlt[counter] - component1ToW3Count[counter])
        component2ToW2CountDiff.append(component2ToW2CountAlt[counter] - component2ToW2Count[counter])
        component3ToW3CountDiff.append(component3ToW3CountAlt[counter] - component3ToW3Count[counter])
        product1CountDiff.append(product1CountAlt[counter] - product1Count[counter])
        product2CountDiff.append(product2CountAlt[counter] - product2Count[counter])
        product3CountDiff.append(product3CountAlt[counter] - product3Count[counter])
        idleTimeInspector1Diff.append(idleTimeInspector1Alt[counter] - idleTimeInspector1[counter])
        idleTimeInspector2Diff.append(idleTimeInspector2Alt[counter] - idleTimeInspector2[counter])
        idleTimeWorkstation1Diff.append(idleTimeWorkstation1Alt[counter] - idleTimeWorkstation1[counter])
        idleTimeWorkstation2Diff.append(idleTimeWorkstation2Alt[counter] - idleTimeWorkstation2[counter])
        idleTimeWorkstation3Diff.append(idleTimeWorkstation3Alt[counter] - idleTimeWorkstation3[counter])
        product1ThroughputDiff.append(product1ThroughputAlt[counter] - product1Throughput[counter])
        product2ThroughputDiff.append(product2ThroughputAlt[counter] - product2Throughput[counter])
        product3ThroughputDiff.append(product3ThroughputAlt[counter] - product3Throughput[counter]) 

        entities.resetVariables()
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
    
    
    component1CountMeanAlt = np.mean(component1CountAlt)
    component2CountMeanAlt = np.mean(component2CountAlt)
    component3CountMeanAlt = np.mean(component3CountAlt)
    component1CountVarianceAlt = stat.variance(component1CountAlt)
    component2CountVarianceAlt = stat.variance(component2CountAlt)
    component3CountVarianceAlt = stat.variance(component3CountAlt)
    component1CountCIAlt = mean_confidence_interval(component1CountAlt)
    component2CountCIAlt = mean_confidence_interval(component2CountAlt)
    component3CountCIAlt = mean_confidence_interval(component3CountAlt)
    
    component1ToW1CountMeanAlt = np.mean(component1ToW1CountAlt)
    component1ToW2CountMeanAlt = np.mean(component1ToW2CountAlt)
    component1ToW3CountMeanAlt = np.mean(component1ToW3CountAlt)
    component2ToW2CountMeanAlt = np.mean(component2ToW2CountAlt)     
    component3ToW3CountMeanAlt = np.mean(component3ToW3CountAlt)
    component1ToW1CountVarianceAlt = stat.variance(component1ToW1CountAlt)
    component1ToW2CountVarianceAlt = stat.variance(component1ToW2CountAlt)
    component1ToW3CountVarianceAlt = stat.variance(component1ToW3CountAlt)
    component2ToW2CountVarianceAlt = stat.variance(component2ToW2CountAlt)
    component3ToW3CountVarianceAlt = stat.variance(component3ToW3CountAlt)
    component1ToW1CountCIAlt = mean_confidence_interval(component1ToW1CountAlt)
    component1ToW2CountCIAlt = mean_confidence_interval(component1ToW2CountAlt)
    component1ToW3CountCIAlt = mean_confidence_interval(component1ToW3CountAlt)
    component2ToW2CountCIAlt = mean_confidence_interval(component2ToW2CountAlt)    
    component3ToW3CountCIAlt = mean_confidence_interval(component3ToW3CountAlt)
                
    product1CountMeanAlt = np.mean(product1CountAlt)
    product2CountMeanAlt = np.mean(product2CountAlt)
    product3CountMeanAlt = np.mean(product3CountAlt)
    product1CountVarianceAlt = stat.variance(product1CountAlt)
    product2CountVarianceAlt = stat.variance(product2CountAlt)
    product3CountVarianceAlt = stat.variance(product3CountAlt)
    product1CountCIAlt = mean_confidence_interval(product1CountAlt)
    product2CountCIAlt = mean_confidence_interval(product2CountAlt)
    product3CountCIAlt = mean_confidence_interval(product3CountAlt)

    idleTimeInspector1MeanAlt = np.mean(idleTimeInspector1Alt)
    idleTimeInspector2MeanAlt = np.mean(idleTimeInspector2Alt)
    idleTimeWorkstation1MeanAlt = np.mean(idleTimeWorkstation1Alt)
    idleTimeWorkstation2MeanAlt = np.mean(idleTimeWorkstation2Alt)
    idleTimeWorkstation3MeanAlt = np.mean(idleTimeWorkstation3Alt)
    idleTimeInspector1VarianceAlt = stat.variance(idleTimeInspector1Alt)
    idleTimeInspector2VarianceAlt = stat.variance(idleTimeInspector2Alt)
    idleTimeWorkstation1VarianceAlt = stat.variance(idleTimeWorkstation1Alt)
    idleTimeWorkstation2VarianceAlt = stat.variance(idleTimeWorkstation2Alt)
    idleTimeWorkstation3VarianceAlt = stat.variance(idleTimeWorkstation3Alt)
    idleTimeInspector1CIAlt = mean_confidence_interval(idleTimeInspector1Alt)
    idleTimeInspector2CIAlt = mean_confidence_interval(idleTimeInspector2Alt)
    idleTimeWorkstation1CIAlt = mean_confidence_interval(idleTimeWorkstation1Alt)
    idleTimeWorkstation2CIAlt = mean_confidence_interval(idleTimeWorkstation2Alt)
    idleTimeWorkstation3CIAlt = mean_confidence_interval(idleTimeWorkstation3Alt)
    
    product1ThroughputMeanAlt = np.mean(product1ThroughputAlt)
    product1ThroughputVarianceAlt = stat.variance(product1ThroughputAlt)
    product1ThroughputCIAlt = mean_confidence_interval(product1ThroughputAlt)
    product2ThroughputMeanAlt = np.mean(product2ThroughputAlt)
    product2ThroughputVarianceAlt = stat.variance(product2ThroughputAlt)
    product2ThroughputCIAlt = mean_confidence_interval(product2ThroughputAlt)  
    product3ThroughputMeanAlt = np.mean(product3ThroughputAlt)
    product3ThroughputVarianceAlt = stat.variance(product3ThroughputAlt)
    product3ThroughputCIAlt = mean_confidence_interval(product3ThroughputAlt)      
    
    component1CountMeanDiff = np.mean(component1CountDiff)
    component2CountMeanDiff = np.mean(component2CountDiff)
    component3CountMeanDiff = np.mean(component3CountDiff)
    component1CountVarianceDiff = stat.variance(component1CountDiff)
    component2CountVarianceDiff = stat.variance(component2CountDiff)
    component3CountVarianceDiff = stat.variance(component3CountDiff)
    component1CountCIDiff = mean_confidence_interval(component1CountDiff)
    component2CountCIDiff = mean_confidence_interval(component2CountDiff)
    component3CountCIDiff = mean_confidence_interval(component3CountDiff)
    
    component1ToW1CountMeanDiff = np.mean(component1ToW1CountDiff)
    component1ToW2CountMeanDiff = np.mean(component1ToW2CountDiff)
    component1ToW3CountMeanDiff = np.mean(component1ToW3CountDiff)
    component2ToW2CountMeanDiff = np.mean(component2ToW2CountDiff)     
    component3ToW3CountMeanDiff = np.mean(component3ToW3CountDiff)
    component1ToW1CountVarianceDiff = stat.variance(component1ToW1CountDiff)
    component1ToW2CountVarianceDiff = stat.variance(component1ToW2CountDiff)
    component1ToW3CountVarianceDiff = stat.variance(component1ToW3CountDiff)
    component2ToW2CountVarianceDiff = stat.variance(component2ToW2CountDiff)
    component3ToW3CountVarianceDiff = stat.variance(component3ToW3CountDiff)
    component1ToW1CountCIDiff = mean_confidence_interval(component1ToW1CountDiff)
    component1ToW2CountCIDiff = mean_confidence_interval(component1ToW2CountDiff)
    component1ToW3CountCIDiff = mean_confidence_interval(component1ToW3CountDiff)
    component2ToW2CountCIDiff = mean_confidence_interval(component2ToW2CountDiff)    
    component3ToW3CountCIDiff = mean_confidence_interval(component3ToW3CountDiff)
                
    product1CountMeanDiff = np.mean(product1CountDiff)
    product2CountMeanDiff = np.mean(product2CountDiff)
    product3CountMeanDiff = np.mean(product3CountDiff)
    product1CountVarianceDiff = stat.variance(product1CountDiff)
    product2CountVarianceDiff = stat.variance(product2CountDiff)
    product3CountVarianceDiff = stat.variance(product3CountDiff)
    product1CountCIDiff = mean_confidence_interval(product1CountDiff)
    product2CountCIDiff = mean_confidence_interval(product2CountDiff)
    product3CountCIDiff = mean_confidence_interval(product3CountDiff)

    idleTimeInspector1MeanDiff = np.mean(idleTimeInspector1Diff)
    idleTimeInspector2MeanDiff = np.mean(idleTimeInspector2Diff)
    idleTimeWorkstation1MeanDiff = np.mean(idleTimeWorkstation1Diff)
    idleTimeWorkstation2MeanDiff = np.mean(idleTimeWorkstation2Diff)
    idleTimeWorkstation3MeanDiff = np.mean(idleTimeWorkstation3Diff)
    idleTimeInspector1VarianceDiff = stat.variance(idleTimeInspector1Diff)
    idleTimeInspector2VarianceDiff = stat.variance(idleTimeInspector2Diff)
    idleTimeWorkstation1VarianceDiff = stat.variance(idleTimeWorkstation1Diff)
    idleTimeWorkstation2VarianceDiff = stat.variance(idleTimeWorkstation2Diff)
    idleTimeWorkstation3VarianceDiff = stat.variance(idleTimeWorkstation3Diff)
    idleTimeInspector1CIDiff = mean_confidence_interval(idleTimeInspector1Diff)
    idleTimeInspector2CIDiff = mean_confidence_interval(idleTimeInspector2Diff)
    idleTimeWorkstation1CIDiff = mean_confidence_interval(idleTimeWorkstation1Diff)
    idleTimeWorkstation2CIDiff = mean_confidence_interval(idleTimeWorkstation2Diff)
    idleTimeWorkstation3CIDiff = mean_confidence_interval(idleTimeWorkstation3Diff)
    
    product1ThroughputMeanDiff = np.mean(product1ThroughputDiff)
    product1ThroughputVarianceDiff = stat.variance(product1ThroughputDiff)
    product1ThroughputCIDiff = mean_confidence_interval(product1ThroughputDiff)
    product2ThroughputMeanDiff = np.mean(product2ThroughputDiff)
    product2ThroughputVarianceDiff = stat.variance(product2ThroughputDiff)
    product2ThroughputCIDiff = mean_confidence_interval(product2ThroughputDiff)  
    product3ThroughputMeanDiff = np.mean(product3ThroughputDiff)
    product3ThroughputVarianceDiff = stat.variance(product3ThroughputDiff)
    product3ThroughputCIDiff = mean_confidence_interval(product3ThroughputDiff)     
    
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
        
        print("Original Design")
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
        
        print("Alternate Design")
        print("Component 1 Inspected - Mean: ", component1CountMeanAlt, ", Variance: ", component1CountVarianceAlt, ", CI: ", component1CountCIAlt)
        print("Component 2 Inspected - Mean: ", component2CountMeanAlt, ", Variance: ", component2CountVarianceAlt, ", CI: ", component2CountCIAlt)
        print("Component 3 Inspected - Mean: ", component3CountMeanAlt, ", Variance: ", component3CountVarianceAlt, ", CI: ", component3CountCIAlt)
        print("Queue C1W1 Output - Mean: ", component1ToW1CountMeanAlt, ", Variance: ", component1ToW1CountVarianceAlt, ", CI: ", component1ToW1CountCIAlt)
        print("Queue C1W2 Output - Mean: ", component1ToW2CountMeanAlt, ", Variance: ", component1ToW2CountVarianceAlt, ", CI: ", component1ToW2CountCIAlt)
        print("Queue C1W3 Output - Mean: ", component1ToW3CountMeanAlt, ", Variance: ", component1ToW3CountVarianceAlt, ", CI: ", component1ToW3CountCIAlt)
        print("Queue C2W2 Output - Mean: ", component2ToW2CountMeanAlt, ", Variance: ", component2ToW2CountVarianceAlt, ", CI: ", component2ToW2CountCIAlt)
        print("Queue C3W3 Output - Mean: ", component3ToW3CountMeanAlt, ", Variance: ", component3ToW3CountVarianceAlt, ", CI: ", component3ToW3CountCIAlt)
        print("Product 1 Produced - Mean: ", product1CountMeanAlt, ", Variance: ", product1CountVarianceAlt, ", CI: ", product1CountCIAlt)
        print("Product 2 Produced - Mean: ", product2CountMeanAlt, ", Variance: ", product2CountVarianceAlt, ", CI: ", product2CountCIAlt)
        print("Product 3 Produced - Mean: ", product3CountMeanAlt, ", Variance: ", product3CountVarianceAlt, ", CI: ", product3CountCIAlt)
        print("Proportion Inspector1 Idle - Mean: ", idleTimeInspector1MeanAlt, ", Variance: ", idleTimeInspector1VarianceAlt, ", CI: ", idleTimeInspector1CIAlt)
        print("Proportion Inspector2 Idle - Mean: ", idleTimeInspector2MeanAlt, ", Variance: ", idleTimeInspector2VarianceAlt, ", CI: ", idleTimeInspector2CIAlt)
        print("Proportion Workstation1 Idle - Mean: ", idleTimeWorkstation1MeanAlt, ", Variance: ", idleTimeWorkstation1VarianceAlt, ", CI: ", idleTimeWorkstation1CIAlt)
        print("Proportion Workstation2 Idle - Mean: ", idleTimeWorkstation2MeanAlt, ", Variance: ", idleTimeWorkstation2VarianceAlt, ", CI: ", idleTimeWorkstation2CIAlt)
        print("Proportion Workstation3 Idle - Mean: ", idleTimeWorkstation3MeanAlt, ", Variance: ", idleTimeWorkstation3VarianceAlt, ", CI: ", idleTimeWorkstation3CIAlt)
        print("Product 1 Throughput - Mean: ", product1ThroughputMeanAlt, ", Variance: ", product1ThroughputVarianceAlt, ", CI: ", product1ThroughputCIAlt)
        print("Product 2 Throughput - Mean: ", product2ThroughputMeanAlt, ", Variance: ", product2ThroughputVarianceAlt, ", CI: ", product2ThroughputCIAlt)
        print("Product 3 Throughput - Mean: ", product3ThroughputMeanAlt, ", Variance: ", product3ThroughputVarianceAlt, ", CI: ", product3ThroughputCIAlt)  
        
        print("Comparing Results")
        print("Component 1 Inspected - Mean: ", component1CountMeanDiff, ", Variance: ", component1CountVarianceDiff, ", CI: ", component1CountCIDiff)
        print("Component 2 Inspected - Mean: ", component2CountMeanDiff, ", Variance: ", component2CountVarianceDiff, ", CI: ", component2CountCIDiff)  
        print("Component 3 Inspected - Mean: ", component3CountMeanDiff, ", Variance: ", component3CountVarianceDiff, ", CI: ", component3CountCIDiff)
        print("Queue C1W1 Output - Mean: ", component1ToW1CountMeanDiff, ", Variance: ", component1ToW1CountVarianceDiff, ", CI: ", component1ToW1CountCIDiff)
        print("Queue C1W2 Output - Mean: ", component1ToW2CountMeanDiff, ", Variance: ", component1ToW2CountVarianceDiff, ", CI: ", component1ToW2CountCIDiff)
        print("Queue C1W3 Output - Mean: ", component1ToW3CountMeanDiff, ", Variance: ", component1ToW3CountVarianceDiff, ", CI: ", component1ToW3CountCIDiff)
        print("Queue C2W2 Output - Mean: ", component2ToW2CountMeanDiff, ", Variance: ", component2ToW2CountVarianceDiff, ", CI: ", component2ToW2CountCIDiff)
        print("Queue C3W3 Output - Mean: ", component3ToW3CountMeanDiff, ", Variance: ", component3ToW3CountVarianceDiff, ", CI: ", component3ToW3CountCIDiff)
        print("Product 1 Produced - Mean: ", product1CountMeanDiff, ", Variance: ", product1CountVarianceDiff, ", CI: ", product1CountCIDiff)
        print("Product 2 Produced - Mean: ", product2CountMeanDiff, ", Variance: ", product2CountVarianceDiff, ", CI: ", product2CountCIDiff)
        print("Product 3 Produced - Mean: ", product3CountMeanDiff, ", Variance: ", product3CountVarianceDiff, ", CI: ", product3CountCIDiff)
        print("Proportion Inspector1 Idle - Mean: ", idleTimeInspector1MeanDiff, ", Variance: ", idleTimeInspector1VarianceDiff, ", CI: ", idleTimeInspector1CIDiff)
        print("Proportion Inspector2 Idle - Mean: ", idleTimeInspector2MeanDiff, ", Variance: ", idleTimeInspector2VarianceDiff, ", CI: ", idleTimeInspector2CIDiff)
        print("Proportion Workstation1 Idle - Mean: ", idleTimeWorkstation1MeanDiff, ", Variance: ", idleTimeWorkstation1VarianceDiff, ", CI: ", idleTimeWorkstation1CIDiff)
        print("Proportion Workstation2 Idle - Mean: ", idleTimeWorkstation2MeanDiff, ", Variance: ", idleTimeWorkstation2VarianceDiff, ", CI: ", idleTimeWorkstation2CIDiff)
        print("Proportion Workstation3 Idle - Mean: ", idleTimeWorkstation3MeanDiff, ", Variance: ", idleTimeWorkstation3VarianceDiff, ", CI: ", idleTimeWorkstation3CIDiff)
        print("Product 1 Throughput - Mean: ", product1ThroughputMeanDiff, ", Variance: ", product1ThroughputVarianceDiff, ", CI: ", product1ThroughputCIDiff)
        print("Product 2 Throughput - Mean: ", product2ThroughputMeanDiff, ", Variance: ", product2ThroughputVarianceDiff, ", CI: ", product2ThroughputCIDiff)
        print("Product 3 Throughput - Mean: ", product3ThroughputMeanDiff, ", Variance: ", product3ThroughputVarianceDiff, ", CI: ", product3ThroughputCIDiff)          
        
        
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

        
def plotData(data, name):
    xList = []
    yList = []
    timeElapsed = 0.0
    for val in data:
        timeElapsed += val[1]
        xList.append(timeElapsed)
        yList.append(val[0])
    plt.figure(figsize=(18,6))
    axis = plt.subplot()
    axis.set_title("Capacity of Queue " + name)
    axis.set_xlabel("Simulation Time (Minutes)")
    axis.set_ylabel("Capacity")        
    plt.plot(xList, yList)
    
    

    #simulation_env = simpy.Environment()
    #workstation1 = entities.Workstation1(simulation_env, workstation1_servicetimes)
    #workstation2 = entities.Workstation2(simulation_env, workstation2_servicetimes)
    #workstation3 = entities.Workstation3(simulation_env, workstation3_servicetimes)
    #inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3, False, inspector1component1_servicetimes)
    #inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3, inspector2component2_servicetimes, inspector2component3_servicetimes, random_2_3)
    #minutes = 2400
    #simulation_env.run(minutes)
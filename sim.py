import simpy
import entities

def sim():
    simulation_env = simpy.Environment()
    workstation1 = entities.WorkStation1(simulation_env)
    workstation2 = entities.WorkStation2(simulation_env)
    workstation3 = entities.WorkStation3(simulation_env)
    inspector1 = entities.Inspector1(simulation_env, workstation1, workstation2, workstation3)
    inspector2 = entities.Inspector2(simulation_env, workstation2, workstation3)
    simulation_env.run(5000)
    print('Finished Simulation')
    print('{}{}'.format("WorkStation 1 produced ",workstation1.productCount) + " of Product 1")
    print('{}{}'.format("WorkStation 2 produced ",workstation2.productCount) + " of Product 2")
    print('{}{}'.format("WorkStation 3 produced ",workstation3.productCount) + " of Product 3")
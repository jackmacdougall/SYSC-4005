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
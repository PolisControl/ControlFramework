from Framework import Simulation
import numpy as np 

runner1 = Simulation(0)
A = np.array([1, 2])
print(A.shape)
runner1.State_Space(np.array([1, 2]), np.array([1, 0]), np.array([1, 0]), np.array([0, 0]))

runner1.numericalIV(0, 15, "Euler", 40, 10)

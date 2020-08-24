import numpy as np
A = np.array([ [.005,.14], [.03,.03] ])
b = np.array([50,20])
z = np.linalg.solve(A,b)
print(z)

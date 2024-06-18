
import numpy as np

a = np.array([[1, -1, 1, -2], 
              [9, -1, 1, 8], 
              [-7, 8, 0, -6], 
              [3, -5, 0, -6]], float)

b = np.array([-20, 60, -60, -44], float)

solution = np.linalg.solve(a, b)
print("Решение матричным методом:", solution)

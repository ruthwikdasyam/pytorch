import torch
import numpy as np


# torch from list
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
# print((x_data))

np_array = np.array(data)
np_tensor = torch.tensor(np_array)
# print(np_tensor)

# ones_like and rand_like
x_ones = torch.ones_like(x_data)
print(x_ones)
x_rand = torch.rand_like(x_data, dtype=torch.float)#not implemented for long
print(x_rand)


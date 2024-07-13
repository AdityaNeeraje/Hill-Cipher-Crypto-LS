import numpy as np

with open("output_mod0.txt") as file:
    data=np.array([int(x.strip()) for x in file.readlines()])

with open("output_mod1.txt") as file:
    data=np.vstack((data, np.array([int(x.strip()) for x in file.readlines()])))
with open("output_mod2.txt") as file:
    data=np.vstack((data, np.array([int(x.strip()) for x in file.readlines()])))
with open("output_mod3.txt") as file:
    data=np.vstack((data, np.array([int(x.strip()) for x in file.readlines()])))
data=data.T.flatten()
print(list(data))
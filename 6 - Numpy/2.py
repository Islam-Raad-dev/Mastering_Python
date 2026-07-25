# ----------------------------
# -- Numpy => Create Arrays --
# ----------------------------

import numpy as np

# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)

# Type

print(type(my_list))
print(type(my_array))

print("#" * 50)

# Accessing Elements

print(my_list[0])
print(my_array[0])

print("#" * 50)

a = np.array(10)
b = np.array([10, 20])
c = np.array([[1, 2], [4, 5]])
d = np.array([[[3, 2], [3, 4]], [[5, 6], [7, 8]]])

print(d[1, 1, -1])


print("#" * 50)

# Number Of Dimensions



print("#" * 50)

# Custom Dimensions



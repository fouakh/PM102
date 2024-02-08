import numpy as np
import matplotlib.pyplot as plt

num_points = 1
radius = 3

sample_order = 8
sample = 5

width, height = 500, 500

x = np.arange(0, width, 1)
y = np.arange(0, height, 1)
X, Y = np.meshgrid(x, y) 

random_x = np.random.randint(0, width, num_points)
random_y = np.random.randint(0, height, num_points)

image = np.zeros((height, width))

# For random points
# for i in range(num_points):
#     image += (X - random_x[i]) ** 2 + (Y - random_y[i]) ** 2 <= radius ** 2
# image[random_y, random_x] = 1

image[width // 2, height // 2] = 1


x = np.arange(0, width, 1)
y = np.arange(0, height, 1)
X, Y = np.meshgrid(x, y) 

plt.imshow(image, cmap='gray')
plt.axis("off")
plt.show()

np.savetxt(f"Dirac{num_points}-{sample}s{sample_order}.dat", image, header=f"sampling_step = {sample}e-0{sample_order}\nwavelength = 5e-07")


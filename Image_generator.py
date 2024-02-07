import numpy as np
import matplotlib.pyplot as plt

num_points = 5
radius = 3
sample_order = 7

width, height = 500, 500

x = np.arange(0, width, 1)
y = np.arange(0, height, 1)
X, Y = np.meshgrid(x, y) 

random_x = np.random.randint(0, width, num_points)
random_y = np.random.randint(0, height, num_points)

image = np.zeros((height, width))
for i in range(num_points):
    image += (X - random_x[i]) ** 2 + (Y - random_y[i]) ** 2 <= radius ** 2
# image[random_y, random_x] = 1

x = np.arange(0, width, 1)
y = np.arange(0, height, 1)
X, Y = np.meshgrid(x, y) 

plt.imshow(image, cmap='gray')
plt.axis("off")
plt.show()

np.savetxt(f"Circles{num_points}-s{sample_order}.dat", image, header=f"sampling_step = 1.0e-0{sample_order}\nwavelength = 5e-07")


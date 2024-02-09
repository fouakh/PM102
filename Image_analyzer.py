import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

data = np.loadtxt('Dirac1-1s3.result20240209112501.dat', dtype=complex)

ift = np.fft.ifftshift(data)
ift = np.fft.ifft2(ift)
ift = np.fft.ifftshift(ift)
ift = ift.real

point1 = (207, 224)
point2 = (292, 275)


plt.scatter(*point1, color='red', marker='o', s=50, label='Point 1')
plt.scatter(*point2, color='blue', marker='o', s=50, label='Point 2')

line = ConnectionPatch(point1, point2, "data", "data", color="y", linestyle="--")
plt.gca().add_artist(line)

pixels = np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
wavelength = 5e-07
sampling_step = 1e-03

# 2 Rectangle 2.44 Circle
length = 2 * wavelength / (pixels * sampling_step) * 1e+06

plt.imshow(abs(data), cmap='gray')
plt.axis("off")
plt.annotate(f'Distance: {pixels:.2f} pixels\nLen: {length:.12f} micro m',
             xy=(0.5, 0.01),
             xycoords='axes fraction',
             ha='center',
             fontsize=10,
             color='white')

plt.legend()
plt.show()



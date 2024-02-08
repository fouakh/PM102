import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Diracs5-s7.result20240208100437.dat', dtype=complex)

ift = np.fft.ifftshift(data)
ift = np.fft.ifft2(ift)
ift = np.fft.ifftshift(ift)
ift = ift.real

threshold = 0.00001
thresholded_data = np.where(data < threshold, 0, 1)

plt.imshow(abs(data), cmap='gray')
plt.axis("off")
plt.show()

# wavelength = 5e-07
# sampling_step = 1e-08
# pixels = 10
# print(2.44 * wavelength / (pixels * sampling_step) )
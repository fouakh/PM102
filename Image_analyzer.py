import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Diracs5-s5.result20240207170652.dat', dtype=complex)

ift = np.fft.ifftshift(data)
ift = np.fft.ifft2(ift)
ift = np.fft.ifftshift(ift)
ift = ift.real

plt.imshow(abs(data), cmap='gray')
plt.axis("off")

plt.show()
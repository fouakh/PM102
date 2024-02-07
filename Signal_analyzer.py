import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('Data_for_filtre.result-mystere-D-s1e+06-sin1kHz-to-sin100kHz.dat',
                     names=True,
                     dtype=complex,
                     delimiter='\n')
sampling_step = 1e-06

data = [t[0] for t in data]

time = np.arange(0, len(data) * sampling_step, sampling_step)

# Calcul de la FFT
fft_result = np.fft.fft(data)
freq = np.fft.fftfreq(len(data), sampling_step)


magnitude_fft = np.abs(fft_result)
phase_fft = np.angle(fft_result)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time, data, label='Signal temporel')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.xlim(0, 0.1)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(freq, magnitude_fft, label='Module de la FFT')
plt.xlabel('Fréquence')
plt.ylabel('Module')

plt.legend()

plt.subplot(3, 1, 3)
plt.plot(freq, phase_fft, label='Phase de la FFT')
plt.xlabel('Fréquence')
plt.ylabel('Phase')
plt.legend()

plt.tight_layout()
plt.show()


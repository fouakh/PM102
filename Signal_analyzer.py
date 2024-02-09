import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('dirac-1s8.result20240209091426.dat' , dtype=complex,)
sampling_step = 1e-08

time = np.arange(0, len(data) * sampling_step, sampling_step)

# Calcul de la FFT
fft_result = np.fft.fft(data)
freq = np.fft.fftfreq(len(data), sampling_step)

magnitude_fft = np.abs(fft_result)
phase_fft = np.angle(fft_result)
max_mag = np.max(magnitude_fft)
cutoff_mag = max_mag / np.sqrt(2)
cutoff_index = np.argmax(magnitude_fft <= cutoff_mag)

print(f'Cutoff Frequency:\t{freq[cutoff_index]}\tHz')

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(time, abs(data), label='h(t)')
plt.xlabel('Time')
plt.ylabel('Magnitude')
#plt.xlim(0, 0.005)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(freq, magnitude_fft, label='|H(f)|')
plt.xlabel('Frequence')
plt.ylabel('Magnitude')
plt.axvline(x=freq[cutoff_index], color='r', linestyle='--', label='Cutoff Frequency')
plt.legend()


plt.tight_layout()
plt.show()



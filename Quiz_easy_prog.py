import numpy as np
import matplotlib.pyplot as plt
import random as rd

data = np.loadtxt('Quiz_0602.dat')
pas = 0.0001

time = np.arange(0, len(data)* pas, pas)
fft_result = np.fft.fft(data)
freq = np.fft.fftfreq(len(data), time[1] - time[0])

fig, axs = plt.subplots(2, 1, figsize=(6, 6))
    
for i, ax in enumerate(axs):     
    if i == 0:
        ax.set_ylabel(r'$|F(x\rightarrow\sin(mx))(f)|$')
        ax.scatter(freq, np.abs(fft_result), color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$|(F)|$')  
    else:
        ax.scatter(freq, np.angle(fft_result), color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$\phi(F)$')
        ax.set_ylabel(r'$\phi(F(x\rightarrow\sin(mx))(f))$')
        
    ax.set_xlabel(r'$f$')
    #ax.set_xlim(-2, 2)  
    ax.legend()

plt.show()

index_sorted = np.argsort(np.abs(fft_result))
max_index = index_sorted[-6:]
max_freq = np.sort(freq[max_index])[3:]
print(max_freq)
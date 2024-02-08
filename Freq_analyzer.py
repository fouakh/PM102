import numpy as np
import matplotlib.pyplot as plt
import random as rd

data = np.loadtxt('Quiz_normal_001.dat')
step = 0.001

more_data = result_array = np.concatenate((data, np.zeros(1000000)))
time = np.arange(0, len(more_data)* step, step)
window = [305, 315]

fft_result = np.fft.fft(more_data)
freq = np.fft.fftfreq(len(more_data), time[1] - time[0])
magnitude_fft = np.abs(fft_result)
phase_fft = np.angle(fft_result)*180/np.pi

fig, axs = plt.subplots(3, 1, figsize=(6, 7))

index_start = np.where(np.abs(freq - window[0]) < 0.1)[0][0]
index_finish = np.where(np.abs(freq - window[1]) < 0.1)[0][0]
index_sorted = np.argsort(magnitude_fft[index_start:index_finish])
max_index = index_sorted[-1]
print(f"frequence = {freq[index_start + max_index]}")
print(f"Amplitude = {magnitude_fft[index_start + max_index]*2/len(more_data)}")
print(f"Phase = {phase_fft[index_start + max_index]}")
    
for i, ax in enumerate(axs):      
    if i == 0:
        ax.set_ylabel(r'$|F(f)|$')
        ax.scatter(freq[index_start:index_finish], magnitude_fft[index_start:index_finish], color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$|(F)|$')
        #ax.set_xlim(window[0], window[1])  
    elif i == 1:
        ax.scatter(freq, phase_fft, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$\phi(F)$')
        ax.set_ylabel(r'$\phi(F(f))$')
        ax.set_xlim(window[0], window[1])
    else:
        ax.scatter(time, more_data, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$f(t)$')
        ax.set_ylabel(r'$f(t)$')
        #ax.set_xlim(1, 1.2)
    ax.grid(True)
    ax.set_xlabel(r'$f$')  
    ax.legend()

plt.show()

###############################################################

# import numpy as np
# import matplotlib.pyplot as plt
# import random as rd

# path = '/c/Users/admin/PH102'
# data = np.loadtxt('Quiz_normal_001.dat')
# pas = 0.001

# time = np.arange(0, len(data)* pas, pas)
# freq = np.arange(0, 1/pas, 1/(len(data)*3*pas))
# scalar_prod = 0*freq

# for i,f in enumerate(freq) : 
#     ejx = np.exp(2j*np.pi*f*time)
#     scalar_prod[i] = np.abs(np.dot(ejx,data))

# freq_min, freq_max = 50, 100
# index = np.where((freq >= freq_min) & (freq <= freq_max))
# index_max = index[0][np.argmax(scalar_prod[index])]
# print(freq[index_max])


# # plt.scatter(freq, scalar_prod, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1)
# # plt.show()
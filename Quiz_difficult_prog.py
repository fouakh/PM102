import numpy as np
import matplotlib.pyplot as plt
import random as rd

data = np.loadtxt('Quiz_0602_5.dat')
pas = 1e-07

more_data = result_array = np.concatenate((data, np.zeros(100000)))
time = np.arange(0, len(more_data)* pas, pas)
window1 = [200000, 300000]
window = [2.8e+06, 3.0e+06]
window3 = [4.1e+06, 4.4e+06]

fft_result = np.fft.fft(more_data)
freq = np.fft.fftfreq(len(more_data), time[1] - time[0])
magnitude_fft = np.abs(fft_result)
phase_fft = np.angle(fft_result)*180/np.pi

fig, axs = plt.subplots(3, 1, figsize=(6, 7))

# index_start = np.where(np.abs(freq - window[0]) < 1000)[0][0] 
# index_finish = np.where(np.abs(freq - window[1]) < 1000)[0][0]
index_start = 0
index_finish = -1
index_sorted = np.argsort(magnitude_fft[index_start:index_finish])
max_index = index_sorted[-1]
print(f"frequence = {freq[index_start + max_index]}")
print(f"Amplitude = {magnitude_fft[index_start + max_index]*2/len(data)}")
print(f"Phase = {180 + phase_fft[index_start + max_index]}")
    
for i, ax in enumerate(axs):      
    if i == 0:
        ax.set_ylabel(r'$|F(f)|$')
        ax.scatter(freq[index_start:index_finish], magnitude_fft[index_start:index_finish], color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$|(F)|$')
        #ax.set_xlim(window[0], window[1])  
    elif i == 1:
        ax.scatter(freq, phase_fft, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$\phi(F)$')
        ax.set_ylabel(r'$\phi(F(f))$')
        #ax.set_xlim(window[0], window[1])
    else:
        ax.scatter(time[0:len(data)], data, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$f(t)$')
        ax.set_ylabel(r'$f(t)$')
        #ax.set_xlim(1, 1.2)
    ax.grid(True)
    ax.set_xlabel(r'$f$')  
    ax.legend()

plt.show()

###############################################

# import numpy as np
# import matplotlib.pyplot as plt
# import random as rd

# path = '/c/Users/admin/PH102'
# data = np.loadtxt('Quiz_difficult_002.dat')
# pas = 1e-05

# def first_and_last_values_condition(array, condition):
#     indices = np.where(condition(array))[0]
#     if len(indices) == 0:
#         return None, None 
#     first_index = indices[0]
#     last_index = indices[-1]

#     return first_index, last_index

# time = np.arange(0, len(data)* pas, pas)
# min, max = first_and_last_values_condition(data, lambda x: np.abs(x) < 0.01)

# cut_data = data[min:max]
# print(min, max)

# fft_result = np.fft.fft(cut_data)
# freq = np.fft.fftfreq(len(cut_data), time[1] - time[0])
# magnitude_fft = np.abs(fft_result)
# phase_fft = np.angle(fft_result)*180/np.pi

# fig, axs = plt.subplots(3, 1, figsize=(6, 7))
    
# for i, ax in enumerate(axs):  
    
#     if i == 0:
#         ax.set_ylabel(r'$|F(f)|$')
#         ax.scatter(freq, magnitude_fft, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$|(F)|$')
#         ax.set_xlim(10000, 30000)  
#     elif i == 1:
#         ax.scatter(freq, phase_fft, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$\phi(F)$')
#         ax.set_ylabel(r'$\phi(F(f))$')
#         ax.set_xlim(10000, 30000)
#     else:
#         ax.scatter(time[min:max], cut_data, color=f'#{rd.randint(0, 0xFFFFFF):06x}', s=1, label=r'$f(t)$')
#         ax.set_ylabel(r'$f(t)$')
#         #ax.set_xlim(0, 0.05)
#     ax.grid(True)
#     ax.set_xlabel(r'$f$')  
#     ax.legend()

# plt.show()

# index_sorted = np.argsort(magnitude_fft)
# max_index = index_sorted[-4:]
# print(f"frequence = {freq[max_index]}")
# print(f"Amplitude = {magnitude_fft[max_index]*2/len(cut_data)}")
# print(f"Phase = {180 + phase_fft[max_index]}")
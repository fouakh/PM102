import numpy as np

frequency = [10, 50, 100, 500, 1000, 5000, 10000]

num_points = 100000
start_time = 0
end_time = 1
sampling_rate = (end_time - start_time) / num_points

time = np.arange(start_time, end_time, sampling_rate)
data = np.zeros(num_points)
for f in frequency:
    data += np.sin(2 * np.pi * f * time)

file_path = 'Data_for_filtre.s1e+07-sin1kHz-to-sin1MHz.dat'
np.savetxt(file_path, data, delimiter='\n', header='sampling_step = 1e-06')

print(f"The data has been saved to {file_path}.")
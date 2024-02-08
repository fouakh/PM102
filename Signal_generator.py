import numpy as np

sample = 5
sample_order = 8
number_points = 10000

sampling_rate = sample * 10 ** (-sample_order)

time = np.arange(0, number_points*sampling_rate, sampling_rate)
data = np.zeros(len(time))
data[0] = 1

file_name = f"dirac-{sample}s{sample_order}.dat"
np.savetxt(file_name, data, delimiter='\n', header=f"sampling_step = {sample}e-0{sample_order}")

print(f"The data has been saved\t{file_name}")
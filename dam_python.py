from scipy.io import readsav
from sunpy.time import parse_time
import matplotlib.pyplot as plt


t_start = '2015-07-24 13:30'
t_end = '2015-07-24 14:30'

a = readsav('sav_test_dam.sav', python_dict = True)
dam = a['dam']
names = dam.dtype.names

spec_array = dam.image[0]
freqs = dam.freq[0]
JD = dam.JD[0]
temps = dam.temps[0]
time_arr = dam.anytim[0]
delta_t = dam.delta_t[0]

dam_times = []
for i in range(len(time_arr)):
	dam_times.append(parse_time(time_arr[i]))

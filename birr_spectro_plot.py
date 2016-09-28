import numpy as np
import matplotlib.pyplot as plt
from sunpy import lightcurve as lc
from sunpy.spectra.sources.callisto import CallistoSpectrogram
import scipy
smooth = scipy.ndimage.filters.uniform_filter 
from sunpy.time import parse_time
basetime=parse_time('1979-01-01 00:00:00')

t_start ='2015-11-04 13:00'
t_end ='2015-11-04 14:30'
start_time_day = '2015-11-04 00:00'


g = lc.GOESLightCurve.create(t_start, t_end)
gl = g.data['xrsb']


d = CallistoSpectrogram.from_range('BIR', t_start, t_end)
c = d.subtract_bg()

y = (parse_time(start_time_day) - basetime).total_seconds() + d.t_init
new_time = d.time_axis + y

callisto_times = []
for i in range(len(new_time)):
	callisto_times.append(parse_time(new_time[i]))


c.plot(cmap = 'viridis')

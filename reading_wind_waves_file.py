import numpy as np
import datetime
import matplotlib.pyplot as plt

filename = 'WI_H1_WAV_2500.txt'

f = open(filename, 'r')
lines = f.readlines()

li = []
for i in range(len(lines)):
	if lines[i][0] != '#':
		li.append(lines[i])


freqs_string = li[1].split('(@_')[1:]
freq = []
for i in range(len(freqs_string)):
	freq.append(int(freqs_string[i].split('_kHz')[0]))

freq = np.array(freq)
freq = freq*1./1000 #freq in MHz

time_array = []
alll = []
for i in range(3, len(li)):

	s = li[i].split(' ')
	ss = []
	for i in range(len(s)):
		if s[i] != '':	
			ss.append(s[i])
	ss[-1] = ss[-1].split('\n')[0]
	for i in range(2, len(ss)):
		ss[i] = float(ss[i])
	time_array.append(datetime.datetime.strptime(ss[0] + ' ' + ss[1][0:8], '%d-%m-%Y %H:%M:%S'))
	alll.append(ss[2:])
#date = datetime.datetime.strptime(ss[0] + ' ' + ss[1], '%d-%m-%Y %H:%M:%S.%f')


a = np.array(alll)
plt.imshow(a.T, aspect = 'auto', cmap = 'viridis')
xticks = []
yticks = []
xlabels = []
ylabels = []
for i in range(0, len(freq),20):
	yticks.append(i)
	ylabels.append(str(freq[i]))	
	

for i in range(0, len(time_array),20):
	xticks.append(i)
	xlabels.append(str(time_array[i])[11:])
plt.xticks(xticks, xlabels)
plt.yticks(yticks, ylabels)
plt.xlabel('Start time ' + str(time_array[0]) + ' UT')
plt.ylabel('Freq (MHz)')
plt.show()

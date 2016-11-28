from astropy.io import fits
from sunpy.time import parse_time
basetime=parse_time('1979-01-01 00:00:00')
start_time_day = '2014-04-18 00:00'
##################################################
## Code to read ORFEE fits files dynamic spectra #
##################################################

file_name = 'ext_orf140418_1229_1331.fts'
fx = fits.open(file_name, memmap = True)

#-----------#
#freq arrays#
#-----------#

orfee_axis = fx[1]
freq_b1 = orfee_axis.data['FREQ_B1']
freq_b2 = orfee_axis.data['FREQ_B2']
freq_b3 = orfee_axis.data['FREQ_B3']
freq_b4 = orfee_axis.data['FREQ_B4']
freq_b5 = orfee_axis.data['FREQ_B5']

#---------------#
#Spectra arrays #
#---------------#

orfee_image = fx[2]
#orfee_image.name 

TIME_B1 = orfee_image.data['time_b1']/1000.0
STOKESI_B1 = orfee_image.data['stokesi_b1']
STOKESV_B1 = orfee_image.data['stokesv_b1']
TIME_B2 = orfee_image.data['time_b2']/1000.0
STOKESI_B2 = orfee_image.data['stokesi_b2']
STOKESV_B2 = orfee_image.data['stokesv_b2']
TIME_B3 = orfee_image.data['time_b3']/1000.0
STOKESI_B3 = orfee_image.data['stokesi_b3']
STOKESV_B3 = orfee_image.data['stokesv_b3']
TIME_B4 = orfee_image.data['time_b4']/1000.0
STOKESI_B4 = orfee_image.data['stokesi_b4']
STOKESV_B4 = orfee_image.data['stokesv_b4']
TIME_B5 = orfee_image.data['time_b4']/1000.0
STOKESI_B5 = orfee_image.data['stokesi_b5']
STOKESV_B5 = orfee_image.data['stokesv_b5']

all_data = np.concatenate((STOKESI_B1.T, STOKESI_B2.T, STOKESI_B3.T, STOKESI_B4.T, STOKESI_B5.T))

all_time = np.concatenate((TIME_B1, TIME_B2, TIME_B3, TIME_B4, TIME_B5))

#function to make time array into datetime array
def make_datetime(time_ar):
	time_array = []
	for i in range(len(time_ar)):
		y = parse_time((parse_time(start_time_day) - basetime).total_seconds() + time_ar[i])	
		time_array.append(y)
	return time_array

t_b1 = make_datetime(TIME_B1)
t_b2 = make_datetime(TIME_B2)
t_b3 = make_datetime(TIME_B3)
t_b4 = make_datetime(TIME_B4)
t_b5 = make_datetime(TIME_B5)



## pandas series of freq (205MHz) that interested in

#pulsations = Series(STOKESI_B1[:,150], index = t_b1).truncate('2014-04-18 12:54', '2014-04-18 12:58') #205mhz
pulsations1 = Series(STOKESI_B1[:,315], index = t_b1).truncate('2014-04-18 12:54', '2014-04-18 12:58') #270Mhz
pulsations3 = Series(STOKESI_B1[:,207], index = t_b1).truncate('2014-04-18 12:54', '2014-04-18 12:58')#228 mhz
pulsations2 = Series(STOKESI_B2[:,15], index = t_b2).truncate('2014-04-18 12:54', '2014-04-18 12:58') #327mhz

###Fourier analysis function##
def fourier_ana(x,dt):
	N = len(x)
	dt = dt
	df = 1./(N*dt)
	PSD = abs(dt*fftpack.fft(x)[:N/2])**2
	f = df*np.arange(N/2)
	plt.plot(1./f, PSD)
	plt.xlim(0,100)
	A = np.where(PSD == max(PSD))[0][0]
	return f, PSD


#plotting
import seaborn as sns
sns.set_style('ticks',{'xtick.direction':'in','ytick.direction':'in'})
sns.set_context('paper')

import matplotlib as mpl
label_size = 15
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 

plt.figure(figsize=(15, 10))
test = STOKESI_B1[...,100:315] #slicing columns from 186 - 270 MHz
test = test[16401:17001] #truncating from 12:56:20 - 12:57:20
test_freq = freq_b1[100:315]
test_time = t_b1[16401:17001]


xx = [0,100,200,300,400,500]
xticks = []
for i in xx:
	xticks.append(str(test_time[i])[11:19])
#l = np.locgical_and(test_freq > 200, test_freq <201)
#np.where(l == True)
yy = [36, 87, 137, 189]
yticks = test_freq[yy]
for i in range(len(yticks)):
	yticks[i] = str(yticks[i])[0:3]

cmap = 'magma_r'

plt.imshow(test.T, aspect = 'auto', cmap = cmap)
plt.xticks(xx, xticks)
plt.yticks(yy, yticks)
plt.title('Orfee Spectrogram', fontsize = 20)
plt.ylabel('Frequencies (MHz)', fontsize = 20)
plt.xlabel('Start time ' + str(test_time[0])[0:19] + ' UT', fontsize = 20)
plt.tight_layout()

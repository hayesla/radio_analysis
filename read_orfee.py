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




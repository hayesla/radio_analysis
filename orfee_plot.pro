pro plot_ORFEE

!p.background=0                                      
!p.color=255

time_start='12:30:00'
time_end='13:30:00'

loadct,5


file='ext_orf140418_1229_1331.fts'
day='2014-apr-18 00:00:00'
orfee_axis=mrdfits(file,1,header) 

orfee_image=mrdfits(file,2,header) 
time_b1=(orfee_image.time_b1/1d3)+anytim(day,/utim)
time_b2=(orfee_image.time_b2/1d3)+anytim(day,/utim)
time_b3=(orfee_image.time_b3/1d3)+anytim(day,/utim)
time_b4=(orfee_image.time_b4/1d3)+anytim(day,/utim)
time_b5=(orfee_image.time_b5/1d3)+anytim(day,/utim)

orfee_1=rotate(orfee_image.stokesi_b1,3)
orfee_2=rotate(orfee_image.stokesi_b2,3)
orfee_3=rotate(orfee_image.stokesi_b3,3)
orfee_4=rotate(orfee_image.stokesi_b4,3)
orfee_5=rotate(orfee_image.stokesi_b5,3)

orfee = constbacksub( orfee_1, /auto)

spectro_plot,sigrange( orfee < 50),time_b1,reverse(orfee_axis.freq_b1 ),xstyle=st,charsize=1.2,$

xrange='2014-apr-18 '+[time_start,time_end],/xs,$

/ys,ytitle='Frequency [MHz]',/notitle


spectro_plot,sigrange(orfee_1),time_b1,reverse(orfee_axis.freq_b1),yrange=yrange,/ys,/xs,/notitle,/noerase,/over,charsize=1.2,timerange='2015-mar-12 '+[time_start,time_end],/ylog
spectro_plot,sigrange(orfee_2),time_b2,reverse(orfee_axis.freq_b2),yrange=yrange,/ys,/xs,/notitle,/noerase,/over,charsize=1.2,timerange='2015-mar-12 '+[time_start,time_end],/ylog
spectro_plot,sigrange(orfee_3),time_b3,reverse(orfee_axis.freq_b3),yrange=yrange,/ys,/xs,/notitle,/noerase,/over,charsize=1.2,timerange='2015-mar-12 '+[time_start,time_end],/ylog
spectro_plot,sigrange(orfee_4),time_b4,reverse(orfee_axis.freq_b4),yrange=yrange,/ys,/xs,/notitle,/noerase,/over,charsize=1.2,timerange='2015-mar-12 '+[time_start,time_end],/ylog
spectro_plot,sigrange(orfee_5),time_b5,reverse(orfee_axis.freq_b5),yrange=yrange,/ys,/xs,/notitle,/noerase,/over,charsize=1.2,timerange='2015-mar-12 '+[time_start,time_end],/ylog



;save, orfee_image, filename = 'orfee_sav_file.sav'
stop
end


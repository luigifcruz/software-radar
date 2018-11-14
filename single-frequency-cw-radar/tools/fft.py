import numpy as np
import scipy.signal as signal
import scipy.interpolate as sp
import matplotlib.pyplot as plt

#a = np.fromfile('radar_small.bin', dtype='complex64')
cdata = np.fromfile('radar.bin', dtype='complex64')

Fs_y = 976
fft_size = 256

plt.specgram(cdata, NFFT=fft_size, Fs=Fs_y)  
plt.title("Radar")  
plt.ylim(-Fs_y/2, Fs_y/2)  
plt.xlim(0,len(cdata)/Fs_y)  
plt.ticklabel_format(style='plain', axis='y')  
plt.show()

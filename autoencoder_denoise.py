'''
remove noise frome ECG signal using a trained autocoder
@author: Kemeng Chen
'''

from numpy import genfromtxt
import numpy as np 
import matplotlib.pyplot as plt 
import os
import sys
from util import*

def noise_removal(file_name):
	fs=360
	file_path=os.path.join(os.getcwd(), 'data', file_name)
	if not os.path.isfile(file_path):
		raise AssertionError(file_path, 'not found')

	beats=genfromtxt(file_path, delimiter=',')
	[num_beats, beat_lgth]=np.shape(beats)
	model_name='test_model.meta'
	model_path=os.path.join(os.getcwd(), 'models')
	nr_model=restore_model(model_path, model_name)
	dn_beats=nr_model.run_model(beats)

	lgth=num_beats*beat_lgth
	index=np.arange(lgth)/fs
	ecg=np.reshape(beats, [lgth])
	ecg_rec=np.reshape(dn_beats, [lgth])

	fig, ax=plt.subplots()
	ax.plot(index, ecg, 'b', label='Noisy ECG')
	ax.plot(index, ecg_rec, 'r', label='De-noised ECG')
	ax.set_title('Noise removal using autoencoder')
	ax.tick_params(direction='in', length=1)
	ax.set_xlim([index[0], index[lgth-1]])
	ax.set_xlabel('Time [sec]')
	ax.grid()
	ax.legend()
	plt.show()


if __name__ == '__main__':
	if len(sys.argv)<2:
		raise ValueError('No file name specified')
	noise_removal(sys.argv[1])

import pandas as pd 
import os as os
import numpy as np 
from pylab import * 
from datetime import datetime, timedelta
import shutil
from dateutil.relativedelta import relativedelta
from scipy.signal import butter, filtfilt
from itertools import cycle
from dateutil.relativedelta import relativedelta
from scipy.signal import butter, filtfilt, resample
from nptdms import TdmsFile
import matplotlib.pyplot as plt


#Define Data Directory

data_dir = '../Data/'

#Define output directory

output_dir = '../Charts/'

#Loop through tests

for test in os.listdir(data_dir):
	fig=plt.figure()

	# Create figure with set x-axis, set size, and available tools in bokeh package
	# output_file(output_location + chart + '.html',mode='cdn')



	# Define 20 color pallet using RGB values. 
	# Must be done under chart loop so each chart starts with the same colors
	tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
				(44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
				(148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
				(227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
				(188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
	color=cycle(['r','b','g','k','y','m'])
	plot_markers = cycle(['s', 'o', '^', 'd', 'h', 'p','v','8','D','*','<','>','H'])
	for i in range(len(tableau20)):
		r, g, b = tableau20[i]
		tableau20[i] = (r / 255., g / 255., b / 255.)

	for f in os.listdir(data_dir+str(test)+'/'):
		if f.endswith('.csv'):
			print(data_dir+str(test)+'/'+str(f))
			data_df = pd.read_csv(data_dir+str(test)+'/'+str(f), skiprows = 9)

			start_time = datetime.strptime(data_df['Time'][0],'%I:%M:%S %p')
			#H:MM:SS time format
			ignition = start_time+timedelta(seconds =60)
			end_test = start_time+timedelta(seconds =120)

			time_ls = pd.Series(datetime.strptime(t,'%I:%M:%S %p') for t in data_df['Time'])
			data_df = data_df.set_index('Time')
			# print(data_df)



			elapsed_time= pd.Series([(t-start_time).total_seconds() for t in time_ls])
			print(elapsed_time)


			plt.plot(elapsed_time, data_df['Process'],ls='-',markevery=1,marker=next(plot_markers),label=f[:-3],color=next(color))


	plt.grid(True)
	plt.xlabel('Time (s)', fontsize=16)
	plt.ylabel('Temperature ($^{\circ}$C)', fontsize=16)
	plt.ylim([0,400])
	# plt.xlim([300,350])
	plt.xticks(fontsize=16)
	plt.yticks(fontsize=16)
	ax1 = plt.gca()
	handles1, labels1 = ax1.get_legend_handles_labels()		
	fig.set_size_inches(10, 7)				
	# plt.title('Experiment '+str(experiment)+' '+chart, y=1.08)
	plt.tight_layout()	
	plt.legend(handles1, labels1,  loc='upper left', fontsize=12, handlelength=1)	
	plt.savefig(output_dir + str(test) + '.pdf')
	plt.close('all')


import numpy as np
import matplotlib.pyplot as rdm
import statistics as st

def data(file,kolom):
    data = np.genfromtxt(file, delimiter='\t')
    databaru = []
    if kolom == 2:
        for i in data[:38,kolom]:
            if not np.isnan(i):
                databaru.append(i+0.11)
    else:
        for i in data[:38,kolom]:
            if not np.isnan(i):
                databaru.append(i+0.011)
    return databaru

dataporo = data('34-29b.dat',3)
dataperm = data('34-29b.dat',2)
datalogperm = data('34-29b.dat',4)

print('koefisien korelasi porositas-permeabilitas',st.corr_coeff(dataporo,dataperm))
print('koefisien korelasi porositas-logpermeabilitas',st.corr_coeff(dataporo,datalogperm))
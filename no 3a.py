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


print('Kovarian data Porositas-Permeabilitas:',st.cov_data(dataporo,dataperm))
print('Kovarian data Porostias-Log Permeabilitas:',st.cov_data(dataporo,datalogperm))

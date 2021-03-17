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

b_0, b_1 = st.lin_reg(dataporo,datalogperm)
Y_kalkulasi = [b_0+x*b_1 for x in dataporo]

b = st.lsq_reg(dataporo,datalogperm)
Y_kalkulasi_lse = [b[0]+x*b[1] for x in dataporo]

rdm.scatter(datalogperm, dataporo, label='Data Observasi')
rdm.plot(Y_kalkulasi, dataporo, label='Regresi-Kovariansi')
rdm.plot(Y_kalkulasi_lse, dataporo, '--r', label='Regresi LSE')
rdm.xlabel('Log Permeabilitas')
rdm.ylabel('Porositas')
rdm.ylim(max(dataporo), 0)
rdm.legend()
rdm.show()
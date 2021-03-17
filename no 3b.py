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

data1 = data('34-29b.dat',3)
data2 = data('34-29b.dat',2)
data3 = data('34-29b.dat',4)


fig, axs = rdm.subplots(3,3)

for j,i in enumerate([1,2,3]):

    a,b = st.auto_corr(data1,i+1)
    c,d = st.auto_corr(data2,i+1)
    e,f = st.auto_corr(data3,i+1)

    axs[0,j].plot(b,a)
    axs[0,j].set_title('Permeabilitas')
    axs[0,j].set_ylabel('Auto Korelasi')
    axs[0,j].set_xlabel('Lag')
    axs[0,j].grid(True)

    axs[1,j].plot(d,c)
    axs[1,j].set_title('Porositas')
    axs[1,j].set_ylabel('Koefisien Korelasi')
    axs[1,j].set_xlabel('Lag')
    axs[1,j].grid(True)

    axs[2,j].plot(f,e)
    axs[2,j].set_title('Log Permeabilitas')
    axs[2,j].set_ylabel('Koefisien Korelasi')
    axs[2,j].set_xlabel('Lag')
    axs[2,j].grid(True)


rdm.show()
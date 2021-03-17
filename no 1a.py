#119120087_Bernard Cavin Ronlei_TGA
import numpy as np
import matplotlib.pyplot as rdm

def data(file,kolom):
    data = np.genfromtxt(file, delimiter='\t')
    databaru = []
    if kolom == 2:
        for i in data[:38,kolom]:
            if not np.isnan(i):
                databaru.append(i+0.87)
    else:
        for i in data[:38,kolom]:
            if not np.isnan(i):
                databaru.append(i+0.087)
    return databaru

dataporositas = data('34-29b.dat',3)

kelas = int(len(dataporositas)**0.5)

frekuensi, bins, patches = rdm.hist(dataporositas, kelas, density=True, facecolor='pink', alpha=0.75)
rdm.ylabel('Frekuensi')
rdm.xlabel('Porositas [v/v]')
rdm.grid(True)
rdm.show()
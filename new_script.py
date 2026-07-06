import numpy as np
from matplotlib import pyplot as plt
import camb

# Ρύθμιση παραμέτρων
h0_val = 67.5
pars = camb.set_params(H0=h0_val, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06, As=2e-9, ns=0.965, lmax=3000)
results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')

# Δημιουργία των 4 subplots
fig, ax = plt.subplots(2, 2, figsize=(12, 12))
totCL = powers['total']
ls = np.arange(totCL.shape[0])

# Σχεδιασμός των 4 καμπυλών (TT, EE, BB, TE)
ax[0, 0].plot(ls, totCL[:, 0]); ax[0, 0].set_title('TT')
ax[0, 1].plot(ls, totCL[:, 1]); ax[0, 1].set_title('EE')
ax[1, 0].plot(ls, totCL[:, 2]); ax[1, 0].set_title('BB')
ax[1, 1].plot(ls, totCL[:, 3]); ax[1, 1].set_title('TE')

# Αποθήκευση όλου του σχήματος (και των 4 μαζί)
plt.savefig(f'all_spectra_H0_{int(h0_val)}.png')
print("All 4 spectra saved in one image!")

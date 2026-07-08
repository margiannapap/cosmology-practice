import numpy as np
from matplotlib import pyplot as plt
import camb

# 1. Ορισμός συνάρτησης για υπολογισμό spectra (για να μην γράφουμε τα ίδια διπλά)
def get_spectra(H0_val):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0_val, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06)
    pars.InitPower.set_params(As=2e-9, ns=0.965)
    pars.set_for_lmax(3000, lens_potential_accuracy=1)
    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')
    return powers['total'] # Επιστρέφει τα 'total' (lensed) spectra

# 2. Υπολογισμός για τα δύο μοντέλα
cl_67 = get_spectra(67.5)
cl_73 = get_spectra(73.0)
ls = np.arange(cl_67.shape[0])

# 3. Δημιουργία του plot
fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# Labels και τίτλοι για τα subplots
labels = [r'$TT$', r'$EE$', r'$TE$']
indices = [0, 1, 3] # Τα indices για TT, EE, TE στο totCL

for i in range(3):
    idx = indices[i]
    ax[i].plot(ls, cl_67[:, idx], label='H0 = 67.5')
    ax[i].plot(ls, cl_73[:, idx], label='H0 = 73.0')
    ax[i].set_title(labels[i])
    ax[i].set_xlim([2, 3000])
    ax[i].set_xlabel(r'$\ell$')
    ax[i].legend()

plt.tight_layout()
plt.savefig('CMB_H0_comparison.png')
plt.show()

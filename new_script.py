import numpy as np
from matplotlib import pyplot as plt
import camb

# Define parameters (You can change H0 here!)
# H0 = 67.5 is the baseline (Planck 2018 value)
# Try changing it to 75.0 to see the shift in the peaks
h0_val = 75.0

pars = camb.set_params(
    H0=h0_val, 
    ombh2=0.022, 
    omch2=0.122, 
    mnu=0.06, 
    omk=0, 
    tau=0.06, 
    As=2e-9, 
    ns=0.965, 
    halofit_version='mead', 
    lmax=3000
)

results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')

totCL = powers['total']
ls = np.arange(totCL.shape[0])

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(ls, totCL[:, 0], label=f'H0 = {h0_val}')
ax.set_title(r'$TT$ Power Spectrum')
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$D_\ell [\mu K^2]$')
ax.set_xlim([2, 2500])
ax.legend()

# Save the plot automatically
filename = f'spectrum_H0_{int(h0_val)}.png'
plt.savefig(filename)
print(f"Plot saved as {filename}")

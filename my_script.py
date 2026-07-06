import numpy as np
from matplotlib import pyplot as plt
import camb

# Set up the cosmological parameters according to the standard model (LambdaCDM)
# We use the defaults provided by the official CAMB documentation
pars = camb.set_params(
    H0=67.5, 
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

# Calculate the cosmological results based on the defined parameters
results = camb.get_results(pars)

# Retrieve the CMB power spectra dictionary
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')

# Extract lensed and unlensed scalar power spectra for comparison
totCL = powers['total']
unlensedCL = powers['unlensed_scalar']
ls = np.arange(totCL.shape[0])

# Initialize the figure to plot TT, EE, and TE spectra
fig, ax = plt.subplots(2, 2, figsize=(12, 12))

# Plot TT power spectrum (Lensed vs Unlensed)
ax[0, 0].plot(ls, totCL[:, 0], color='k', label='Lensed')
ax[0, 0].plot(ls, unlensedCL[:, 0], color='C2', label='Unlensed')
ax[0, 0].set_title(r'$TT\, [\mu K^2]$')
ax[0, 0].legend()

# Plot the fractional difference caused by lensing in TT
ax[0, 1].plot(ls[2:], 1 - unlensedCL[2:, 0] / totCL[2:, 0])
ax[0, 1].set_title(r'Fractional TT lensing')

# Plot EE power spectrum
ax[1, 0].plot(ls, totCL[:, 1], color='k')
ax[1, 0].plot(ls, unlensedCL[:, 1], color='C2')
ax[1, 0].set_title(r'$EE\, [\mu K^2]$')

# Plot TE power spectrum
ax[1, 1].plot(ls, totCL[:, 3], color='k')
ax[1, 1].plot(ls, unlensedCL[:, 3], color='C2')
ax[1, 1].set_title(r'$TE\, [\mu K^2]$')

# Set labels and axis limits for all subplots
for a in ax.reshape(-1):
    a.set_xlim([2, 3000])
    a.set_xlabel(r'$\ell$')

plt.tight_layout()
plt.show()

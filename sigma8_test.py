import camb
import numpy as np
import matplotlib.pyplot as plt

# Setup basic parameters
pars = camb.CAMBparams()
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122)
pars.set_matter_power(redshifts=[0.0], kmax=2.0)

# Function to calculate power spectrum for a given sigma8
def get_pk(sigma8_val):
    # Fiducial As
    As = 2e-9
    pars.InitPower.set_params(As=As, ns=0.965)
    results = camb.get_results(pars)
    s8_fid = results.get_sigma8_0()
    
    # Scale As to get desired sigma8
    pars.InitPower.set_params(As=As * sigma8_val**2 / s8_fid**2, ns=0.965)
    results = camb.get_results(pars)
    kh, z, pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=2, npoints=200)
    return kh, pk[0]

# Calculate for two different sigma8 values
kh, pk1 = get_pk(0.7)
kh, pk2 = get_pk(0.9)

# Plot
plt.loglog(kh, pk1, label='sigma8 = 0.7')
plt.loglog(kh, pk2, label='sigma8 = 0.9')
plt.xlabel('k [h/Mpc]')
plt.ylabel('P(k)')
plt.legend()
plt.savefig('sigma8_comparison.png')
print("Plot saved as sigma8_comparison.png")

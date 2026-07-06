import camb
import numpy as np
import matplotlib.pyplot as plt

# 1. Setup the cosmological parameters
pars = camb.CAMBparams()
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122)
pars.InitPower.set_params(ns=0.965)

# 2. Get the base result to define totCL
pars.set_for_lmax(2500, lens_potential_accuracy=1)
results = camb.get_results(pars)
totCL = results.get_lensed_scalar_cls(CMB_unit='muK')
ls = np.arange(totCL.shape[0])

# 3. Calculate results with varying accuracy levels
# The lensing B-modes are non-linear, so they need to be calculated carefully
pars.set_for_lmax(2500, lens_potential_accuracy=1)
results = camb.get_results(pars)
lmax2500CL = results.get_lensed_scalar_cls(CMB_unit='muK')

pars.set_for_lmax(4000, lens_potential_accuracy=1)
results = camb.get_results(pars)
lmax4000CL = results.get_lensed_scalar_cls(CMB_unit='muK')

pars.set_for_lmax(4000, lens_potential_accuracy=2)
results = camb.get_results(pars)
accCL = results.get_lensed_scalar_cls(CMB_unit='muK')

pars.set_for_lmax(6000, lens_potential_accuracy=4)
results = camb.get_results(pars)
refCL = results.get_lensed_scalar_cls(CMB_unit='muK')

# 4. Plotting the results
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

# We use [:len(ls)] to make sure all arrays have the same length as the base 'ls'
ax[0].plot(ls, totCL[:len(ls), 2], color='C0', label='Default accuracy')
ax[0].plot(ls, lmax2500CL[:len(ls), 2], color='C1', label='lmax=2500, acc=1')
ax[0].plot(ls, lmax4000CL[:len(ls), 2], color='C2', label='lmax=4000, acc=1')
ax[0].plot(ls, accCL[:len(ls), 2], color='C3', label='lmax=4000, acc=2')
ax[0].plot(ls, refCL[:len(ls), 2], color='k', label='Reference')

# ... και το ίδιο για το fractional error ...
ax[1].plot(ls[2:], totCL[2:len(ls), 2] / refCL[2:len(ls), 2] - 1, color='C0')
ax[1].plot(ls[2:], lmax2500CL[2:len(ls), 2] / refCL[2:len(ls), 2] - 1, color='C1')
ax[1].plot(ls[2:], lmax4000CL[2:len(ls), 2] / refCL[2:len(ls), 2] - 1, color='C2')
ax[1].plot(ls[2:], accCL[2:len(ls), 2] / refCL[2:len(ls), 2] - 1, color='C3')

# Save the plot automatically
plt.savefig('lensing_accuracy.png')
print("The plot has been saved as 'lensing_accuracy.png'")
plt.show()

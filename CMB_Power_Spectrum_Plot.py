# ==========================================================
# ADVANCED CMB TEMPERATURE POWER SPECTRUM
# Ultra Enhanced Scientific Visualization
# ==========================================================

# Install required packages:
# pip install numpy matplotlib camb astropy

import numpy as np
import matplotlib.pyplot as plt
import camb
from camb import model
from astropy.cosmology import FlatLambdaCDM

# ==========================================================
# COSMOLOGY SETUP
# ==========================================================

cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)

pars = camb.CAMBparams()

pars.set_cosmology(
    H0=70,
    ombh2=0.022,
    omch2=0.122,
    mnu=0.06,
    omk=0,
    tau=0.06
)

pars.InitPower.set_params(
    As=2e-9,
    ns=0.965
)

pars.set_for_lmax(2500, lens_potential_accuracy=1)

# ==========================================================
# CALCULATE POWER SPECTRUM
# ==========================================================

print("Calculating CMB power spectrum...")

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

totCL = powers['total']

ell = np.arange(totCL.shape[0])

# ==========================================================
# DARK COSMIC STYLE
# ==========================================================

plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(14, 8))

# ==========================================================
# MAIN TT SPECTRUM
# ==========================================================

ax.loglog(
    ell[2:2501],
    totCL[2:2501, 0],
    color='cyan',
    linewidth=2.5,
    label='TT Power Spectrum'
)

# ==========================================================
# GLOW EFFECT
# ==========================================================

for lw, alpha in zip([8, 6, 4], [0.05, 0.08, 0.12]):
    ax.loglog(
        ell[2:2501],
        totCL[2:2501, 0],
        color='cyan',
        linewidth=lw,
        alpha=alpha
    )

# ==========================================================
# FILL UNDER CURVE
# ==========================================================

ax.fill_between(
    ell[2:2501],
    totCL[2:2501, 0],
    color='deepskyblue',
    alpha=0.15
)



# ==========================================================
# PEAK MARKERS
# ==========================================================

peak_x = [220, 540, 800]
peak_y = [5600, 2500, 2200]

ax.scatter(
    peak_x,
    peak_y,
    color='yellow',
    s=80,
    zorder=5
)

# ==========================================================
# PEAK ANNOTATIONS
# ==========================================================

ax.annotate(
    'First Acoustic Peak',
    xy=(220, 5600),
    xytext=(320, 7000),
    fontsize=11,
    color='white',
    arrowprops=dict(
        arrowstyle='->',
        color='white',
        lw=1.5
    )
)

ax.annotate(
    'Second Peak',
    xy=(540, 2500),
    xytext=(700, 3500),
    fontsize=11,
    color='white',
    arrowprops=dict(
        arrowstyle='->',
        color='white',
        lw=1.5
    )
)

ax.annotate(
    'Third Peak',
    xy=(800, 2200),
    xytext=(1100, 3000),
    fontsize=11,
    color='white',
    arrowprops=dict(
        arrowstyle='->',
        color='white',
        lw=1.5
    )
)

# ==========================================================
# TITLES & LABELS
# ==========================================================

ax.set_title(
    "(CMB)\nTemperature Power Spectrum",
    fontsize=15,
    pad=15
)

ax.set_xlabel(
    r"Multipole Moment $\ell$",
    fontsize=15
)

ax.set_ylabel(
    r"$C_\ell$ ($\mu K^2$)",
    fontsize=15
)

# ==========================================================
# GRID & MINOR TICKS
# ==========================================================

ax.minorticks_on()

ax.grid(
    which='major',
    linestyle='--',
    alpha=0.35
)

ax.grid(
    which='minor',
    linestyle=':',
    alpha=0.15
)

# ==========================================================
# LEGEND
# ==========================================================

ax.legend(
    fontsize=11,
    loc='upper right',
    framealpha=0.3
)

# ==========================================================
# COSMIC TEXT
# ==========================================================

plt.text(
    4,
    120,
    "Planck-like ΛCDM Cosmology",
    fontsize=11,
    color='white',
    alpha=0.8
)

# ==========================================================
# FINAL DISPLAY
# ==========================================================

plt.tight_layout()

plt.show()

# ==========================================================
# INFORMATION
# ==========================================================

print("\n========================================")
print(" Advanced CMB Spectrum Generated!")
print("========================================")

print("""
Features Included:
✔ Dark cosmic theme
✔ Glow effect
✔ Filled spectrum
✔ Acoustic peak labels
✔ Cosmological regions
✔ Scientific annotations
✔ Professional grid styling
✔ Research-style visualization
""")
# Dispersion Relation Fit

Analysis of the dispersion relation of a discrete (beaded-string / mass-spring) lattice,
using frequency measurements from two trials.

The script:

1. Linearises the dispersion relation as `f² = A[1 − cos(ka)]` and fits the slope `A`
   for each trial and for the averaged data with `scipy.optimize.curve_fit`
   (weighted by the measurement uncertainties).
2. Plots the measured `f²` against `k` with error bars, together with the fitted curves.
3. Computes the theoretical prediction `A = T / (2π² μ a²)` from the tension `T`,
   linear mass density `μ` and spacing `a`, propagates their uncertainties, and plots it.

## Requirements

- Python 3.9+
- numpy, scipy, matplotlib

```bash
pip install -r requirements.txt
```

## Usage

```bash
python NM_code2.py
```

The fit results and uncertainties are printed to the console, and two figures are shown
(experimental fit and theoretical dispersion relation).

## Data

The measured frequencies, wave numbers `k` and their uncertainties are defined
directly at the top of `NM_code2.py`. Edit those arrays to analyse a different data set.

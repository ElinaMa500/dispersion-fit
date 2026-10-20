import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Frequency measurements
f = np.array([
    [6.1, 12.7, 18.8, 23.7, 27.7, 30.0],
    [6.6, 12.6, 18.0, 22.1, 26.0, 30.0]
])

# Individual measurements
f1 = f[0, :]
f2 = f[1, :]

# Average frequencies
favg = np.mean(f, axis=0)

# Standard deviation of frequency measurements
stdfset = np.std(f, axis=0)
print("Standard deviation of frequency measurements:", stdfset)

# Wave numbers and uncertainties
k = np.array([0.02882, 0.05764, 0.08647,
              0.11529, 0.14411, 0.17293])

err_k = np.array([
    1.16299e-4, 4.65195e-4, 0.00105,
    0.00186, 0.00291, 0.00419
])

a = 15.5
err_a = 0.1

# Linearized dispersion model
def linearized_dispersion(x, slope):
    return slope * (1 - x)

# Transform the data
x = np.cos(a * k)
y1 = f1**2
y2 = f2**2
yavg = favg**2

# Uncertainty in frequency squared
df = 0.1

dy1 = 2 * f1 * df
dy2 = 2 * f2 * df
dyavg = 2 * favg * df

print("y_err for Trial 1:", dy1)
print("y_err for Trial 2:", dy2)
print("y_err for Average:", dyavg)

# Curve fitting
popt1, pcov1 = curve_fit(
    linearized_dispersion, x, y1,
    sigma=dy1, absolute_sigma=True
)

popt2, pcov2 = curve_fit(
    linearized_dispersion, x, y2,
    sigma=dy2, absolute_sigma=True
)

popt_avg, pcov_avg = curve_fit(
    linearized_dispersion, x, yavg,
    sigma=dyavg, absolute_sigma=True
)

print("Trial 1 fit:", popt1 , '+-', pcov1)
print("Trial 2 fit:", popt2, '+-', pcov2)
print("Average fit:", popt_avg, '+-', pcov_avg)

# Generate fitted curves
k_fit = np.linspace(min(k), max(k), 500)
x_fit = np.cos(a * k_fit)

y_fit1 = linearized_dispersion(x_fit, popt1[0])
y_fit2 = linearized_dispersion(x_fit, popt2[0])
y_fitavg = linearized_dispersion(x_fit, popt_avg[0])

# Plot data and fits
plt.figure(figsize=(8, 5))

plt.errorbar(k, y1, yerr=dy1, xerr=err_k,
             fmt='o', capsize=3, color='blue',
             label='Trial 1')

plt.errorbar(k, y2, yerr=dy2, xerr=err_k,
             fmt='x', capsize=3, color='green',
             label='Trial 2')

plt.errorbar(k, yavg, yerr=dyavg, xerr=err_k,
             fmt='s', capsize=3, color='black',
             label='Average')

plt.plot(k_fit, y_fit1, color='blue', label='Fit 1')
plt.plot(k_fit, y_fit2, color='green', label='Fit 2')
plt.plot(k_fit, y_fitavg, color='red', label='Average fit')

plt.xlabel("k (rad/m)")
plt.ylabel(r"$f^2$")
plt.title(r"Fit: $f^2 = A[1-\cos(ka)]$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()




T = 29.2
dT = 0.65       # Replace with your uncertainty in T

a = 0.155      # Spacing in metres
da = 0.001     # Uncertainty in spacing, metres

mu = 23.23e-3       # linear mass density (kg/m)
dmu = 0.01e-3

slope = T / (2 * np.pi**2 * mu * a**2)
y_th = slope * (1 - np.cos(k * a))

print(f'Slope: {slope}')

# Propagate uncertainties
factor_a = (k * a) * np.sin(k * a) / (1 - np.cos(k * a)) - 2

y_err = y_th * np.sqrt(
    (dT / T)**2
    + (dmu / mu)**2
    + (factor_a * da / a)**2
)

plt.figure(figsize=(8, 5))
plt.errorbar(k, y_th, yerr=y_err, xerr=err_k,
             fmt='o', capsize=3, color='blue', label='Theory')

plt.xlabel("k (rad/m)")
plt.ylabel(r"$f^2$")
plt.title(r"Theoretical dispersion relation")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Theoretical y values:", y_th)
print("Theoretical y uncertainties:", y_err)



#graph
# import numpy as np
# import matplotlib.pyplot as plt

# k = np.array([0.02882, 0.05764, 0.08647,
#               0.11529, 0.14411, 0.17293])

# f = np.array([
#     [6.1, 12.7, 18.8, 23.7, 27.7, 30],
#     [6.6, 12.6, 18.0, 22.1, 26.0, 30]
# ])

# plt.plot(k, f[0]**2, label="Dataset 1", marker="o")
# plt.plot(k, f[1]**2, label="Dataset 2", marker="x")

# plt.xlabel("k")
# plt.ylabel(r"$f^2$")
# plt.title(r"Graph of $f^2$ against $k$")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
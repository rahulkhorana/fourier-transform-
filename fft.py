import matplotlib.pyplot as plt
import numpy as np
pi = np.pi

PERIOD = 11.278
AMPLITUDE = 19.877

for samples in (0, 1200):
    var_time = np.arange(samples)
    var_amplitude = np.array(AMPLITUDE * np.sin(2 * π * time / PERIOD), dtype=int)
    var_transform_length = samples // 2
    var_sn = np.abs(np.fft.fft(ampl)[:fft_length].real) / samples
    var_frequency  = np.linspace(0, 0.5, fft_length)

    fig, (time_domain, freq_domain) = plt.subplots(1, 1, figsize=(5 + 2*(samples > 1000), 11))
    fig.suptitle("{} samples".format(samples))
    time_domain.bar(var_time, var_amplitude)
    time_domain.set_xlabel("sample number (time sequence)")

    freq_domain.plot(var_frequency, var_sn)
    freq_domain.set_xlabel("Frequency")
    freq_domain.set_title("Fourier transform")

plt.show()

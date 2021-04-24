import numpy as np
from matplotlib import pyplot as plt

def fourier_transform(signal, fs):
    """
    Run a Fourier Transform on a signal
    
    Returns:
        Freq and Magnitude of the signal after running the FFT
    """
    freqs = np.fft.rfftfreq(4*len(signal), 1/fs)
    fft = np.abs(np.fft.rfft(signal, 4*len(signal)))
    return freqs, fft

def plot_specgram(signal, fs):
    plt.figure(figsize=(10, 5))
    plt.specgram(signal, Fs=fs, NFFT=250, noverlap=125, xextent=[0, len(signal) / fs / 60]);
    plt.xlabel('Time (min)')
    plt.ylabel('Frequency (Hz)')

def plot_fft1(signal, fs):
    freq, mag = fourier_transform(signal, fs)
    plt.figure(figsize=(10, 5))
    plt.xlim(0, 6)
    plt.plot(freq, mag)
#     plt.plot(np.fft.rfftfreq(len(signal), 1/fs), np.abs(np.fft.rfft(signal)))
    plt.xlabel('Frequency (Hz)')
    
def plot_fft2(signal, freqs, fft, fs):
    plt.subplot(2,1,1)
    ts = np.arange(len(signal)) / fs
    plt.plot(ts, signal)
    plt.subplot(2,1,2)
    plt.plot(freqs, np.abs(fft))
    plt.title("Frequency Domain")
    plt.xlabel("Frequency (Hz)")
    plt.tight_layout()
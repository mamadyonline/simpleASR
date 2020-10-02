# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:14:37 2020

@author: Ali
"""

import numpy as np
import matplotlib.pyplot as plt
from HTKFeat import MFCC_HTK
from pydub import AudioSegment

# %% Loading wav file
mfcc = MFCC_HTK()

#signal = mfcc.load_rawsignal("samples/SA1.wav")
file = "LaLimace.wav"
signal_raw = AudioSegment.from_wav(file).set_channels(1)
signal = np.frombuffer(signal_raw._data, dtype=np.int16).astype(np.double)
sig_len = signal.size/signal_raw.frame_rate


# %% Visualizing waveform
plt.figure(figsize=(15,4))
t = np.linspace(0, sig_len, signal.size)
plt.plot(t, signal)
plt.xlim(0,sig_len)
plt.figure(figsize=(15,4))
s=plt.specgram(signal, Fs=signal_raw.frame_rate)
plt.colormaps()
plt.xlim(0,sig_len)


#%%
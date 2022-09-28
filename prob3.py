#!/usr/bin/python3

from scipy.io import wavfile
import numpy as np
import sounddevice as sd
from math import pi

import sys

if len(sys.argv) != 2:
    print('please specify number of samples per period (N)')
    exit(1)

N = int(sys.argv[1])  # number of samples per period

F = 440  # 440 Hz

fs = F * N  # sampling rate

f = F/fs  # discrete frequency

samples = 3/(1/fs)  # 3 secs of samples

x = np.arange(0, samples)
y = np.sin(2*pi*f*x)

sd.play(y, fs, blocking=True)  # play sound


print('hola')

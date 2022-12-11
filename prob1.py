#!/usr/bin/python3
import sys
from scipy.io import wavfile

if len(sys.argv) != 2:
    print('please specify name of wav file')
    exit(1)

# Read wav file
fs, data = wavfile.read(sys.argv[1])
print(f'sample rate {fs}')

# Write wav file
wavfile.write(f'cpy_{sys.argv[1]}', fs, data)
print(f'file written')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Example of filespec module usage.

Author: Carlos Galdino
Email: galdino@ifi.unicamp.br
'''


from filespec import *
from pathlib import Path
import matplotlib.pyplot as plt

# import specfile data
data = FileSpec(str(Path(r'..\fixtures\test.specfile')))

# Scan that we want to plot
scan_number = 286

# extract scan data
scan_286 = data.scans[scan_number][0].getData()

# Plot
tth = scan_286[:, 0]
intensity = scan_286[:, 22]

plt.figure()
plt.plot(tth, intensity, xlabel=r'tth', ylabel=r'Intensity')
plt.show()
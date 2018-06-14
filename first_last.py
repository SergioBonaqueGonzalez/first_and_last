"""
@author: Dr. Sergio Bonaque-Gonzalez
Optical Engineer.
sergiob@wooptix.com
"""

def get_fist_last_non_zero_index(line):
    first = next((i for i, x in enumerate(line) if x), None)
    for idx, item in enumerate(line):
        if item != 0:
            last = idx
    return (first, last)

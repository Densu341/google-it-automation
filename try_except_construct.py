#!/usr/bin/env python3

def character_frequency(filename):
    """Return a dictionary of character frequencies for the given file."""
    # Open the file for reading
    try:
        f = open(filename)
    except IOError:
        return None
    
    # Read the file and count the character frequencies
    frequency = {}
    for line in f:
        for char in line:
            frequency[char] = frequency.get(char, 0) + 1
    f.close()
    return frequency
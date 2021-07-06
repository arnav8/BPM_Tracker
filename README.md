# BPM_Tracker

This repo contains three different methods to find the BPM or tempo of the songs. 
[bpm_Wave.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_wave.py)
This is the implementation of a Beats Per Minute (BPM) detection algorithm, as presented in the paper of [G. Tzanetakis, G. Essl and P. Cook titled: "Audio Analysis using the Discrete Wavelet Transform"]( http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.63.5712). Takes a wav file as a command line parameter input and based on the window size, it calculates the bpm. By default the window size is set to 10. But by trial and error, I found out that a 30 second window size does a better job. '''--window 30'''
Dependencies: scipy, numpy, pywavelets, matplotlib
The analysis of their performance and efficiency is depicted below.


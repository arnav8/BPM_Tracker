# BPM_Tracker

This repo contains the three different methods that i ran and tested out, to find the BPM or tempo of an audio. 

## [bpm_Wave.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_wave.py)
* This is the implementation of a Beats Per Minute (BPM) detection algorithm, as presented in the paper of [G. Tzanetakis, G. Essl and P. Cook titled: "Audio Analysis using the Discrete Wavelet Transform"]( http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.63.5712). 
* Takes a wav file as a command line parameter input and based on the window size, it calculates the bpm. By default the window size is set to 10. But by trial and error, I found out that a 30 second window size does a better job. '''--window 30'''
* Dependencies: scipy, numpy, pywavelets, matplotlib


## [bpm_aubio.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_aubio.py)
* Uses the python package [aubio](https://aubio.org/). 
* aubio is a collection of algorithms and tools to label and transform music and sounds. It scans or listens to audio signals and attempts to detect musical events. 
* Aubio is a free and open source software released under the GNU/GPL license and has no required dependencies other than installing aubio python package.

## [bpm_librosa.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_librosa.py)
* Uses the python package [librosa](https://librosa.org/), which does audio and music processing in Python
* It provides the building blocks necessary to create music information retrieval systems.
* Has no required dependencies ther than installing librosa python package..

The analysis of their performance and efficiency is depicted below.


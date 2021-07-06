
# BPM_Tracker

This repo contains the three different methods that i ran and tested out, to find the BPM or tempo of an audio. 

### [bpm_wave.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_wave.py)
* This is the implementation of a Beats Per Minute (BPM) detection algorithm, as presented in the paper of [G. Tzanetakis, G. Essl and P. Cook titled: "Audio Analysis using the Discrete Wavelet Transform"]( http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.63.5712). 
* Takes a wav file as a command line parameter input and based on the window size, it calculates the bpm. By default the window size is set to 10. But by trial and error, I found out that a 30 second window size does a better job.
* Dependencies: scipy, numpy, pywavelets, matplotlib


### [bpm_aubio.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_aubio.py)
* Uses the python package [aubio](https://aubio.org/). 
* aubio is a collection of algorithms and tools to label and transform music and sounds. It scans or listens to audio signals and attempts to detect musical events. 
* Aubio is a free and open source software released under the GNU/GPL license and has no required dependencies other than installing aubio python package.

### [bpm_librosa.py](https://github.com/arnav8/BPM_Tracker/blob/main/bpm_librosa.py)
* Uses the python package [librosa](https://librosa.org/), which does audio and music processing in Python
* It provides the building blocks necessary to create music information retrieval systems.
* Has no required dependencies ther than installing librosa python package..

The analysis of their performance and efficiency is depicted below. We see that bpm_wave performs the best in predicting the correct BPM in the three test audios.\
Test Audio 1 -> I gotta feeling ( by the black eyed peas)\
Test Audio 2 -> Blinding Lights (by the Weeknd)\
Test Audio 3 -> Yesterday ( by the Beatles)\
![rsz_screenshot_from_2021-07-06_17-11-11](https://user-images.githubusercontent.com/60852260/124594293-4253d280-de7d-11eb-8e04-6ed313749ad4.png)
/
![rsz_screenshot_from_2021-07-06_17-12-59](https://user-images.githubusercontent.com/60852260/124594533-88a93180-de7d-11eb-9144-da6d7082f948.png)
/
![rsz_screenshot_from_2021-07-06_17-17-24](https://user-images.githubusercontent.com/60852260/124595025-1e44c100-de7e-11eb-95e9-a575d87d80a8.png)
/

Lastly, I also found this approach for [Beat Tracking using Deep Neural Networks](https://dida.do/blog/beat-tracking-with-deep-neural-networks)

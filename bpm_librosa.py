import librosa

filename = "train3.wav"

#    Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Tempo', round(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#print(beat_times)

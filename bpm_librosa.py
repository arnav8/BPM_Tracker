import librosa

filename = "train3.wav"

y, sr = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Tempo', round(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#print(beat_times)

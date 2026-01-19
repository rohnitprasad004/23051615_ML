import librosa
import numpy as np
import pandas as pd
import os

# Folder containing audio files
audio_folder = "audiofiles"

data_list = []

# Loop through each audio file
for filename in os.listdir(audio_folder):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        file_path = os.path.join(audio_folder, filename)

        # Load audio
        y, sr = librosa.load(file_path)

        # Extract features
        duration = librosa.get_duration(y=y, sr=sr)
        rms = np.mean(librosa.feature.rms(y=y))
        zcr = np.mean(librosa.feature.zero_crossing_rate(y))
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

        # Store results
        data_list.append({
            "File": filename,
            "Duration (sec)": round(duration, 2),
            "RMS Energy": float(rms),
            "Zero Crossing Rate": float(zcr),
            "Spectral Centroid": float(spectral_centroid)
        })

# Convert to DataFrame
df = pd.DataFrame(data_list)

print(df)

# Save CSV
df.to_csv("audio_data.csv", index=False)
print("\nExtracted audio features saved to audio_data.csv")

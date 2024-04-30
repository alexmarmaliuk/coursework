import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import altair as alt

datapath = 'pages/app_data/current_data.csv'
data = pd.read_csv(datapath)

y = np.array(data.y)
x = np.array(data.x)
sr = st.slider('Sample rate', min_value=100, max_value=24000, value=22050)

# Compute the mel spectrogram
S = librosa.feature.melspectrogram(y=y, sr=sr)

# Convert to dB (log scale)
S_dB = librosa.power_to_db(S, ref=np.max)

# Plotting
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-frequency spectrogram')
plt.tight_layout()
plt.show()
st.pyplot()

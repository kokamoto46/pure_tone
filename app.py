#!/usr/bin/env python
# coding: utf-8

# In[6]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title for the application
st.title('Standard pure tone audiometry masking practice application')

# Sidebar for the audiogram controls to keep the layout organized
with st.sidebar:
    # Dropdown menu for selecting the frequency
    frequency = st.selectbox('Frequency to be measured', [250, 500, 1000, 2000, 4000])

    # Adjusting sliders based on the frequency selection
    if frequency == 500:
        max_level = 90
    else:
        max_level = 110

    # Sliders for adjusting the pure tone level and masking noise level
    pure_tone_level = st.slider('Pure tone level (dBHL)', -5, max_level, step=5)
    masking_noise_level = st.slider('Masking noise level (dBHL)', -5, max_level, step=5)

# Logic to light up the "response available" lamp based on the selected frequency and levels
response_message = "No response"
if frequency == 250 and pure_tone_level >= 50:
    response_message = 'Response!'
elif frequency == 500:
    if -20 <= masking_noise_level <= 35 and pure_tone_level >= 95:
        response_message = 'Response!'
    elif masking_noise_level == 40 and pure_tone_level >= 100:
        response_message = 'Response!'
    elif masking_noise_level == 45 and pure_tone_level >= 105:
        response_message = 'Response!'
    elif masking_noise_level >= 50 and pure_tone_level >= 110:
        response_message = 'Response!'
elif frequency == 1000:
    if -20 <= masking_noise_level <= 30 and pure_tone_level >= 90:
        response_message = 'Response!'
    elif masking_noise_level == 35 and pure_tone_level >= 95:
        response_message = 'Response!'
    elif masking_noise_level == 40 and pure_tone_level >= 100:
        response_message = 'Response!'
    elif masking_noise_level >= 45 and pure_tone_level >= 105:
        response_message = 'Response!'
elif frequency == 2000 and pure_tone_level >= 90:
    response_message = 'Response!'
elif frequency == 4000 and pure_tone_level >= 95:
    response_message = 'Response!'

st.sidebar.success(response_message)

# Creating the audiogram diagram
fig, ax = plt.subplots()
frequencies = [250, 500, 1000, 2000, 4000]
levels = [35, 35, 30, 50, 60]

# Converting frequencies to a logarithmic scale for equal spacing
log_freqs = np.log10(frequencies)

ax.plot(log_freqs, levels, 'x--', color='blue', label='Standard Levels')

# Adding the "0" mark based on the pure tone level and selected frequency, adjusting frequency to log scale
if pure_tone_level >= -5:
    ax.plot(np.log10(frequency), pure_tone_level, 'o', color='red', label='Test Level')

# Adjusting the x-axis to show the frequencies as labels but positioned at their logarithmic scale
ax.set_xticks(log_freqs)
ax.set_xticklabels([f"{f} Hz" for f in frequencies])

ax.set_ylim(110, -20)
ax.set_ylabel('Pure tone level (dBHL)')
ax.set_title('Audiogram')
ax.grid(True)
ax.legend()

st.pyplot(fig)

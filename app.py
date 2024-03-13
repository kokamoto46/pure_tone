#!/usr/bin/env python
# coding: utf-8

# In[6]:

import streamlit as st
import matplotlib.pyplot as plt

# Title for the application
st.title('Standard pure tone audiometry masking practice application')

# Sidebar for the audiogram controls to keep the layout organized
with st.sidebar:
    # Dropdown menu for selecting the frequency
    frequency = st.selectbox('Frequency to be measured', [250, 500, 1000, 2000, 4000])

    # Sliders for adjusting the pure tone level and masking noise level
    pure_tone_level = st.slider('Pure tone level (dBHL)', -5, 110, step=5)
    masking_noise_level = st.slider('Masking noise level (dBHL)', -5, 110, step=5)

# Logic to light up the "response available" lamp based on the selected frequency and levels
response_message = ""
if frequency == 250:
    if pure_tone_level >= 50:
        response_message = 'Response!'
    else:
        response_message = 'No response'
elif frequency == 500:
    if pure_tone_level >= 95 and masking_noise_level < 40:
        response_message = 'Response!'
    else:
        response_message = 'No response'
elif frequency == 1000:
    if pure_tone_level >= 90 and masking_noise_level < 30:
        response_message = 'Response!'
    else:
        response_message = 'No response'
elif frequency == 2000:
    if pure_tone_level >= 90:
        response_message = 'Response!'
    else:
        response_message = 'No response'
elif frequency == 4000:
    if pure_tone_level >= 95:
        response_message = 'Response!'
    else:
        response_message = 'No response'

st.sidebar.success(response_message)

# Creating the audiogram diagram
fig, ax = plt.subplots()
frequencies = [250, 500, 1000, 2000, 4000]
levels = [35, 35, 30, 50, 60]
ax.plot(frequencies, levels, 'x--', color='blue', label='Standard Levels')

# Adding the "0" mark based on the pure tone level and selected frequency
if pure_tone_level >= -5:
    ax.plot(frequency, pure_tone_level, 'o', color='red', label='Test Level')

ax.set_xlim(200, 4200)
ax.set_ylim(-20, 110)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Pure tone level (dBHL)')
ax.set_title('Audiogram')
ax.grid(True)
ax.legend()

st.pyplot(fig)

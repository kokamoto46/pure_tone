#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st

# Title for the application
st.title('Standard pure tone audiometry masking practice application')

# Dropdown menu for selecting the frequency
frequency = st.selectbox('Frequency to be measured', [250, 500, 1000, 2000, 4000])

# Sliders for adjusting the pure tone level and masking noise level
pure_tone_level = st.slider('Pure tone level (dBHL)', -5, 110, step=5)
masking_noise_level = st.slider('Masking noise level (dBHL)', -5, 110, step=5)

# Logic to light up the "response available" lamp based on the selected frequency and levels
if frequency == 250:
    if pure_tone_level >= 50:
        st.success('Response available')
    else:
        st.error('Response not available')
elif frequency == 500:
    if pure_tone_level >= 95 and masking_noise_level < 40:
        st.success('Response available')
    else:
        st.error('Response not available')
elif frequency == 1000:
    if pure_tone_level >= 90 and masking_noise_level < 30:
        st.success('Response available')
    else:
        st.error('Response not available')
elif frequency == 2000:
    if pure_tone_level >= 90:
        st.success('Response available')
    else:
        st.error('Response not available')
elif frequency == 4000:
    if pure_tone_level >= 95:
        st.success('Response available')
    else:
        st.error('Response not available')


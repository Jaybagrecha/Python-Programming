# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:35:56 2019

@author: Admin
"""

import speech_recognition as sr
AUDIO_FILE=("Recording(2).wav")

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition couldnt understand audio")
except sr.RequestError:
    print("Couldnt get the results from google SeAUDIO_FILEch Engine")
    
    
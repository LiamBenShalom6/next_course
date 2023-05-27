#!/usr/bin/env python3
import pyttsx3

text_speech = pyttsx3.init()
to_speech = "first time i'm using a package in next.py course, im liam ben shalom"
text_speech.say(to_speech)
text_speech.runAndWait()
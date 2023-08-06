# -*- coding: utf-8 -*-
"""
Created on Wed May 10 19:38:14 2023

@author: sumo
"""

import pyttsx3
from PyPDF2 import PdfReader

pdfreader = PdfReader('book.pdf')
speaker = pyttsx3.init()

text = ''
for page_num in range(len(pdfreader.pages)):
    text += pdfreader.pages[page_num].extract_text()

clean_text = text.strip().replace('\n', '')
print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()

import os
import time
from pyfiglet import Figlet

f = Figlet(font='slant')
word = 'CON LỢN HUY NGUYỄN'
curr_word = ''
for char in word:
   #os.system('clear') #assuming the platform is linux, clears the screen
    curr_word += char
    print(f.renderText(curr_word))
    time.sleep(0.5)
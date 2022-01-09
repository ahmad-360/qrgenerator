import os
import qrcode
from PIL import Image
import termcolor
from termcolor import *


os.system("clear")

print("""
  ___                                      _             
 / _ \ _ __ __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | | '__/ _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |_| | | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
 \__\_\_|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
           |___/                           

                                        by Mal4D

""")


i=input(str("Inser what you want : " ))

image=qrcode.make(i)
print(colored('Generating ...', 'yellow',))

image.save("qr.png")
img = Image.open(r'qr.png')
img.show()

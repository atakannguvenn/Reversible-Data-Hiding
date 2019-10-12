import cv2
import numpy as np
from matplotlib import pyplot as plt
import imageio
from PIL import Image

lena = imageio.imread('my.png')
print(lena.shape)
extract = np.zeros(shape=(512,512))

ptr1=0
msg=''

for i in range(512):
	for j in range(512):
		extract[i][j]=lena[i][j]

print(extract)

for i in range(512):
	for j in range(512):
		if ptr1 >40:
			break
		if extract[i][j]==155:
			msg=msg+'1'
			ptr1=ptr1+1
		if extract[i][j]==154:
			msg=msg+'0'
			ptr1=ptr1+1

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

print(msg)
print (decode_binary_string(msg))
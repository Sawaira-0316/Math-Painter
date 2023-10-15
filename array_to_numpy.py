import numpy as np
from PIL import Image

#creat 3D array of zeros,then replace zeros
data=np.zeros((5,4,3),dtype=np.uint8)
data[:]=[255,255,0]

#make a red patch
data[0:4,0:2]=[255,200,233]
data[3:4,1:4]=[45,3,233]

print(data)

Image=Image.fromarray(data,'RGB')
Image.save("canvas.png")
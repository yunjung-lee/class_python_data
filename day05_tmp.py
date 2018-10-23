#이미지 영역 지정

import scipy as sp
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

def flood_fill(test_array,h_max=255):
    input_array = np.copy(test_array)
    el = sp.ndimage.generate_binary_structure(2,2).astype(np.int)
    inside_mask = sp.ndimage.binary_erosion(~np.isnan(input_array), structure=el)
    output_array = np.copy(input_array)
    output_array[inside_mask]=h_max
    output_old_array = np.copy(input_array)
    output_old_array.fill(0)
    el = sp.ndimage.generate_binary_structure(2,1).astype(np.int)
    while not np.array_equal(output_old_array, output_array):
        output_old_array = np.copy(output_array)
        output_array = np.maximum(input_array,sp.ndimage.grey_erosion(output_array, size=(3,3), footprint=el))
    return output_array

x = plt.imread("test.jpg")
# "convert" to grayscale and invert
binary = 255-x[:,:,0]

filled = flood_fill(binary)

plt.imshow(filled)

# in tkinter



#
# The PIL library itself provides no GUI code --what you are asking for is an application with a GUI. I'd suggest using Tkinter + PIL, but there is no way it is trivial - you will have to handle the mouse clicks, create a rectangle object tracking it, have a way to "reset" the rectangle, and so on.
#
# Unfortunatelly the Canvas Tkinter widget which is used to draw things on is poorly documented - you will have to read trough it here: http://www.pythonware.com/library/tkinter/introduction/canvas.htm
#
# Bellow there is an example code that reads an image file from the disk and draws it on a tkinter window. As you can see, here is some object juggling to get it right.
import Tkinter
import Image, ImageTk, ImageDraw

image_file = "svg.png"

w = Tkinter.Tk()

img = Image.open(image_file)
width, height = img.size
ca = Tkinter.Canvas(w, width=width, height=height)
ca.pack()
photoimg = ImageTk.PhotoImage("RGB", img.size)
photoimg.paste(img)
ca.create_image(width//2,height//2, image=photoimg)
Tkinter.mainloop()

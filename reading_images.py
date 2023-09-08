from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from skimage import io, img_as_float, img_as_ubyte
import cv2
import czifile
import glob

###############################################
# Using Pillow to read in and display images

# Contruct the image in Pillow
img = Image.open("images/test_image.jpg")

# Pillow uses its own image types, not arrays
print(type(img))

# Output the image
img.show()

# Print image format
print(img.format)

# Print image mode (RGB/CMYK/etc.)
print(img.mode)

# Pillow objs can be converted to arrays
img_arr = np.asarray(img)
print(img_arr)


###############################################
# Using matplotlib to read in and display images

img = mpimg.imread("images/test_image.jpg")

# The type of mpl images are np arrays
print(type(img))
print(img)

# Tuple of array dimensions
print(img.shape)

plt.imshow(img)
plt.colorbar()
plt.show()


###############################################
# Using skikit-image to manipulate images

# img_as_float converts a 256 bit RGB val to a float val between 0 and 1
img = img_as_float(io.imread("images/test_image.jpg"))

print(img)

img_byte = img_as_ubyte(img)

print(img_byte)


###############################################
# Using opencv to read in and display images

bw_img = cv2.imread("images/test_image.jpg", 0)
color_img = cv2.imread("images/test_image.jpg", 1)

# opencv types are np arrays
print(type(bw_img)) 
print(type(color_img)) 

# imshow displays image in a new window, first arg is name of the window
cv2.imshow("B&W", bw_img)
cv2.imshow("COLOR", color_img)
# all windows created will display at the same time until destroyed

# HOWEVER, window will immediately disappear unless
# Maintain output window until 
# user presses a key or 1000 ms (1s)
cv2.waitKey(0)          
#destroys all windows created
cv2.destroyAllWindows() 

#OpenCV imread, imwrite and imshow all work with the BGR order, not RGB
#but there is no need to change the order when you read an image with 
#cv2.imread and then want to show it with cv2.imshow
#if you use matplotlib, it uses RGB. 

plt.imshow(color_img)  

#OpenCV represents RGB images as multi-dimensional NumPy arrays, but as BGR.

#we can convert the images from BGR to RGB
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
plt.show()

#We can also change color spaces from RGB to HSV..
plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV))
plt.show()


###############################################
# Using czifile to read in and display images

img = czifile.imread('images/test_image.czi')
print(img.shape)

img = czifile.imread('images/Osteosarcoma_01.czi')
print(img.shape)
img1=img[0, 0, :, :, :, 0]
print(img1.shape)
img2=img1[2,:,:]
io.imshow(img2)

######################################################################################
### Reading multiple images from a folder
#The glob module finds all the path names 
#matching a specified pattern according to the rules used by the Unix shell
#The glob.glob returns the list of files with their full path 

#select the path
path = "images/test_images/molecules/*.*"
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    a= cv2.imread(file)  #now, we can read each file since we have the full path
    print(a)  #print numpy arrays for each file

#let us look at each file
    cv2.imshow('Original Image', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#process each image - change color from BGR to RGB.
    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imshow('Color image', c)
#wait for 1 second
    k = cv2.waitKey(0)
#destroy the window
    cv2.destroyAllWindows()
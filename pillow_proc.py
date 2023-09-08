from PIL import Image
import glob

img = Image.open("images/test_image.jpg")
img.show()
print(img.size) #width and height in pixels

# Resizing
small_img = img.resize((100,200))
small_img.save("images/test_image_small.jpg")
small_img.show()

halfsize_img = img.resize((int(img.width/2), int(img.height/2))) #resize tuple MUST be an int, can't have half a pixel
halfsize_img.save("images/test_image_halfsize.jpg")
halfsize_img.show()
print(halfsize_img.size)

# To also maintain aspect ratio, use thumbnail
img.thumbnail((200,200))
img.save("images/test_image_small_new.jpg")
print(img.size)
# If tuple is larger than original size, doesn't enlarge


# Cropping
img = Image.open("images/test_image.jpg")
cropped_img = img.crop((0, 0, 300, 300))  #crops from (0,0) to (300,300)
cropped_img.save("images/cropped_img.jpg")


# Pasting one image onto another
img1 = Image.open("images/test_image.jpg")
img2 = Image.open("images/test_images/molecules/1.jpg")
img2.thumbnail((100,100))

# Copy img1 into a new image
img1_copy = img1.copy()
img1_copy.paste(img2, (350,350))
img1_copy.save("images/pasted_image.jpg")
img1_copy.show()

# Rotating images
img = Image.open("images/test_image.jpg")

img_90_rot = img.rotate(90)
img_90_rot.save("images/rotated90.jpg")  #keeps original aspect ratio and dimensions

img_45_rot = img.rotate(45)
img_45_rot.save("images/rotated45.jpg")  #keeps original aspect ratio and dimensions

img_45_rot = img.rotate(45, expand=True)  #Dimensions are expanded to fir the entire image
img_45_rot.save("images/rotated45.jpg")  


#Flipping or transposing images
img = Image.open("images/test_image.jpg")

img_flipLR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipLR.save("images/flippedLR.jpg")

img_flipTB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipTB.save("images/flippedTB.jpg")


# Color transforms, convert images between L (greyscale), RGB and CMYK
img = Image.open("images/test_image.jpg")

grey_img = img.convert('L')  #L is for grey scale
grey_img.save("images/grey_img.jpg")


path = "images/test_images/molecules/*.*"
for file in glob.glob(path):
    print(file)     #just stop here to see all file names printed
    a= Image.open(file)  #now, we can read each file since we have the full path
    
    rotated45 = a.rotate(45, expand=True)
    rotated45.save(file+"_rotated45.png", "PNG")   
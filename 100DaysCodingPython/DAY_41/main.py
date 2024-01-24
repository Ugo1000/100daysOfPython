from PIL import Image, ImageFilter

img = Image.open('./DAY_41/shot.png')

# filterImage = img.filter(ImageFilter.BLUR)


filterImage = img.convert('L')

filterImage.save("b.png","png")

# filterImage.show()

# crk = filterImage.rotate(90)
# crk.show()
crop = filterImage.resize((20,20))

crop.show()
 
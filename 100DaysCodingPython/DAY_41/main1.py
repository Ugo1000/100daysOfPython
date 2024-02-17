from PIL import Image

my_img = Image.open('./DAY_41/groot.jpg')
print("This image mode is : ", my_img.mode)
print("This image size is : ", my_img.size)
print("This image description is :", my_img.format_description)
print("This image info is : ", my_img.info)


converted_image = my_img.convert()

converted_image.save('groot_png.png', 'jpeg')
converted_image.show()

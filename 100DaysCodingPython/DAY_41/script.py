from PIL import Image

my_img = Image.open('./DAY_41/groot.jpg')
print("This image mode is : ", my_img.mode)
print("This image size is : ", my_img.size)
print("This image discription is :", my_img.format_description)
print("This image info is : ", my_img.info)


convterted_image = my_img.convert()

convterted_image.save('groot_png.png', 'jpeg')
convterted_image.show()


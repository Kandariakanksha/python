from PIL import Image
img=Image.open("IMG_20180303_220541_214.jpg")
print(img.size)
print(img.format)
area=(80,80,100,100)
cropped_img=img.crop(area)
img.show()
cropped_img.show()
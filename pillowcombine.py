from PIL import Image

imag= Image.open("IMG_20180303_220541_214.jpg")
image= Image.open("IMG_20180303_21507_476.jpg")


area=(100, 100, 300, 300)
imag.paste(image, area)


imag.show()
import random
import urllib.request
def download_web_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpeg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://assets.hongkiat.com/uploads/ww-flower-wallpapers/blueflowers.jpg")

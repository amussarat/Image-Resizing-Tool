from PIL import Image

img = Image.open('./ComputerGeek.jpg')
img.thumbnail((400,400))
img.save('ResizedImg.jpg')
print(f'Compressed Image size: {img.size}')
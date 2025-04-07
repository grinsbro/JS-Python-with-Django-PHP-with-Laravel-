import qrcode

img = qrcode.make("google.com")
print(type(img))
img.save('google.png')

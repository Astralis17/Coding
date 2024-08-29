import qrcode

img = qrcode.make ("https://is.gd/t343CF")
img.save("code.png")
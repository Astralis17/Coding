import qrcode

img = qrcode.make ("https://astralis0.github.io/TryInTY/")
name = "TryInTY"#input("Name for QR code; ")
img.save(name + ".png")
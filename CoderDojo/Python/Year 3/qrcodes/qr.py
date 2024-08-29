import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://bofreinaprgjbryrpgevpobbtnybb.w3spaces.com/")
qr.make(fit=True)

img = qr.make_image(fill_color=(140,255,251), back_color="black")
img.save("website.png")
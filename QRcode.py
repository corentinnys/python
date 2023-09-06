import qrcode

data = "QR code using make function"
img = qrcode.make(data)
img.save('qrcode.png')
img.show()

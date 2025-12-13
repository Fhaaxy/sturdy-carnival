import qrcode

data = input("Insert the url QR Code: ").strip()


qr = qrcode.QRCode()
qr.add_data(data)

path = input("Insert the path to save the QR Code image (including filename.png): ").strip()
img = qr.make_image()
img.save(path)
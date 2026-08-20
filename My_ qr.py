import qrcode

data = input("Kis cheeza ka QR Code banana hai? Link ya naam likho: ")

img = qrcode.make(data)

img.save("/storage/emulated/0/Download/my_qr.png")

print("Ho gaya! my_qr.png naam se QR Code ban gaya hai")
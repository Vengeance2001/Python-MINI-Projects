import qrcode 
import qrcode.constants

#take input
link = input("Enter the link to be converted in qr:")

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("samplefile.png")
print("your qr code has been generated sucessfully!")


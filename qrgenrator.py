#  rub this first to installl qrcode ----  pip install  qrcode
import qrcode as qr

#img = qr.make("https://instagram.com/mr.niraj14?igshid=MTk0NTkyODZkYg==")
#img.save("instaqrcode.png")

from PIL import Image


# add feature in qr code featur like-  color ,shape, bg color
feature = qr.QRCode(version=1,box_size=40, border=10,error_correction = qr.constants.ERROR_CORRECT_H,)

feature.add_data("https://instagram.com/mr.niraj14?igshid=MTk0NTkyODZkYg==")

feature.make(fit=True)

img = feature.make_image(fill_color="red",back_color = "yellow")
img.save("instagramqrcode.png")

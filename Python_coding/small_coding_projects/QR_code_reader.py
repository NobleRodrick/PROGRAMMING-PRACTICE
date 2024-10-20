# install the library
# create the function that collects a text and converts it to qrcode
# save the qrcode  as an image
# create a function that takes the image and converts it to a text
# run the function

import qrcode
import qrcode.constants

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")
    
generate_qr_code("https://github.com/NobleRodrick")
    

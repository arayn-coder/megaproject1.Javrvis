import qrcode

def QR_code():
    # Data to be encoded
    data = input("Please give data for gernate QR code: ")

    # Create QR Code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1 is smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Thickness of the border (minimum is 4)
    )

    # Add data to the QR Code
    qr.add_data(    data)
    qr.make(fit=True)

    # Generate the QR Code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR Code to a file
    img.save("qrcode.png")
    print("qrcode generate successfully!...")

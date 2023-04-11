import qrcode
import time

logo = """
  _____   ______      _______  _____  ______  _______       ______ _______ __   _ _______  ______ _______ _______  _____   ______
 |   __| |_____/      |       |     | |     \ |______      |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/
 |____\| |    \_      |_____  |_____| |_____/ |______      |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_
                                                                                                                                 """


def qr_generate():
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('MyQRCode.png')
    print("\nKod QR wygenerowano do pliku MyQRCode.png")
    time.sleep(2)
    exit()


print(logo)
data = input("\nWprowadź dane do wygenerowania kodu QR: ")
qr_generate()

import qrcode
qr = qrcode.make('follow @_md.cartel')
qr.save('my_qrcode.png')
print('QR Code generated and saved as 'my_qrcode.png'!')
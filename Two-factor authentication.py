import pyotp
import qrcode


secret = pyotp.random_base32()
print(f'Secret: {secret}')

totp = pyotp.TOTP(secret)


uri = totp.provisioning_uri(name='user@example.com', issuer_name='YourAppName')

img = qrcode.make(uri)
img.save('qrcode.png')
print('QR Code generated and saved as qrcode.png')


user_input_otp = input('Enter the OTP from your authentication app: ')

if totp.verify(user_input_otp):
    print('OTP is valid!')
else:
    print('Invalid OTP.')

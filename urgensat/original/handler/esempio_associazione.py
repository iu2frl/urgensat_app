import base64
import iot.pyDH as pyDH
import pyotp

d1 = pyDH.DiffieHellman()
d2 = pyDH.DiffieHellman()
d1_pubkey = d1.gen_public_key()
d2_pubkey = d2.gen_public_key()
d1_sharedkey = d1.gen_shared_key(d2_pubkey)
d2_sharedkey = d2.gen_shared_key(d1_pubkey)

totp = pyotp.TOTP(base64.b32encode(d1_sharedkey.encode("UTF-8")))

totp.now()
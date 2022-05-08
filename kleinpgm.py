 
import adafruit_binascii as binascii
from KLEIN import KLEIN

key=0xFFFFFFFFFFFFFFFF

key="Test"
plaintext="Hello"

print ("Message:\t",plaintext)

k=int(binascii.hexlify(key.encode()),16)
m=int(binascii.hexlify(plaintext.encode()),16)

# Test for klein64
# k=0xFFFFFFFFFFFFFFFF
# m=0x0000000000000000 # Cipher 0x6456764e8602e154

# Test for klein80
# k=0xFFFFFFFFFFFFFFFFFFFF
# m=0x0000000000000000 # Cipher 0x82247502273DCC5F

# Test for klein96
# k=0xFFFFFFFFFFFFFFFFFFFFFFFF
# m=0x0000000000000000 # Cipher 0x15A3A03386A7FEC6

klein64 = KLEIN(nr=12, size=64)
klein80 = KLEIN(nr=16, size=80)
klein96 = KLEIN(nr=20, size=96)

k64=klein64.encrypt(k, m)
k80=klein80.encrypt(k, m)
k96=klein96.encrypt(k, m)

print ("KLEIN64 (NR=12, Size=64):\t",hex(k64))
print ("KLEIN80 (NR=16, Size=80):\t",hex(k80))
print ("KLEIN96 (NR=20, Size=96):\t",hex(k96))

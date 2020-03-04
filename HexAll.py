import struct
import numpy as np
from binascii import unhexlify


inputHex = "3f80"
inputHex = "3c00"
inputHex = "0001"


inputFloat32 = 1.0
inputFloat16 = 1.0
inputBFloat16 = 3.0
inputUInt32 = 100
inputInt32 = -1

print("")
print("HEX To Value")

if len(inputHex)>4:
  print("hex->float32 : " + struct.unpack(">f", bytes.fromhex(inputHex)))
  print("hex->UInt    : " + struct.unpack(">I", bytes.fromhex(inputHex)))
  print("hex->Int     : " + struct.unpack(">i", bytes.fromhex(inputHex)))
else:
  print("hex->Bfloat  : " + str(struct.unpack(">f", bytes.fromhex(inputHex+"0000"))))
  
  aa = struct.unpack(">I", bytes.fromhex("0000"+inputHex))[0]
  aa = struct.pack("<I",aa).hex()[0:4]
  x=unhexlify(bytes(aa, 'utf-8'))
  aa = np.frombuffer(x, np.float16)
  print("hex->float16 : " + str(aa))

  print("hex->UInt    : " + str(struct.unpack(">I", bytes.fromhex("0000"+inputHex))))
  print("hex->Int     : " + str(struct.unpack(">i", bytes.fromhex("0000"+inputHex))))
  



print("")
print("Value To HEX")

aa = struct.pack(">f", inputFloat32).hex()
bb = struct.unpack(">I", bytes.fromhex(aa))
print("float->hex   : " + str(aa) + "   DEC:" + str(bb))

aaa = np.array([inputFloat16],"float16")
bbb = bytes(memoryview(aaa[0])).hex()
aa = struct.unpack(">I", bytes.fromhex("0000"+bbb))[0]
aa = struct.pack("<I",aa).hex()[0:4]
bb = struct.unpack(">I", bytes.fromhex("0000"+aa))
print("float16->hex : " + str(aa) + "   DEC:" + str(bb))

aa = struct.pack(">f", inputBFloat16).hex()
bb = struct.unpack(">I", bytes.fromhex("0000"+aa[0:4]))
print("Bfloat->hex  : " + str(aa)[0:4] + "   DEC:" + str(bb))

aa = struct.pack(">i", inputInt32).hex()
bb = struct.unpack(">I", bytes.fromhex(aa))
print("Int->hex     : " + str(aa) + "   DEC:" + str(bb))

aa = struct.pack(">I", inputUInt32).hex()
print("UInt->hex    : " + str(aa))


# https://docs.python.org/zh-cn/3/library/struct.html

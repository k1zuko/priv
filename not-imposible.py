import struct
import random
def b2l(s):
	c = 0
	unpack = struct.unpack
	length = len(s)
	if length % 4:
		e = (4 - length % 4)
		s = b'\x00' * e + s
		length = length + e
	for i in range(0, length, 4):
		c = (c << 32) + unpack('>I', s[i:i+4])[0]
	return c

flag = b2l(b"LKS{fakefakefakefakefakefakefakefake!}")
assert len(flag) == 38
r = random.getrandbits(256)
print(f"{r = }")
# r = 97787004860334326825769940273828203688991199084221347055088163884691816874265
print(f"{flag % r = }")
# flag % r = 16754372898400552280895412128272336087724225140127018828775003692690045821835
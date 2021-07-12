import struct,sys
import os.path
def align(file, size = 4):
    while(file.tell() % size): file.seek(file.tell() + 1)
def read32(file):
    return struct.unpack("<I", file.read(4))[0]

def getString(f, term=b'\0'):
    result = ""
    tmpChar = f.read(1).decode("ASCII")
    while ord(tmpChar) != 0:
        result += tmpChar
        tmpChar = f.read(1).decode("ASCII")
    return result

f = open("crowd.fs", "rb")
i = open("index.fs", "rb")

while(read32(i) != 0):
    startoff = read32(i)
    filesize = read32(i)
    crc32 = read32(i)# Some kind of hash idk
    name = getString(i)
    align(i)

    f.seek(startoff)
    out = open(name, "wb")

    for _ in range(filesize): out.write(f.read(1))



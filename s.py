#Struct

from struct import pack, unpack

strfile = "F:/Python/struct.txt"
strformat = "iid"

packed = pack(strformat, 1,2,45.5)

print("Packed Data is",packed)

with open(strfile, "bw") as f:
    f.write(bytes(packed))

with open(strfile, "br") as f:
    buffer = f.read()
    unpacked = unpack(strformat, buffer)
    print(unpacked)



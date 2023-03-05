table_of_crc = []
for i in range(256):
    crc = 0
    for j in range(8):
        if (i ^ crc) & 1:
            crc = (crc >> 1) ^ 0xEDB88320
        else:
            crc //= 2 #or crc>>=1
        i //= 2 #or i>>=1
    table_of_crc.append(crc)

def crc32(string):
    value = 0xffffffff

    for char in string:
        value = table_of_crc[(ord(char) ^ value) & 0x000000ff] ^ (value >> 8)
    return hex(value)

print(crc32('Hello world!'))
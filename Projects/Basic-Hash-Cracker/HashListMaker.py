import os
import hashlib

filenameMD5 = "md5"
filenameSHA1 = "sha1"
filenameSHA256 = "sha256"
filenameSHA512 = "sha512"
File = r'D:\projects\Hash_cracker\10k-common-passwords'

with open(File+".txt", 'r') as file, \
    open(File+filenameMD5 +".txt", 'w') as f_md5, \
    open(File+filenameSHA1 +".txt", 'w') as f_sha1, \
    open(File+filenameSHA256 +".txt", 'w') as f_sha256, \
    open(File+filenameSHA512 +".txt", 'w') as f_sha512:

    for line in file:
        stripped_line = line.strip()
        encoded_line = stripped_line.encode('utf-8')

        f_md5.write(f"{stripped_line}:{hashlib.md5(encoded_line).hexdigest()}\n")
        f_sha1.write(f"{stripped_line}:{hashlib.sha1(encoded_line).hexdigest()}\n")
        f_sha256.write(f"{stripped_line}:{hashlib.sha256(encoded_line).hexdigest()}\n")
        f_sha512.write(f"{stripped_line}:{hashlib.sha512(encoded_line).hexdigest()}\n")



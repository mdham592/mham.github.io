import string
import hashlib
import itertools

File = r'D:\projects\Hash_cracker\10k-common-passwords'


def bruteForce(hash):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)
    charset = lowercase + uppercase + digits + symbols
    max_length = 8

    print(f"Starting brute force using {hashAlg} with full charset...")
    hash_func = getattr(hashlib, hashAlg)

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            password = ''.join(combo)
            encoded = password.encode('utf-8')
            hashed = hash_func(encoded).hexdigest()

            if hashed == hash:
                print(f"Password found: {password}")
                return
    print("Password not found.")



while True:
    cracked = False
    breachedHash = input("Please enter hash:")
    hashAlg = ""
    if len(breachedHash) == 32:
        hashAlg="md5"
    elif len(breachedHash) == 40:
        hashAlg="sha1"
    elif len(breachedHash) == 64:
        hashAlg="sha256"
    elif len(breachedHash) == 128:
        hashAlg="sha512"
    else:
        print("Sorry we only support MD5, SHA1, SHA256, and SHA512")
        exit()
    print("\nStarting dictionary attack:\n")
    with open(File+hashAlg +".txt", 'r') as file :
        for line in file:
            stripped_line = line.strip()
            currentHash=stripped_line.split(":", 1)[1]
            if currentHash == breachedHash:
                password = stripped_line.split(":", 1)[0]
                print("The hash was found in the dictionary. Hash is: " + password +"\n\n")
                cracked = True
                break
    if cracked == False:
        continueBF = input("\nThe hash has was not found in our dictionary. Do you wish to continuing to brute force? This will may take a long time. (y or n)\n")
        if continueBF == "y":
            print("Time will tell")
            bruteForce(breachedHash)
        else:
            print("The world may never know")










#check if password is in the top 10,000 password (can be swaped for rockyou v2)




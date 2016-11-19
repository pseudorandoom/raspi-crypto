# import pdb; pdb.set_trace()
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
publickey = key.publickey()

def encrypt(plain):
    return publickey.encrypt(plain, 32)[0]

def decrypt(cyphertext):
    return key.decrypt(cyphertext)

if __name__ == '__main__':
    encrypted = publickey.encrypt('hack the planet!', 32)[0]
    print 'encrypted', encrypted
    decrypted = key.decrypt(encrypted)
    print 'decrypted', decrypted

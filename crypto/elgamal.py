from Crypto.PublicKey import ElGamal
from Crypto import Random

key = ElGamal.generate(1024, Random.new().read)
publickey = key.publickey()
encrypted = publickey.encrypt('hack the planet!')
print 'encrypted', encrypted
decrypted = key.decrypt(encrypted)
print 'decrypted', decrypted

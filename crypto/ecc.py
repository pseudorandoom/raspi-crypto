#!/usr/bin/env python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
 
padder = padding.OAEP(
 mgf=padding.MGF1(algorithm=hashes.SHA1()),
 algorithm=hashes.SHA1(),
 label=None
)

public_key = private_key.public_key().public_numbers().public_key(default_backend())

def encrypt(plain):
    return public_key.encrypt(plain, padder)

def decrypt(cypher):
    return private_key.decrypt(cypher, padder)


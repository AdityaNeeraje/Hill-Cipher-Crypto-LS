# import the necessary libraries here
from Crypto.Cipher import AES
import Crypto
from Crypto.Random import random
import Crypto.Random
from Crypto.Random.random import randrange
from Crypto.Random.random import getrandbits
from Crypto.Util.number import bytes_to_long, long_to_bytes
from random import randbytes
import random

class RSA:
    """Implements the RSA public key encryption / decryption."""

    def __init__(self, key_length):
        # define self.p, self.q, self.e, self.n, self.d here based on key_length
        self.__p=Crypto.Util.number.getPrime(key_length)
        self.__q=Crypto.Util.number.getPrime(key_length)
        self.n=self.__p*self.__q
        self.__tot=(self.__p-1)*(self.__q-1)
        self.e=random.randint(1,self.__tot)
        while Crypto.Util.number.GCD(self.e, self.__tot) != 1:
            self.e+=1
        self.d=pow(self.e, -1, self.__tot)

    def encrypt(self, binary_data):
        int_data = bytes_to_long(binary_data)
        return pow(int_data, self.e, self.n)

    def decrypt(self, encrypted_int_data):
        return long_to_bytes(pow(encrypted_int_data, self.d, self.n)).decode()

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""

    def is_parity_odd(self, encrypted_int_data):
        return pow(encrypted_int_data, self.d, self.n) % 2 == 1


def parity_oracle_attack(ciphertext, rsa_parity_oracle):
    n=rsa_parity_oracle.n
    if (n%2 == 0):
        d=pow(rsa_parity_oracle.e, -1, n/2-1)
        return long_to_bytes(pow(ciphertext, d, n)).decode()
    left=0
    right=n-1
    mid=(left+right)//2
    index=0
    power=pow(2, rsa_parity_oracle.e, n)
    while left < right:
        index+=1
        mid=(left+right)//2
        ciphertext*=power
        ciphertext%=n
        if rsa_parity_oracle.is_parity_odd(ciphertext):
            left=mid+1
        else:
            right=mid
    # return left
    return long_to_bytes(left).decode()

def main():
    input_bytes = input("Enter the message: ")
    # input_bytes="HELLO"
    # input_bytes=randbytes(10)
    encoded_message=input_bytes.encode()
    # Generate a 1024-bit RSA pair    
    rsa_parity_oracle = RSAParityOracle(1024)
    # Encrypt the message
    ciphertext = rsa_parity_oracle.encrypt(encoded_message)
    print("Encrypted message is: ",ciphertext)

    print("Decrypted text is: ",rsa_parity_oracle.decrypt(ciphertext))

    # Check if the attack works
    plaintext = parity_oracle_attack(ciphertext, rsa_parity_oracle)
    # print(plaintext-bytes_to_long(encoded_message))
    print("Obtained plaintext: ",plaintext)
    # assert plaintext == input_bytes.encode()


if __name__ == '__main__':
    main()
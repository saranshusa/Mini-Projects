# This program shows a basic algorithm of cryptocurrency mining process.
# In this program, Bitcoin (BTC) is mined with following inputs:
# Block : 682981
# Hash : 0000000000000000000a659c5c2fd4d0dca61483c22818e1fc117f89649b8812
# Miner : AntPool
# Prefix Zeros : 19
# Block Reward : 6.25 BTC

from hashlib import sha256
import time
from time import sleep

MAX_NONCE = 1000000000 # The larger the value of MAX_NONCE, the larger the resources requires for mining like power.

def SHA256 (text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(blockNumber, transactions, previousHash, prefixZeros):
    prefixStr = '0' * prefixZeros
    for nonce in range(MAX_NONCE):
        text = str(blockNumber) + transactions + previousHash + str(nonce)
        newHash = SHA256(text)
        if newHash.startswith(prefixStr):
            print(f'Yay! Mined Successfully. NONCE is : {nonce}')
            return newHash

    raise BaseException('Unable to find required nonce. Increase MAX_NONCE.')

def main():
    transactions = 'Saransh -> Sam _20BTC'
    difficulty = 19 # Set this value to a lower integer to get the result faster. eg: 8
    start = time.time()
    print('\nMINING STARTED....\n')

    newHash = mine(982976, transactions, '0000000000000000000b9ee355271d05189f1288fb851f6323f33ced4e807b58', difficulty)
    
    totalTime = str((time.time() - start))
    print(f'\nMINING ENDED.... \t Total time consumed : {totalTime} Seconds\n')
    print(newHash)
    sleep(5)

if __name__ == '__main__':
    main()
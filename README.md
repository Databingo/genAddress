# genAddress
Bitcoin and Litecoin like Wallet Address Generator

This is a Bitcon like wallet address generator coded in Python 3.
input a seed = str(time.time()) + ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
and outputs private key and an uncompressed public address in base58 format, the most used.

# Usage:
python test.py

# Output:
BTC Private Key: L51GMF6Hxt784FkCSQ4WcvEse8w1pFmx9hy1ZEmG4H4CkUhxXQ5y
Public Key: 12d9bjgh97v9st1GHjxbxUVGE4oww4ZpzC
LTC Private Key: TAqXnzPUNG5iq6P4z31NqGnFazaKtLnqxusGR3PodFENGNBiZWUD
Public Key: LLr6rwzXDnAD8ghRTswuEVZ2SHBE3BfV2k

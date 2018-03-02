import time,string,random
import hashlib
import bitkeylib

seed = str(time.time()) + ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
enx = seed.encode() 
pk = bytes(hashlib.sha256(enx).digest())

bitkeylib.NetworkConstants.set_mainnet('BTC')

privkey_wif = bitkeylib.serialize_privkey(pk, True, "p2pkh")

txin_type, bprivkey, compressed = bitkeylib.deserialize_privkey(privkey_wif)
pubkey = bitkeylib.public_key_from_private_key(bprivkey, compressed)
addr = bitkeylib.pubkey_to_address(txin_type, pubkey)

print('BTC Private Key: {0}\nPublic Key: {1}'.format(privkey_wif, addr))

bitkeylib.NetworkConstants.set_mainnet('LTC')

privkey_wif = bitkeylib.serialize_privkey(pk, True, "p2pkh")

txin_type, bprivkey, compressed = bitkeylib.deserialize_privkey(privkey_wif)
pubkey = bitkeylib.public_key_from_private_key(bprivkey, compressed)
addr = bitkeylib.pubkey_to_address(txin_type, pubkey)

print('LTC Private Key: {0}\nPublic Key: {1}'.format(privkey_wif, addr))

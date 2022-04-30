from web3 import Web3
from mnemonic import Mnemonic
import time

class Blockchain():
    
    def wallet(self) -> None:
        phrase = Mnemonic("english")
        words = phrase.generate(strength=128)
        # print(f"Save this Mnemonnic phrase: {words}")
        seed = phrase.to_seed(words, passphrase="")
        entropy = phrase.to_entropy(words)
        infura_url ="https://kovan.infura.io/v3/1b6c0ac430c04d9ea18aabe4d787763d"
        web3 = Web3(Web3.HTTPProvider(infura_url))
        private  = Web3.toHex(entropy)
        account_name = web3.eth.account.create()
        block = web3.eth.get_block('latest')
        print(account_name.address)
        print(account_name.privateKey)
        pass

class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()






block = Blockchain()





































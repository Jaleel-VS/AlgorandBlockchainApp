import json
import hashlib


def get_encoded_bytes(json_object, encoding='utf-8'):
    try:
        return json.dumps(json_object).encode(encoding)
    except Exception as e:
        print("Exception when converting to json and encoding: %s\n" % e)
        return None
    
def get_transaction_address(txid):
    return "https://testnet.algoexplorer.io/tx/{}".format(txid)

def get_hash(bytes):
    return hashlib.sha256(bytes).hexdigest()
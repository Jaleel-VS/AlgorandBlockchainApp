import json
import hashlib


def get_encoded_bytes(json_object, encoding='utf-8'):
    try:
        return json.dumps(json_object).encode(encoding)
    except Exception as e:
        print("Exception when converting to json and encoding: %s\n" % e)
        return None
    
def get_transaction_address(txid):
    output = ""
    output += "Transaction ID: {}\n".format(txid)
    output += "View transaction at:\n"
    output += "https://app.dappflow.org/explorer/transaction/{}\n".format(txid)
    output += "https://testnet.algoexplorer.io/tx/{}".format(txid)
    return output

def get_hash(bytes):
    return hashlib.sha256(bytes).hexdigest()
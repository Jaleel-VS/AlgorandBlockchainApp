import json


def get_encoded_bytes(json_object, encoding='utf-8'):
    try:
        return json.dumps(json_object).encode(encoding)
    except Exception as e:
        print("Exception when converting to json and encoding: %s\n" % e)
        return None
    
def print_transaction_address(txid):
    print("Transaction ID: {}".format(txid))
    print("View transaction at: ")
    print("https://app.dappflow.org/explorer/transaction/{}".format(txid))
    print("https://testnet.algoexplorer.io/tx/{}".format(txid))
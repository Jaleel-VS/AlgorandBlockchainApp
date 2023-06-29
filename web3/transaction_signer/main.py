from algosdk.v2client.algod import AlgodClient
from algosdk import transaction, account, mnemonic
from utils import get_encoded_bytes, print_transaction_address
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY=os.getenv("ALGO_SECRET")
ADDR = account.address_from_private_key(SECRET_KEY)

class Transaction:
    def __init__(self, note):
        self.__setup()
        self.sp = self.client.suggested_params()
        self.note = get_encoded_bytes(note)
        self.tx_id = self.__create_transaction()
        self.__print_transaction_address(self.tx_id)

    def __setup(self):
        self.client = AlgodClient(
            os.getenv("ALGOD_TOKEN"),
            os.getenv("ALGOD_SERVER"),
        )

    def __create_transaction(self):
        txn = transaction.PaymentTxn(
            sender=ADDR,
            sp=self.sp,
            amt=0,
            receiver=ADDR,
            note=self.note).sign(SECRET_KEY)
        
        txid = self.client.send_transaction(txn)

        try:
            transaction.wait_for_confirmation(
                self.client,
                txid,
                4
            )

            


        except Exception as e:
            raise e

        return txid
    
    def __print_transaction_address(self, txid):
        print_transaction_address(txid)

    

if __name__ == "__main__":
    txn = Transaction("Hello World!")
from services.transaction import Transaction
from services.utils import get_hash
import boto3
import json
# Send relevant document to the Blockchain

s3_resource = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"

def send_hash_to_blockchain(document_bytes: bytes) -> dict:
        t_hash = get_hash(document_bytes)
        t = Transaction(t_hash)
        t_add = t.get_transaction_address(t.tx_id)
        return {"success": True,
                "transaction_hash": t_hash,
                "transaction_id": t.tx_id, # This is the transaction id that we will be using to get the transaction details    
                "transaction_address": t_add}

# Helping methods
async def s3_upload(contents: bytes, key: str, folder:str):
    s3_resource.Bucket('fairchancedocketbucket').put_object(Key=f'{folder}/{key}', Body=contents, Metadata={'Case Number': '123', 'Reviewed': 'True'})
    
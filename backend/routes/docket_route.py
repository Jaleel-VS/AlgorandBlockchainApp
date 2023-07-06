# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.docket import Docket
from services.transaction import Transaction
from services.utils import get_hash
import json


docket_router = APIRouter()
s3_client = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"

# Helping methods
async def s3_upload(contents: bytes, key: str):

    s3_client.Bucket('fairchancedocketbucket').put_object(Key=key, Body=contents)

# s3.client is a low-level client representing Amazon Simple Storage Service (s3). Documentation shows the many methods that you can use with this client
# GET REQUEST METHOD (Getting the list of all buckets)







# Post test docket 
@docket_router.post("/docket_test")
async def create_docket(docket: Docket):
    try:
        print(docket)
        docket_bytes = json.dumps(docket.dict()).encode()

        # we should abstract this to a seperate method/class
        t_hash = get_hash(docket_bytes)
        t = Transaction(t_hash)
        t_add = t.get_transaction_address(t.tx_id)
        await s3_upload(contents=docket_bytes, key=f"Docket_{t.tx_id}.txt")
        return {"success": True,
                "transaction_hash": t_hash,
                "transaction_id": t.tx_id, # This is the transaction id that we will be using to get the transaction details    
                "transaction_address": t_add}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    
    



    # We will be using the upload file method of the boto3 module
    # The access key id and the password are very importaht when we are trying to configure the IAM user on our machine

  
# GET REQUEST METHOD (Listing the dockets)

# Get REQUEST METHOD (Get a specific docket)

# PUT REQUEST METHOD (Update, though it won't be a true update because s3 will just use versioning)

# There will be no delete
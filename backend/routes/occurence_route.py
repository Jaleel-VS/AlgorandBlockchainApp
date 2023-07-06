# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.occurrence import Occurrence
from services.transaction import Transaction
from services.utils import get_hash
import json

occurrence_router = APIRouter()
s3_client = boto3.resource('s3')

# Helping methods
async def s3_upload(contents: bytes, key: str):

    s3_client.Bucket('fairchancedocketbucket').put_object(Key=key, Body=contents)

# Post an occurance
@occurrence_router.post("/log_occurance") 
async def create_occurrence(occurrence: Occurrence):
    try:
        print(occurrence)
        occurrence_bytes = json.dumps(occurrence.dict()).encode()

        # we should abstract this to a seperate method/class
        t_hash = get_hash(occurrence_bytes)
        t = Transaction(t_hash)
        t_add = t.get_transaction_address(t.tx_id)
        await s3_upload(contents=occurrence_bytes, key=f"Occurrence_{t.tx_id}.txt")
        return {"success": True,
                "transaction_hash": t_hash,
                "transaction_id": t.tx_id, # This is the transaction id that we will be using to get the transaction details    
                "transaction_address": t_add}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
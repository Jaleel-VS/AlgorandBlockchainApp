# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.occurrence import Occurrence
from utils.helper import send_hash_to_blockchain
from utils.helper import s3_upload
from services.transaction import Transaction
from services.utils import get_hash
import json

occurrence_router = APIRouter()
s3_client = boto3.resource('s3')




# Post an occurance
@occurrence_router.post("/log_occurrence") 
async def create_occurrence(occurrence: Occurrence):
    try:
        print(occurrence)
        occurrence_bytes = json.dumps(occurrence.dict()).encode()
        # Sending to Blockchain
        response_dict = dict(send_hash_to_blockchain(occurrence_bytes))
        # Uploading to s3 bucket
        await s3_upload(contents=occurrence_bytes, key=f"Occurrence_{response_dict['transaction_id']}.txt", folder ="OCCURRENCES/")
        return response_dict
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    

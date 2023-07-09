# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.occurrence import Occurrence
from config.database import get_occ_count, update_occ_count
from utils.helper import send_hash_to_blockchain, s3_resource, s3_upload
from services.transaction import Transaction
from services.utils import get_hash
import json
import pymongo

occurrence_router = APIRouter()





# Post an occurance
@occurrence_router.post("/log_occurrence") 
async def create_occurrence(occurrence: Occurrence):
    try:
        occurrence_bytes = json.dumps(occurrence.dict()).encode()
        # Sending to Blockchain
        response_dict = dict(send_hash_to_blockchain(occurrence_bytes))
        # Uploading to s3 bucket
        occurrence_number = get_occ_count()
        await s3_upload(contents=occurrence_bytes, key=f"Occurrence_{occurrence_number}.txt", folder ="OCCURRENCES")
        update_occ_count()
        return response_dict
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    
@occurrence_router.get("/occurrence_number")
async def get_occurrence_number():
    return get_occ_count()
    

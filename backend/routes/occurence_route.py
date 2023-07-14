# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.occurrence import Occurrence
from config.database import get_occ_count, update_occ_count, insert_occurrence
from utils.helper import send_hash_to_blockchain, s3_resource, s3_upload
from services.transaction import Transaction
from services.utils import get_hash
import json
from services.email.mailer import Email
from typing import Any

occurrence_router = APIRouter()





# Post an occurance
@occurrence_router.post("/log_occurrence") 
async def create_occurrence(occurrence: Occurrence):
    try:
        occurrence_dict = occurrence.dict()

        occurrence_bytes = json.dumps(occurrence.dict()).encode()
        
        # Sending to Blockchain
        response_dict = dict(send_hash_to_blockchain(occurrence_bytes))
        
        # Uploading to s3 bucket
        await s3_upload(contents=occurrence_bytes, key=f"Occurrence_{occurrence_dict['occID']}.txt", folder ="OCCURRENCES")
        
        occurrence_dict.update(response_dict)
        
        insert_occurrence(occurrence.dict())
        update_occ_count()
        return {
            "success": True,
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    
@occurrence_router.get("/occurrence_number")
async def get_occurrence_number():
    return  f"OCC{get_occ_count():04d}"
    

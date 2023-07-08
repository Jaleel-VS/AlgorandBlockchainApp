# Program for sending Evidence to s3 bucket
import boto3
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.evidence import Evidence
from services.transaction import Transaction
from utils.helper import send_hash_to_blockchain
#from utils.helper import s3_upload
from services.utils import get_hash
import json

evidence_router = APIRouter()
s3_resource = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"

async def s3_upload(contents: bytes, key: str, folder:str, meta_data: dict):
    #s3_resource.Bucket('fairchancedocketbucket').put_object(Key=f'{folder}/{key}', Body=contents, Metadata={'Case Number': meta_data.get("case_Id"), 'Evidence Description': meta_data["evidence_description"] , "Evidence Origin": meta_data["evidence_origin"], "Associated Officer": meta_data["associated_officer"] })
    s3_resource.Bucket('fairchancedocketbucket').put_object(Key=f'{folder}/{key}', Body=contents, Metadata={"Relevant data": json.dumps(meta_data)})

# Post evidence to s3 
@evidence_router.post("/Evidence")
async def upload_evidence(evidence: Evidence):
    try:
        
        evidence_dict = dict(evidence)
        print(evidence_dict)
        #evidence_content_bytes = json.dumps(evidence_dict["evidence_content"]).encode()
        evidence_content_bytes = evidence_dict["evidence_content"] # Must figure out type here
        evidence_content = evidence_dict.pop("evidence_content")
        evidence_data_bytes = json.dumps(evidence_dict).encode()
        print(evidence_dict)
        # Sending to Blockchain
        response_dict = dict(send_hash_to_blockchain(evidence_data_bytes))
        # # Uploading to s3 bucket
        await s3_upload(contents= evidence_content_bytes, key=f"Evidence_{response_dict['transaction_id']}.txt", folder = "EVIDENCE", meta_data = evidence_dict)
        # return response_dict
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    
@evidence_router.get("/Evidence") # Get all dockets
async def list_all_evidence():
    bucket = s3_resource.Bucket('fairchancedocketbucket')
    all_dockets_list = []
    #for obj in bucket.objects.all():
    for obj in bucket.objects.filter(Prefix = 'EVIDENCE/'):
        metadata = obj.Object().metadata
        key= obj.key
        docket_dict = {"key": key, "Metadata": metadata}
        all_dockets_list.append(docket_dict)
    return all_dockets_list
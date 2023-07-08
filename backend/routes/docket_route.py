# Program for sending dockets to s3 bucket
import boto3
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.docket import Docket
from services.transaction import Transaction
from services.utils import get_hash
from utils.helper import send_hash_to_blockchain
from utils.helper import s3_upload
import json
import os


docket_router = APIRouter()
s3_resource = boto3.resource('s3') 

@docket_router.get("/docket_download") # This downloads the docket
async def download_docket(caseID: str): 
    file = f'.\downloads\Docket_{caseID}.txt'
    s3_resource.Bucket('fairchancedocketbucket').download_file(f'DOCKETS/Docket_{caseID}.txt', file)
    f = open(file, "r")
    print(f.read())
    f.close()
    #if os.path.isfile(".\downloads\docket1.txt"):
        #os.remove(".\downloads\docket1.txt")

@docket_router.get("/docket_get") # Getting the details of a single docket
async def get_docket(caseID:str):
    obj = s3_resource.Object('fairchancedocketbucket', f"DOCKETS/Docket_{caseID}.txt")
    body = eval(obj.get()['Body'].read().decode('utf-8')) 
    return body
    

@docket_router.get("/docket") # Get all dockets
async def list_all_dockets():
    bucket = s3_resource.Bucket('fairchancedocketbucket')
    all_dockets_list = []
    #for obj in bucket.objects.all():
    for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
        metadata = obj.Object().metadata
        key= obj.key
        docket_dict = {"key": key, "Metadata": metadata}
        all_dockets_list.append(docket_dict)
    return all_dockets_list


@docket_router.get("/docket_reviewed") # Get all reviewed dockets
async def list_all_reviewed_dockets():
    bucket = s3_resource.Bucket('fairchancedocketbucket')
    all_dockets_list = []
    #for obj in bucket.objects.all(): This lists everything that is in the bucket
    for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
        metadata_dict = dict(obj.Object().metadata)
        if(bool(metadata_dict.get("reviewed"))):
            key= obj.key
            docket_dict = {"key": key, "Metadata": metadata_dict }
            all_dockets_list.append(docket_dict)
        else:
            continue
    return all_dockets_list
        
@docket_router.get("/docket_unreviewed") # Get all unreviewed dockets
async def list_all_unreviewed_dockets():
    bucket = s3_resource.Bucket('fairchancedocketbucket')
    all_dockets_list = []
    #for obj in bucket.objects.all():
    for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
        metadata_dict = dict(obj.Object().metadata)
        if(not bool(metadata_dict.get("reviewed"))):
            key= obj.key
            docket_dict = {"key": key, "Metadata": metadata_dict }
            all_dockets_list.append(docket_dict)
        else:
            continue
    return all_dockets_list
        

# Post test docket 
@docket_router.post("/docket_test") # I want to organise the object properly and be able to add metadata
async def create_docket(docket: Docket):
    try:
        print(docket)
        docket_bytes = json.dumps(docket.dict()).encode()
        # Sending to Blockchain
        response_dict = dict(send_hash_to_blockchain(docket_bytes))
        # Uploading to s3 bucket
        await s3_upload(contents=docket_bytes, key=f"Docket_{response_dict['transaction_id']}.txt", folder= "DOCKETS")
        return response_dict
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    
    


# @docket_router.put("/docket") # Salvage this to 
# async def insert_metadata(case_number: str, reviewed: bool):
#     reviewed_or_not = str(reviewed)
#     s3_resource.Object('fairchancedocketbucket', 'Docket_from_frontend2.txt').put(Metadata={'Case Number': case_number, 'Reviewed': reviewed_or_not})

# @docket_router.get("/dockets_list") # Get unreviewed dockets
# async def list_dockets():
#     bucket = s3_resource.Bucket('fairchancedocketbucket')
#     for obj in bucket.objects.all():
#         #if(obj.Object().metadata['reviewed'] == 'True'):# This return a dict
#         metadata_dict = dict(obj.Object().metadata)
#         body = obj.get()['Body'].read()
#         if(bool(metadata_dict.get("reviewed"))):
#             print(metadata_dict)
#             print("Docket: ", obj.key, " Metadata: ", metadata_dict.get("reviewed") , " Object Data: ", body , "\n*******************************************************************")
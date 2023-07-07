# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.docket import Docket
from services.transaction import Transaction
from services.utils import get_hash
import json
import os


docket_router = APIRouter()
s3_resource = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"
#s3_client = boto3.client('s3')

# Helping methods
async def s3_upload(contents: bytes, key: str):

    s3_resource.Bucket('fairchancedocketbucket').put_object(Key=key, Body=contents, Metadata={'Case Number': '123', 'Reviewed': 'True'})
    #s3_resource.Object('fairchancedocketbucket', key).put(Body= contents, Metadata={'Case Number': 123, 'Reviewed': True})

# s3.client is a low-level client representing Amazon Simple Storage Service (s3). Documentation shows the many methods that you can use with this client
# GET REQUEST METHOD (Getting the list of all buckets)



# @docket_router.put("/docket") # Salvage this to 
# async def insert_metadata(case_number: str, reviewed: bool):
#     reviewed_or_not = str(reviewed)
#     s3_resource.Object('fairchancedocketbucket', 'Docket_from_frontend2.txt').put(Metadata={'Case Number': case_number, 'Reviewed': reviewed_or_not})

@docket_router.get("/docket") # This downloads the docket
async def get_docket(name: str): 
    s3_resource.Bucket('fairchancedocketbucket').download_file(name, '.\downloads\docket1.txt')
    f = open(".\downloads\docket1.txt", "r")
    print(f.read())
    f.close()
    if os.path.isfile(".\downloads\docket1.txt"):
        os.remove(".\downloads\docket1.txt")

@docket_router.get("/dockets_list")
async def list_dockets():
    #print(s3_client.list_objects(Bucket='fairchancedocketbucket', Delimiter= '*'))
    bucket = s3_resource.Bucket('fairchancedocketbucket')
    for obj in bucket.objects.all():
        #if(obj.Object().metadata['reviewed'] == 'True'):# This return a dict
        metadata_dict = dict(obj.Object().metadata)
        if(bool(metadata_dict.get("reviewed"))):
            print(metadata_dict)
            print("Docket: ", obj.key, " Metadata: ", metadata_dict.get("reviewed") , " Object Data: ", obj.Object().get() , "\n*******************************************************************")

# Post test docket 
@docket_router.post("/docket_test") # I want to organise the object properly and be able to add metadata
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
    
    



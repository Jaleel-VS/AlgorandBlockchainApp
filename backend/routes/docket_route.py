# Program for sending dockets to s3 bucket
import boto3
#import zipfile # Wanna make our dockets into a zip file
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.docket import Docket
from services.transaction import Transaction
import json


docket_router = APIRouter()
s3_client = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"

# Helping methods
async def s3_upload(contents: bytes, key: str):

    s3_client.Bucket('fairchancedocketbucket').put_object(Key=key, Body=contents)

# s3.client is a low-level client representing Amazon Simple Storage Service (s3). Documentation shows the many methods that you can use with this client
# GET REQUEST METHOD (Getting the list of all buckets)



# GET REQUEST METHOD (Listing the dockets)

# Get REQUEST METHOD (Get a specific docket)

# POST REQUEST METHOD(uploading a new docket)
@docket_router.post("/docket") # Defining the route. 
async def upload_new_docket(victim_details: UploadFile| None= None, victim_statement:UploadFile| None =None): # Now for the Python method that is executed 
    print("file uploaded") # Receiving the file as is did not cause any issues 
    if not victim_details:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='No file found!!'
        )
    victim_details_contents = await victim_details.read()
    victim_statement_contents = await victim_statement.read()
    contents = victim_details_contents + victim_statement_contents
    await s3_upload(contents=contents, key = "demo_file1")
    return

# Post test docket 
@docket_router.post("/docket_test")
async def create_docket(docket: Docket):
    print(docket)
    docket_bytes = json.dumps(docket.dict()).encode()
    # await s3_upload(contents=docket_bytes, key="Docket_from_frontend.txt")
    return {"message": "Dumela Lefatse", "success": True}



    # We will be using the upload file method of the boto3 module
    # The access key id and the password are very importaht when we are trying to configure the IAM user on our machine

  


# PUT REQUEST METHOD (Update, though it won't be a true update because s3 will just use versioning)

# There will be no delete
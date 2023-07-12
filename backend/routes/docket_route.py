# Program for sending dockets to s3 bucket
import boto3
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.docket import Docket
from models.user import User
from models.user_login import UserLogin
from config.database import (
    get_docket_count, update_docket_count,
      insert_docket, docket_approved, docket_declined, get_all_dockets,
        docket_pending, get_declined_dockets, get_approved_dockets, get_pending_dockets, 
        get_tasks, get_docket)
from services.transaction import Transaction
from services.utils import get_hash
from utils.helper import send_hash_to_blockchain, s3_upload, s3_resource
from datetime import datetime
import json
import os


docket_router = APIRouter()


# @docket_router.get("/docket_download") # This downloads the docket
# async def download_docket(caseID: str): 
#     file = f'.\downloads\Docket_{caseID}.txt'
    
#     s3_resource.Bucket('fairchancedocketbucket').download_file(f'DOCKETS/Docket_{caseID}.txt', file)
#     f = open(file, "r")
#     print(f.read())
#     f.close()
    #if os.path.isfile(".\downloads\docket1.txt"):
        #os.remove(".\downloads\docket1.txt")

# @docket_router.get("/docket_get") # Getting the details of a single docket
# async def get_docket(caseID:str):
#     obj = s3_resource.Object('fairchancedocketbucket', f"DOCKETS/Docket_{caseID}.txt")
#     body = eval(obj.get()['Body'].read().decode('utf-8')) 
#     return body
    

# @docket_router.get("/list_all_dockets") # Get all dockets
# async def list_all_dockets():
    
#     # Uses s3
#     # for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
#     #     metadata = obj.Object().metadata
#     #     key= obj.key
#     #     docket_dict = {"key": key, "Metadata": metadata}
#     #     all_dockets_list.append(docket_dict)
#     # return all_dockets_list

#     # Uses Mongodb
#     return get_all_dockets()

# @docket_router.get("/list_pending_dockets") # Get pending dockets
# async def list_pending_dockets():
#     # Uses Mongodb
#     return get_pending_dockets()

# @docket_router.get("/list_declined_dockets") # Get declined dockets
# async def list_declined_dockets():
#     # Uses Mongodb
#     return get_declined_dockets()

# @docket_router.get("/list_approved_dockets") # Get approved dockets
# async def list_approved_dockets():
#     # Uses Mongodb
#     return get_approved_dockets()

# # For an officer's tasks
# @docket_router.get("/list_officer_tasks")
# async def list_officer_tasks(user: UserLogin): 
#    return get_tasks(user)

# @docket_router.post("/approve_docket")
# async def approve_docket(docket_name: str, date_time:datetime): 
#     docket_approved()
#     # Then sent to Blockchain
#     # gotta access the docket first from s3
#     try:
#         docket = get_docket(docket_name)
#         docket_bytes = json.dumps(docket.dict()).encode()
#         # Sending to Blockchain
#         response_dict = dict(send_hash_to_blockchain(docket_bytes))
#         return response_dict
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=e
#         )



# @docket_router.post("/docket_declined")
# async def reject_docket(docket_name, comment: str):
#     docket_declined()


# # Submit docket changes
# @docket_router.post("/docket_submit_changes")
# async def submit_initial_docket(docket: Docket):
#     # Uploading to s3 bucket
#     docket_bytes = json.dumps(docket.dict()).encode()
#     docket_dict = docket.dict()

    
#     # await s3_upload(contents= docket_bytes, key= docket_key, folder= "DOCKETS")
#     docket_pending(docket_key)
#     update_docket_count()


# View docket (by whomever)
# @docket_router.post("/view_docket")
# async def view_docket(docket_name: str):
#     docket = get_docket(docket_name) # This gonna bring me a dict
#     return docket

# @docket_router.post("/make_initial_docket")
# async def make_initial_docket(docket: Docket):
#     # Uploading to s3 bucket
#     now = datetime.now()
#     docket_number = get_docket_count()
#     docket_key = f"Docket_{docket_number}_{now}.txt"
#     docket_dict = dict(docket)
#     docket_dict["_id"] = docket_key
#     #docket["relevant_officer"] = user["username"]
#     docket_bytes = json.dumps(docket_dict).encode()
#     try:
#         insert_docket(docket_key, now, docket_dict["relevant_officer"])
#     except:
#         return {"message": "Something went wrong!"}
#     update_docket_count()
#     await s3_upload(contents=docket_bytes, key= docket_key, folder= "DOCKETS")
#     # blockchain add (walahi im finished haha)

@docket_router.post("/submit_initial_docket")
async def submit_initial_docket(docket: Docket):
    try:
        docket_number = get_docket_count()
        docket_key = f"DOC{docket_number:04d}"

        docket = docket.dict()
        docket["docket_key"] = docket_key

        insert_docket(docket)
        update_docket_count()

        return {
            "success": True,
            "docket_key": docket_key
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )
    


@docket_router.get("docket")
async def get_docket_from_db(docket_id: str):
    docket = get_docket(docket_id)

    if docket:
        docket = docket.dict()
        docket.update(
            {"success": True}
        )

        return docket

    else:
        return {
            "message": "Not found"
        }


# Uses s3
# @docket_router.get("/docket_reviewed") # Get all reviewed dockets
# async def list_all_reviewed_dockets():
#     bucket = s3_resource.Bucket('fairchancedocketbucket')
#     all_dockets_list = []
#     #for obj in bucket.objects.all(): This lists everything that is in the bucket
#     for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
#         metadata_dict = dict(obj.Object().metadata)
#         if(bool(metadata_dict.get("reviewed"))):
#             key= obj.key
#             docket_dict = {"key": key, "Metadata": metadata_dict }
#             all_dockets_list.append(docket_dict)
#         else:
#             continue
#     return all_dockets_list
        
# @docket_router.get("/docket_unreviewed") # Get all unreviewed dockets
# async def list_all_unreviewed_dockets():
#     bucket = s3_resource.Bucket('fairchancedocketbucket')
#     all_dockets_list = []
#     #for obj in bucket.objects.all():
#     for obj in bucket.objects.filter(Prefix = 'DOCKETS/'):
#         metadata_dict = dict(obj.Object().metadata)
#         if(not bool(metadata_dict.get("reviewed"))):
#             key= obj.key
#             docket_dict = {"key": key, "Metadata": metadata_dict }
#             all_dockets_list.append(docket_dict)
#         else:
#             continue
#     return all_dockets_list
        

# # Post test docket 
# @docket_router.post("/docket_test") # I want to organise the object properly and be able to add metadata
# async def create_docket(docket: Docket, user: UserLogin):
#     try:
#         print(docket)
#         docket_bytes = json.dumps(docket.dict()).encode()
#         # Sending to Blockchain
#         response_dict = dict(send_hash_to_blockchain(docket_bytes))
#         # Uploading to s3 bucket
#         now = datetime.now()
#         docket_number = get_docket_count()
#         docket_key = f"Docket_{docket_number}_{now}.txt"
#         await s3_upload(contents=docket_bytes, key= docket_key, folder= "DOCKETS")
#         insert_docket(docket_key, now, user)
#         update_docket_count()
#         return response_dict
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=e
#         )

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
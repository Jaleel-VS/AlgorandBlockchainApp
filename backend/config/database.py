
# import the pymongo package
import pymongo
from models.status import status
from models.user_login import UserLogin
from datetime import datetime
# Constants
# the connection string to connect to the mongoDB database
USER_NAME = "jaleel_admin"
PASSWORD = "5r0iuv7JDXh2LGaG"
#DATABASE_NAME = "FairChanceDatabase"


CONNECTION_STRING = f"mongodb+srv://{USER_NAME}:{PASSWORD}@serverlessinstance0.ksq2r.mongodb.net/?retryWrites=true&w=majority"
# connect to the database
try:
    client = pymongo.MongoClient(CONNECTION_STRING)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
    exit()

db = client.FairChanceDatabase
user_collection = db["User_Collection"]
counters_collection = db["Counters"]
docket_collection=db["Dockets"]

#counters_collection.insert_one({"_id": 'Occurrence', "count": 0})
#counters_collection.insert_one({"_id": 'Docket', "count": 0})
#counters_collection.insert_one({"_id": 'Evidence', "count": 0})

def insert_docket(docket_name:str, date_time:datetime, user:str):
    docket_collection.insert_one({"_id": docket_name, "status": status.PENDING.name, "date_created":date_time, "relevant_officer": user})

def docket_approved(docket_name:str, date_time:datetime ):
    filter = {'_id': docket_name}
    newvalue = { "$set": {'status': status.APPROVED.name, 'date_approved': date_time}}
    counters_collection.update_one(filter, newvalue)

def docket_declined(docket_name:str, comment:str):
    filter = {'_id': docket_name}
    newvalue = { "$set": { 'status': status.DECLINED.name, 'rejection_reason':comment }}
    counters_collection.update_one(filter, newvalue)

def docket_pending(docket_name:str):
    filter = {'_id': docket_name}
    newvalue = { "$set": { 'status': status.PENDING.name}}
    counters_collection.update_one(filter, newvalue)

def get_all_dockets() -> list:
    docket_list = []
    for docket in docket_collection.find():
        docket_list.append(docket)
    return docket_list

def get_declined_dockets() -> list:
    declined_docket_list = []
    for docket in docket_collection.find():
       if(docket["status"] == status.DECLINED):
            declined_docket_list.append(docket)
    return declined_docket_list

def get_approved_dockets() -> list:
    approved_dockets_list = []
    for docket in docket_collection.find():
       if(docket["status"] == status.APPROVED):
            approved_dockets_list.append(docket)
    return approved_dockets_list

def get_pending_dockets() -> list:
    pending_dockets_list = []
    for docket in docket_collection.find():
       if(docket["status"] == status.PENDING):
            pending_dockets_list.append(docket)
    return pending_dockets_list

# Get the tasks for a spcecific officer 
def get_tasks(user: UserLogin):
    tasks_list = []
    for docket in docket_collection.find():
       if(docket["status"] == status.NEEDS_UPDATE.name and docket["relevant_officer"] == user["username"]): 
           tasks_list.append(docket)
    return tasks_list 

def update_occ_count():
    filter = { '_id': 'Occurrence' }
    # current value
    current = get_occ_count()
    current += 1
    # Values to be updated.
    newvalue = { "$set": { 'count': current } }
    # Using update_one() method for single
    # updation.
    counters_collection.update_one(filter, newvalue)

def get_occ_count():
    occurrence_number_dict = dict(counters_collection.find_one({"_id": "Occurrence"}))
    occurence_number = occurrence_number_dict['count']
    return occurence_number

def update_docket_count():
    filter = { '_id': 'Docket' }
    # current value
    current = get_docket_count()
    current += 1
    # Values to be updated.
    newvalue = { "$set": { 'count': current } }
    # Using update_one() method for single
    # updation.
    counters_collection.update_one(filter, newvalue)

def get_docket_count():
    docket_number_dict = dict(counters_collection.find_one({"_id": "Docket"}))
    docket_number = docket_number_dict['count']
    return docket_number

def update_evidence_count():
    filter = { '_id': 'Evidence' }
    # current value
    current = get_evidence_count()
    current += 1
    # Values to be updated.
    newvalue = { "$set": { 'count': current } }
    # Using update_one() method for single
    # updation.
    counters_collection.update_one(filter, newvalue)

def get_evidence_count():
    evidence_number_dict = dict(counters_collection.find_one({"_id": "Evidence"}))
    evidence_number = evidence_number_dict['count']
    return evidence_number


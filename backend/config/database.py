
# import the pymongo package
import pymongo
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

#counters_collection.insert_one({"_id": 'Occurrence', "count": 0})
#counters_collection.insert_one({"_id": 'Docket', "count": 0})
#counters_collection.insert_one({"_id": 'Evidence', "count": 0})

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
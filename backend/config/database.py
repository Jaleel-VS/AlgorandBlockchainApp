
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
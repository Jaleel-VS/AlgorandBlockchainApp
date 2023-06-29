import pymongo # importing the pymongo package

# Constants 
# the connection string to connect to the mongodb database

USER_NAME = "jaleel_admin"
PASSWORD = "5r0iuv7JDXh2LGaG"
DATABASE_NAME = "FairChanceDatabase"

CONNECTION_STRING = f"mongodb+srv://{USER_NAME}:{PASSWORD}@serverlessinstance0.ksq2r.mongodb.net/?retryWrites=true&w=majority"

# Connecting to the database

try:
    client = pymongo.MongoClient(CONNECTION_STRING)
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")
    exit()

# Getting the database
db = client.Fair_Chance_Database

# Getting the collection (one can think of a collection as a table in a relational database)
userCollection = db["User"]
stationCollection = db["Station"]


# Inserting a document in the collection (and a document is almost like a tuple)
#userCollection.insert_one({"badgeID": 1234567, "Unit Number": "890123", "ID Number": "0107250140087", "names": "Katlego Athena", "surnames":"Kgomari", "email":"katkgomari@gmail.com", "password": "password123",})


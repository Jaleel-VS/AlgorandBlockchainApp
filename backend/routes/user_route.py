# This is where we are going to do all the magic to go fetch our todos, create todos, update todos and delete todos

from fastapi import APIRouter # APIRouter is our routing interface
from models.user import User # We import the class todo
from config.database import userCollection# This is when we are going to be looking inside our mongodb client. collection is the todo_collection
from schema.user_schema import list_serial
from bson import ObjectId # This is what mongodb uses to be able to identify the id that it creates itself

user_router = APIRouter()

# GET Request Method 
# Inside here, we can create out fetch call from our mongodb
@user_router.get("/") # We leave it at the API endpoint of just the slash for our application
async def get_users(): # We don't need to pass in anything
    users = list_serial(userCollection.find()) # mongodb has this find functionality that it gets from pymongo. It means that we are going to find everthing in this collection and return it
    # And since we know that it is going to be todos, so we pass it through list_serial which is going to serialise all the data into a dictionary with key and value pairs 
    return users

# POST Request (In the beginning, we just has [] because we had not put anything intomour database yet)
@user_router.post("/")
async def create_user(user: User): # We insert into the database in a post request 
    userCollection.insert_one(dict(user)) # We pass in a dict because mongodb receives JSON-like documents

# PUT Request method (update)
@user_router.put("/{id}") # We pass in the id because we need to find the thing before we can update it. The id is going ti be the one that we get back from our nosql database
async def update_user_details(id:str, user: User):
    userCollection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)}) # The ObjectId comes from the bson that we imported earlier. We also want to make sure that it is a set
    # $set says to overwrite what is currently in the database with that specific object id's todo. We are going to find it and update it


# DELETE Request method
@user_router.delete("/{id}")
async def delete_user(id:str):
    userCollection.find_one_and_delete({"_id": ObjectId(id)})
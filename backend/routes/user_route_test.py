from fastapi import APIRouter
from models.user import User
from config.database import user_collection
from schema.user_schema import list_serial
from bson import ObjectId # This is what mongodb uses to be able to identify the id that it creates itself

user_router = APIRouter()
# GET request method
@user_router.get("/")
async def get_users():
    users = list_serial(user_collection.find())
    return users

# POST request method
@user_router.post("/")
async def post_user(user: User):
    user_collection.insert_one(dict(user))
    
# PUT Request method
@user_router.put("/{id}")
async def put_user(id:str, user: User):
    user_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

# DELETE request method 

@user_router.delete("/{id}")
async def delete_todo(id:str):
    user_collection.find_one_and_delete({"_id": ObjectId(id)})


# for the login 
@user_router.post("/login_test")
async def user_login(user: User): 
    #if user_collection.find_one({"badgeID": badge_id}, {"password": pass_word}) is None:
    #    print("BadgeID or password is incorrect!")
    #else:
    #   print("You have successfully logged in!")
    try:
        print("It worked!")
        return {"success": True}
    except:
        print("oops")

    

            
from fastapi import APIRouter
from models.user import User
from models.user_login import UserLogin
from config.database import user_collection
from schema.user_schema import list_serial
from bson import ObjectId # This is what mongodb uses to be able to identify the id that it creates itself

test_router = APIRouter()



# for the login 
@test_router.post("/login_test")
async def user_login(user: UserLogin): 
    try: 
        # user_dict = dict(user)
        # print(user_dict)
        # print("It worked!")
        # return {"success": True,
        #         "message": "User logged in successfully",
        #         "officerType": "senior",
        #         }
        user_dict = dict(user)
        user_object = user_collection.find_one({"badgeID": user_dict["username"]}) # It returns the entire object
        if user_object is not None:
            if user_dict["password"] == user_object["password"]:
                role = user_object["role"]
                #print(role)
                return{
                    "success": True,
                    "officerType": role,
                }
            else:
                return {
                    "success": False,
                    "message": "Password incorrect"
                }
        else:
            return {
                    "success": False,
                    "message": "User does not exist."
                }
            
                
    except Exception as e:
        print("oops")
        print(e)

    

            
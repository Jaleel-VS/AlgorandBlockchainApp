# NoSQL databases send it over to JSON but it is going to be hard for our pythin application to use it as an object 
# So we need to serialize this nosql information into someyhing that we can use within our application
# We first create an individual serialiser 
# So we connect our todo object to a dictionary so we can see the ids and the keys of each item 


# Below, we pass in a todo and we return a dictionary
def individual_serial(user) -> dict:
    return{
        # We return the key-value pair for everything
        "id": str(user["_id"]), # mongodb create this is for us. We wrap it into a string and wwe pull out the id
        "badgeID": user["badgeID"],
        "idNumber": user["idNumber"],
        "gender": user["gender"],
        "names": user["names"],
        "surnames": user["surnames"], 
        "password": user["password"],
        "unitNumber": user["unitNumber"],
        "rank": user["rank"],
        "phoneNumber": user["phoneNumber"],
        "homeNumber": user["homeNumber"],
        "email": user["email"],
        "nationalities": user["nationalities"],
        "residentialAddress": user["residentialAddress"], 
    }

# We then want to retrieve all of them. The code above just serializes one of the todos
# We want to be able to return all the todos 
# Below, we pass in todos and return a list 
def list_serial(users) -> list:
    return[individual_serial(user) for user in users ] # We run the function above for each todo in our todos
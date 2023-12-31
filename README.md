# This is the FairChance Docket Handling System
This web app is an online Police Docket Handling System that works with the Algorand Blockchain to detect and deter the tampering of police dockets by leveraging the immutability of the blockchain.

- A hash of the docket is sent to the Blockchain and sent to the user.
- If a docket produced by a police officer does not hash to the same hash, it means that the docket has been tampered with. 
### Team
- Katlego Kgomari | Team Lead, Backend
- Modjadji Francis | Lead Frontend
- Vuaya Timamputu | Frontend, Documentation
- JD van Staden | Frontend, Backend, Blockchain

### Tech Stack:
- Frontend: Svelte.JS 
- Backend: FastAPI
- Database: MongoDB
- Cloud storage: AWS S3 


### Instructions on how to run the app: 
- git clone the repository
- copy the .env file and paste in the backend directory
- cd into the backend and make a python virtual environment, and activate it
- run `pip install -r requirements.txt` to install the dependencies for the backend
- run `uvicorn main:app --reload` to start the backend server
- In a new terminal window, cd into the frontend directory
- cd into my-svelte-app and run `npm install` to install the dependencies for the frontend
- to run the frontend, run `npm run dev` in the my-svelte-app directory
- the app should be running on `localhost:8080`

See video demo here: 


- Here are examples of valid Basic officers {name: "SAP321", password: "IVSKRZP"; name: "SAP890", password: "SXHGKIR"; name: "SAP789", password: "DUKJPFA"}
- Here are examples of valid Senior officers {name: "SAP987", password: "RBTWNHG"; name: "SAP234", password: "PQJXTMR"; name: "SAP654", password: "WBFKMTN"}
- Basic officers can log an occurrence which is a detailing of what happened
- The basic officer then creates a docket(button appears when they click submit occurrence)
- Basic officers can also view dockets that need correcting (editing)
- They can also view dockets in general

- Senior officers can review dockets and approve or decline dockets
- If a docket has any errors that need to be corrected, the Senior Officer will reject the docket and add a comment
- If the docket is approved, it's hashed and sent to the blockchain


### Shortcomings
- The app is not fully functional, we were not able to implement the smart contract functionality, but instead used single transactions
- The app is not fully responsive
- The app doesn't have good user feedback when waiting for a response from the backend
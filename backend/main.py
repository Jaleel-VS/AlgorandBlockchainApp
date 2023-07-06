from fastapi import FastAPI
from routes.user_route import user_router

from routes.docket_route import docket_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4100",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    
    # Add more origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(docket_router)


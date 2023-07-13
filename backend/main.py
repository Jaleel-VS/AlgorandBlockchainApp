from fastapi import FastAPI
from routes.occurence_route import occurrence_router
from routes.evidence_route import evidence_router
from routes.docket_route import docket_router
from routes.test_route import test_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


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


app.include_router(docket_router)
app.include_router(test_router)
app.include_router(evidence_router)
app.include_router(occurrence_router)


if __name__ == "__main__":
    uvicorn.run(app)
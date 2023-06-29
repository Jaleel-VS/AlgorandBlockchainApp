from fastapi import FastAPI
#from routes.user_route import user_router
from routes.docket_route import docket_router

app = FastAPI()
#app.include_router(user_router)
app.include_router(docket_router)

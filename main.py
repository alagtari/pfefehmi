from cgi import test
from imp import reload
from fastapi import FastAPI
import  app.models as models
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from app.database import  engine
from  app.routes import auth,user,infrastructure,dynamicscan,project,connector




models.Base.metadata.create_all(bind=engine)   
    


origins = ["*"]
middleware = [ Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])]
app = FastAPI(middleware=middleware)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(auth.router)
app.include_router(user.router)
app.include_router(infrastructure.router)
app.include_router(dynamicscan.router)
app.include_router(project.router)
app.include_router(connector.router)


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app",  port=8000 ,reload=True)            

    
from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.project as project, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['projects'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/projects")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        projects = project.get_all(db)
        return {"status" : 200 , "data" : projects }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/projects")
async def create_user(projet :schemas.Projet,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        project.create(db,projet)
        return   {"status" : 200 , "message": "project created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    


@router.delete("/projects")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        project.delete(db=db, id=id)
        return {"status" :  200 , "message" : "project deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    




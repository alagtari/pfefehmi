import hashlib
from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.users as users, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['users'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/users/all")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        returned_users = users.get_users(db)
        return returned_users 
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/users/create")
async def create_user(user :schemas.User,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        db_user = users.get_user_by_email(db, email=user.email)
        if db_user:
          return {"status" : 400 , "message" : "User already exists"}
        password = hashlib.md5(user.password.encode())
        users.create_user(db=db, user=user,mdp=password.hexdigest())
        return   {"status" : 200 , "message": "user created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    


@router.delete("/users/delete")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        users.delete_user(db=db, id=id)
        return {"status" :  200 , "message" : "User deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    



@router.get('/users/info')
def get_info(request : Request , db: Session  = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        decoded = tokens.decode_token(token)
        email = decoded['user']['data']
        db_user = users.get_user_by_email(db, email=email)
        return {"status" : 200 , "data" : db_user}
    else:
        return{"status" : 401 ,"message":"token expired"}        
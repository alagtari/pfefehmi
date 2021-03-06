from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
import app.crud.users as users, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['Authentication'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post('/login')
def login( request:schemas.UserLogin ,db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=request.email)
    if not db_user:
       return {'status' :404  , 'message' : "Adresse Email incorrecte." }
    elif request.password != db_user.password:
          return {'status' :404  , 'message' : "Mot de passe incorrecte." }
    access_token = tokens.create_access_token(request.email)
    return {"access_token": access_token, "token_type": "bearer" , "status" : 200 , "id" : db_user.id}
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    users = db.query(models.User).all()    
    return users    


def delete_user(db: Session, id: int):
    db_user =db.query(models.User).filter(models.User.id == id).first()
    db.delete(db_user)
    db.commit()

def create_user(db: Session, user:schemas.User,mdp):
    db_user = models.User(name=user.name, email=user.email,password=mdp,role=user.role)
    db.add(db_user)
    db.flush()
    db.refresh(db_user)
    db.commit()
    



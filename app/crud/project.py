from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def get_by_id(db: Session, id: int):
    return db.query(models.Projet).filter(models.Projet.id == id).first()

def get_all(db: Session):
    Projets = db.query(models.Projet).all()    
    return Projets    


def delete(db: Session, id: int):
    Projet =db.query(models.Projet).filter(models.Projet.id == id).first()
    db.delete(Projet)
    db.commit()

def create(db: Session, Projet:schemas.Projet):
    Projet = models.Projet(url =Projet.url,date =Projet.date,total_vulnerability =Projet.total_vulnerability,high =Projet.high,medium =Projet.high,low =Projet.low)
    db.add(Projet)
    db.commit()
    




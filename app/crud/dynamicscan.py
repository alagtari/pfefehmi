from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def get_by_id(db: Session, id: int):
    return db.query(models.Dynamicscan).filter(models.Dynamicscan.id == id).first()

def get_all(db: Session):
    Dynamicscans = db.query(models.Dynamicscan).all()    
    return Dynamicscans    


def delete(db: Session, id: int):
    Dynamicscan =db.query(models.Dynamicscan).filter(models.Dynamicscan.id == id).first()
    db.delete(Dynamicscan)
    db.commit()

def create(db: Session, Dynamicscan:schemas.Dynamicscan):
    Dynamicscan = models.Dynamicscan(url =Dynamicscan.url,date =Dynamicscan.date,total =Dynamicscan.total,high =Dynamicscan.high,medium =Dynamicscan.high,low =Dynamicscan.low,status=Dynamicscan.status,scanner =Dynamicscan.scanner)
    db.add(Dynamicscan)
    db.commit()
    




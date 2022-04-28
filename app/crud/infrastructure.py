from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def get_by_id(db: Session, id: int):
    return db.query(models.Infrastructure).filter(models.Infrastructure.id == id).first()

def get_all(db: Session):
    Infrastructures = db.query(models.Infrastructure).all()    
    return Infrastructures    


def delete(db: Session, id: int):
    Infrastructure =db.query(models.Infrastructure).filter(models.Infrastructure.id == id).first()
    db.delete(Infrastructure)
    db.commit()

def create(db: Session, Infrastructure:schemas.Infrastructure):
    Infrastructure = models.Infrastructure(target =Infrastructure.target,date =Infrastructure.date,total =Infrastructure.total,high =Infrastructure.high,medium =Infrastructure.high,low =Infrastructure.low,status=Infrastructure.status,scanner =Infrastructure.scanner)
    db.add(Infrastructure)
    db.commit()
    




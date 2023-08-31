# [Standard Library]
from dataclasses import dataclass

# [3rd Party]
from sqlalchemy.orm import Session


@dataclass
class Crud:

    def get(self, db: Session, model: str, id: int):
        return db.query(model).filter(model.id == id).first()

    def get_all(self, db: Session, model: str):
        return db.query(model).all()

    def create(self, db: Session, model: str, data: dict):
        db_data = model(**data.dict())
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
        return db_data

    def delete(self, db: Session, model: str, id: int):
        db_data = db.query(model).filter(model.id == id).first()
        if db_data:
            db.delete(db_data)
            db.commit()
            return {"detail": "Record deleted successfully"}

    def update(self, db: Session, model: str, id: int, data: dict):
        db_data = db.query(model).filter(model.id == id).first()
        if db_data:
            for field, value in data.dict().items():
                setattr(db_data, field, value)
            db.commit()
            db.refresh(db_data)
            return db_data

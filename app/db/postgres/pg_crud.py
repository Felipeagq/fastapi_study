from app.db.db_core import Database

class PostgresDatabase(Database):
    
    @staticmethod
    def create(**kwargs):
        print("entro")
        db = kwargs.get("db")
        entity = kwargs.get("entity")
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity
    
    @staticmethod
    def read(**kwargs):
        db = kwargs.get("db")
        entity = kwargs.get("entity")
        print("entidad",entity)
        param = kwargs.get("param")
        if not param:
            q = db.query(entity).all()
            print(q)
        #  q = db.query(entity).filter(entity[param] == )
        else: 
            q = None
        print(q)
        return q 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


@contextmanager
def session_scope(session_maker, needCommit = True):
    session = session_maker()
    try:
        yield session
        if needCommit:
            session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        session.close()

class Connection:
    def __init__(self, tablename='states'):
        # Установка строки соединения базы данных
        connection_string = (
            "mssql+pyodbc://@DESKTOP-64OLUDH\SQLEXPRESS/DataBase?"
            "driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
        )
            
        # Создаем движок и таблицу
        engine = create_engine(connection_string)
        from models import States, Users, Base
        Base.metadata.create_all(engine)
    
        # Определение таблицы
        tables = {'states': States, 'users': Users}
        self.table = tables.get(tablename.lower())
    
        # Создание фабрики сессий
        self.Session = sessionmaker(bind=engine)
        


    def getAll(self):
        with session_scope(self.Session, False) as session:
            results = session.query(self.table).all()
            return results

    def create(self, data):
        with session_scope(self.Session) as session:
            post = self.table(**data)
            session.add(post)


    def get(self, id):
        with session_scope(self.Session, False) as session:
            res = session.query(self.table).get(id)
            return res

import psycopg2
from psycopg2.extras import RealDictCursor

from dotenv import load_dotenv
import os

load_dotenv()

class DBManager:
    def __init__(self):
        self.host = os.getenv('DATABASE_HOST'),
        self.database = os.getenv('DATABASE_NAME'),
        self.user = os.getenv('DATABASE_USER'),
        self.password = os.getenv('DATABASE_PASSWORD'),
        self.port = os.getenv('DATABASE_PORT')

    def _connect(self):
        conn = None
        try:
            conn = psycopg2.connect(
                host=os.getenv('DATABASE_HOST'),
                database=os.getenv('DATABASE_NAME'),
                user=os.getenv('DATABASE_USER'),
                password=os.getenv('DATABASE_PASSWORD'),
                port=os.getenv('DATABASE_PORT')
            )
            return conn
        except Exception as e:
            print(f'Ошибка соединения с БД: {e}')
            raise


    def execute_query(self, query, params=None, fetch=False):
        with self._connect() as conn:
            cursor = conn.cursor(cursor_factory=RealDictCursor)

            try:
                if isinstance(params, tuple):
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                if fetch:
                    return cursor.fetchall()
                
                else: 
                    conn.commit()
                    return True

            except Exception as e:
                conn.rollback()
                print(f"Ошибка выполнения SQL-запроса: {e}")
                raise
            finally:
                cursor.close()


    def getAll(self, id = None):
        if(id):
            query = f"SELECT * FROM articles WHERE user_key = {id}"
        else:
            query = f"SELECT * FROM articles"
        return self.execute_query(query, fetch=True)
    
    def getRow(self, id):
        query =f"SELECT * FROM articles WHERE article_key = {id}"
        return self.execute_query(query=query, fetch=True)
    
    def push(self, data):

        keys = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f'INSERT INTO articles ({keys}) VALUES ({placeholders});'
        
        return self.execute_query(query=query, params=tuple(data.values()))
    
    def update(self, data, id):
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f'UPDATE articles SET ({keys}) = ({placeholders}) WHERE article_key = {id};'
        
        return self.execute_query(query=query, params=tuple(data.values()))
    
    def delete(self, id):
        query = f"DELETE FROM articles WHERE article_key = {id};"
        return self.execute_query(query=query)
    
    def seacrh(self, data):
        conditions = []
        params = []

        for key, item in data.items():
            if item != '' and key is not None:
                conditions.append(f"{key} = %s")
                params.append(item)

        if conditions:
            where = " AND ".join(conditions)
            query = f"SELECT * FROM articles WHERE {where}"
        else:
            query = "SELECT * FROM articles"
        return self.execute_query(query=query, params=tuple(params), fetch=True)
    

    def login(self, login, password):
        user = self.execute_query(query="SELECT * FROM users WHERE login = %s;", params=(login,), fetch=True)
        if user:
            if password == user[0]['pass']:
                return user[0]
            else:
                return "Неправильный пароль"
        else:
            return "Пользователь не найден"
        
    def registration(self, data):
        # ищем существует ли пользователь
        user = self.execute_query(query="SELECT * FROM users WHERE login = %s;", params=(data['login'],), fetch=True)
        if user:
            return 'Пользователь уже есть'
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f'INSERT INTO users ({keys}) VALUES ({placeholders});'
        return self.execute_query(query=query, params=tuple(data.values())) 
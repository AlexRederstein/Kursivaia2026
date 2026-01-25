import psycopg2

def connect():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="root",
        password="root",
        port="5432"
    )

    return conn

def getAllArticles():
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute("SELECT * FROM articles;")
        return cur.fetchall()
    
    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        if conn is not None:
            conn.close()

def pushData(data):
    try:
        conn = connect()
        cur = conn.cursor()

        keys = ', '.join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        
        query = f"""
            INSERT INTO articles ({keys}) VALUES({placeholders});
            """
        
        values = tuple(data.values())
        cur.execute(query, values)
        conn.commit()

    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        if conn is not None:
            conn.close()

def updateData(data, id):
    try:
        conn = connect()
        cur = conn.cursor()

        query = f"""
            UPDATE articles SET title = %s, description = %s, text = %s WHERE article_key = %s;
            """
        
        # values = tuple(data.values())
        cur.execute(query, (data['title'], data['description'], data['text'], id))
        conn.commit()

    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        if conn is not None:
            conn.close()

def getArticle(id):
    try:
        conn = connect()
        cur = conn.cursor()
        
        query = f"""
            SELECT * FROM articles WHERE article_key = %s;
            """
        
        cur.execute(query, id)
        return cur.fetchone()

    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        if conn is not None:
            conn.close()


def deleteArticle(id):
    try:
        conn = connect()
        cur = conn.cursor()
        
        query = f"""
            DELETE FROM articles WHERE article_key = %s;
            """
        
        cur.execute(query, id)
        conn.commit()

    except Exception as e:
        print(f"Ошибка! {e}")
    finally:
        if conn is not None:
            conn.close()

# try:
    
#     conn = connect()
#     cur = conn.cursor
#     cur.execute("SELECT * FROM articles;")

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)

#     cur.close()

# except Exception as e:
#     print(f"Ошибка! {e}")

# finally:
#     if conn is not None:
#         conn.close()
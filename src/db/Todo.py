
class Todo:

    @classmethod
    def get_by_user_id(cls,id,cursor):
        cursor.execute("SELECT * FROM todos WHERE user_id=%s",(id))
        todos = cursor.fetchall()
        cursor.close()
        return todos
    
    @classmethod 
    def insert(cls,db,cursor,title,description,user_id):
        try:
            sentence = "INSERT INTO todos(id,title,description,done,user_id) VALUES(NULL,%s,%s,FALSE,%s)"
            cursor.execute(sentence,(title,description,user_id))
            db.commit()
        except Exception as e:
            print(e)
        cursor.close()

    @classmethod
    def delete_by_id(cls,db,cursor,id):
        cursor.execute("DELETE FROM todos WHERE id=%s",(id))
        db.commit()
        cursor.close()



class User:

    @classmethod
    def get_by_id(cls,id,cursor):
        cursor.execute("SELECT * FROM users WHERE id=%s",(id))
        users = cursor.fetchall()
        if len(users) == 0:
            return None
        cursor.close()
        return users[0]

    @classmethod
    def get_by_mail(cls,email,cursor):
        cursor.execute("SELECT * FROM users WHERE email=%s",(email))
        users = cursor.fetchall()
        if len(users) == 0:
            return None
        cursor.close()
        return users[0]

    @classmethod
    def insert(cls,db,cursor,name,username,password,email):
        print("Inserting {} {} {} {}".format(name,username,password,email))
        try:
            sentence = "INSERT INTO users VALUES(NULL,%s,%s,%s,%s)"
            cursor.execute(sentence,(name,username,password,email))
            db.commit()
        except Exception as e:
            print(e)
        print(cursor.fetchall())
        print("Inserted successfully")
        cursor.execute("SELECT * FROM users WHERE email=%s",(email))
        user = cursor.fetchall()[0]
        cursor.close()
        return user

        
        


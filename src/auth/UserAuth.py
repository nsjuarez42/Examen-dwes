from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class UserAuth(UserMixin):

    def __init__(self,id,name,username,password,email):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def hash_password(cls,password):
        return generate_password_hash(password)
    
    @classmethod
    def check_password(cls,hashed,password):
        return check_password_hash(hashed,password)

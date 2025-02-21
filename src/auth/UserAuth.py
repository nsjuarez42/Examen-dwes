from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class UserAuth(UserMixin):

    def __init__(self,id,name,username,password,email):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.email = email

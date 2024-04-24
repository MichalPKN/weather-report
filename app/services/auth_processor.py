import json
from flask_login import UserMixin

class AuthProcessor:
    def login_user(self, form):
        with open('app/data/users.json', 'r') as f:
            users = f.read()
            if not users:
                return None
            users = json.loads(users)
            for user in users:
                if form.name.data == user['name']:
                    if form.password.data == user['password']:
                        user = UserMixin()
                        user.id = form.name.data
                        return user
                    else:
                        return None
            return None
    
    def register_user(self, form):
        user = {
            'name': form.name.data,
            'password': form.password.data,
            'fav_cities': []
        }
        with open('app/data/users.json', 'r+') as f:
            users = f.read()
            if not users:
                f.write(json.dumps([user]))
            else:
                users = json.loads(users)
                users.append(user)
                f.seek(0)
                f.write(json.dumps(users))
        
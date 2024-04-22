import json

class AuthProcessor:
    #def __init__(self, user_repository):
    #    self.user_repository = user_repository

    def login(self):
        pass
    
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
        
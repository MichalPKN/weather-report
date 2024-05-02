import json
import sys

class FavCitiesService:

    def get_fav_cities(self, user_id):
        with open('app/data/users.json', 'r') as f:
            users = f.read()
            users = json.loads(users)
            for user in users:
                if user_id == user['name']:
                    print(user['fav_cities'], file=sys.stderr)
                    return user['fav_cities']

    def add_fav_city(self, user_id, city):
        print('adding city', file=sys.stderr)
        with open('app/data/users.json', 'r+') as f:
            users = f.read()
            users = json.loads(users)
            for user in users:
                if user_id == user['name']:
                    if city not in user['fav_cities']:
                        user['fav_cities'].append(city)
                        f.seek(0)
                        f.write(json.dumps(users))
                    return

    def remove_fav_city(self, user_id, city_name):
        with open('app/data/users.json', 'r+') as f:
            users = f.read()
            users = json.loads(users)
            for user in users:
                if user_id == user['name']:
                    user['fav_cities'].remove(city_name)
                    f.seek(0)
                    f.write(json.dumps(users))
                    return
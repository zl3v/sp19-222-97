from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "player": "VNY",
        "score": 2100,
        "level": 3,
        "playtime": 323
    },
    {
        "player": "AAA",
        "score": 8500,
        "level": 5,
        "playtime": 651
    },
    {
        "player": "ZCH",
        "score": 19200,
        "level": 6,
        "playtime": 923
    }
]
def get(player):
    for user in users:
        if(player == user["player"]):
            return user
    return "User not found"

def post(player, score, level, playtime):
    for user in users:
        if(player == user["player"]):
            return "User with player name {} already exists".format(player)

    user = {
        "player": player,
        "score": score,
        "level": level,
        "playtime": playtime
        }

    users.append(user)
    return user

def put(player, score, level, playtime):

    for user in users:
        if(player == player):
            user["score"] = score
            user["level"] = level
            user["playtime"] = playtime
            #return user

    user = {
        "player": player,
        "score": score,
        "level": level,
        "playtime": playtime
        }

    users.append(user)
    return #user

def delete(name):
    global users
    users = [user for user in users if user["player"] != name]
    return "{} is deleted.".format(name)

api.add_resource(User, "/user/<string:player>")
app.run(debug=True)

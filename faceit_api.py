import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

header = {"accept": "application/json", "Authorization": "Bearer {}".format(API_KEY)}
url = "https://open.faceit.com/data/v4"

def faceit_get_player_id(nickname):
    query_params = {"nickname": nickname}
    response = requests.get(url + "/players", headers=header, params=query_params)

    return response.json()["player_id"]

def faceit_get_player_avatar(nickname):
    query_params = {"nickname": nickname}
    response = requests.get(url + "/players", headers=header, params=query_params)

    return response.json()["avatar"]

def faceit_get_player_level(nickname):
    query_params = {"nickname": nickname}
    response = requests.get(url + "/players", headers=header, params=query_params)

    return response.json()["games"]["csgo"]["skill_level"]

def faceit_get_player_elo(nickname):
    query_params = {"nickname": nickname}
    response = requests.get(url + "/players", headers=header, params=query_params)

    return response.json()["games"]["csgo"]["faceit_elo"]

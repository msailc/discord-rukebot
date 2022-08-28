from faceit_api import *


def find_profile(nickname):
    profile = dict()

    profile["player_id"] = faceit_get_player_id(nickname)
    profile["player_avatar"] = faceit_get_player_avatar(nickname)

    player_level = str(faceit_get_player_level(nickname))
    profile["player_level"] = player_level
    if player_level == "3":
        profile["player_level"] = "3 - lmao nemas ruke brt"
    profile["player_elo"] = faceit_get_player_elo(nickname)

    return profile

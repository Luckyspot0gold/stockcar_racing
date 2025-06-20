# Local achievement storage
import shelve

def store_locally(achievement_data):
    with shelve.open("pending_achievements") as db:
        key = f"{achievement_data['player']}_{time.time()}"
        db[key] = achievement_data

import json

import redis

from src.service.schemas import DataInModel

redis_db = redis.Redis(host='redis', port=6379)


def add_data_to_db(data_in: DataInModel) -> None:
    key_in_db = str('users_id:') + str(data_in.user_id)
    value_in_db = data_in.data.json()
    redis_db.set(key_in_db, value_in_db)


def get_data_from_db(user_id):
    key = str('users_id:') + str(user_id)
    return json.loads(redis_db.get(key))


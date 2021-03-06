import jwt
import time

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: str):
    data = {"data":data}
    jwt.encode(key = SECRET_KEY , algorithm=ALGORITHM   , payload= data)
    data = {
        "ts":round(time.time() * 1000),#timestamp en ms
        "user":data,
    }

    access_token = jwt.encode(key = SECRET_KEY , algorithm=ALGORITHM , payload=data)
    return access_token


def verify_token(token:str) -> bool : 
    decoded = jwt.decode(key = SECRET_KEY , algorithms=ALGORITHM , jwt=token)
    ts = decoded['ts']
    current_ts = round(time.time() * 1000)
    if (current_ts - ts  < 3600000):
        return True
    else:
        return False

def decode_token(token:str):
    return jwt.decode(key = SECRET_KEY , algorithms=ALGORITHM , jwt=token)
import jwt

def generate_token(email, secret):
    payload = {
        'email': email
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token

def decode_token(token, secret):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload['email']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

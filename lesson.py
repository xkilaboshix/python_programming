import hashlib

# print(hashlib.sha256(b'test').hexdigest())
# print(hashlib.sha256(b'test').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

def get_digest(password):
    password = bytes(password, 'utf-8')
    digest = hashlib.sha256(password).hexdigest()
    return digest

db[user_name] = get_digest(user_pass)

print(db)

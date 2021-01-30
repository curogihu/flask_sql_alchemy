from werkzeug.security import safe_str_cmp  # https://werkzeug.palletsprojects.com/en/1.0.x/installation/#install-werkzeug
from user imoprt User


users = [
    # {
    #     'id': 1,
    #     'username': 'aaaa',
    #     'password': 'bbbb'
    # }
    User(1, 'aaaa', 'bbbb')
]

# username_mapping = {
#     'aaaa': {
#         'id': 1,
#         'username': 'aaaa',
#         'password': 'bbbb'
#     }
# }

username_mapping = {u.username: u for in users}

# userid_mapping = {
#     1: {
#         'id': 1,
#         'username': 'aaaa',
#         'password': 'bbbb'
#     }
# }

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)

    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        return user


def identify(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
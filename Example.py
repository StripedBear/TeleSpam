from Spammer import Spammer


"""Use my.telegram.org for getting api_id and api_hash. 
'phone' should be str."""

new_obj = Spammer(api_id, api_hash, phone)
new_obj.connect()

"""Example of importing the entire program."""

new_obj.get_chats()

"""Example of using only a spammer with ready-made databases. Each message must be on a separate line.
Delay should be from 15 sec. Check Telegram limits for sending messages. It`s change often"""

users = new_obj.base_opening('users_database.txt')
message = new_obj.base_opening('message_database.txt')
new_obj.spam(users, message, delay=20)

"""The same example, but the spam function takes lists as input"""

users = ['user1', 'user2', 'user3']
message = ['Hello!', 'Ola!', 'Ni Hao!']
new_obj.spam(users, message, delay=20)

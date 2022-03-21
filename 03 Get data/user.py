from peewee import *

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    username = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User], safe=True)

# fields = [User.username, User.email]
# data = [
#     ('juli', 'juli@test.com'),
#     ('agus', 'agus@test.com'),
#     ('kadek', 'kadek@test.com'),
#     ('komang', 'komang@test.com'),
# ]
#
# User.insert_many(data, fields=fields).execute()

# get data
# method 1
user1 = User.get(id=1)
print(user1.username)

# method 2
user2 = User.get_by_id(2)
print(user2.username)

# method 3
user3 = User[3]
print(user3.username)

# method 4
query = User.select().dicts()
for user in query:
    print(user['email'])

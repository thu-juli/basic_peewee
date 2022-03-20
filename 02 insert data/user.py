from peewee import *

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User])

# insert data

# method 1
# User.create(name='test', email='test@test.test')

# method 2
# user = User(name='test2', email='test2@test.test')
# user.save()

# method 3
# User.insert(name='test2', email='test2@test.test').execute()

# insert many data

# method 1
# data_source = [
#     {'name':'test4', 'email':'test4@mail.test'},
#     {'name': 'test5', 'email': 'test5@mail.test'},
# ]
#
# User.insert_many(data_source).execute()

# method 2
fields = [User.name, User.email]
data = [
    ('test6', 'test6@mail.com'),
    ('test7', 'test7@mail.com'),
]

User.insert_many(data, fields=fields).execute()

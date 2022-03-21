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
# fields = [User.name, User.email]
# data = [
#     ('kim', 'kim@test.com'),
#     ('test1', 'test1@test.id'),
#     ('test2', 'test2@test.id'),
#     ('test3', 'test3@test.id'),
#     ('test4', 'test4@test.id'),
#     ('test5', 'test5@test.id'),
#     ('test6', 'test6@test.id'),
#     ('test7', 'test7@test.id'),
# ]
#
# print(User.insert_many(data, fields=fields).execute())

# get data
# query = User.select()
# for user in query:
#     print(user.email)

# filter data
# method 1 (search by spesific name)
# users = User.select().where(User.name=='test1')
# for user in users:
#     print(user.email)

# method 2 (search with contains)
users = User.select().where(User.name.contains('test'))
for user in users:
    print(user.email)

from peewee import *

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User])

# insert data
# data = [
#     {'name':'putu1'},
#     {'name':'putu2'},
#     {'name':'putu3'},
#     {'name':'putu4'},
#     {'name':'putu5'},
#     {'name':'putu6'},
#     {'name':'putu7'},
#     {'name':'putu8'},
#     {'name':'putu9'},
# ]
# print(User.insert_many(data).execute())

# count
# print(User.select().count())

# limit
# users = User.select().limit(5)
# for user in users:
#     print(user.name)

# paginataion
bots = User.select().paginate(1, 4)
for bot in bots:
    print(bot.name)

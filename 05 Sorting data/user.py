from peewee import *
import random, datetime

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()
    point = IntegerField()
    join_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User])


def get_rand():
    return random.randint(1, 100)


# insert data
# data = [
#     {'name': 'test1', 'point': get_rand()},
#     {'name': 'test2', 'point': get_rand()},
#     {'name': 'test3', 'point': get_rand()},
#     {'name': 'test4', 'point': get_rand()},
# ]
#
# User.insert_many(data).execute()

# Sorting data (Asc)
# users = User.select().order_by(User.point)
# for user in users:
#     print(user.name + '|' +str(user.point))

# Sorting data (Desc)
users = User.select().order_by(User.point.desc())
for user in users:
    print(user.name + '|' + str(user.point))

from peewee import *
import random
import datetime

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()
    point = IntegerField()
    join_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = sqlite_db


sqlite_db.connect()
sqlite_db.create_tables([User])


def data_rand():
    return random.randint(1, 100)


# insert data
# data = [
#     {'name': 'juli', 'point': data_rand()},
#     {'name': 'kadek', 'point': data_rand()},
#     {'name': 'komang', 'point': data_rand()},
#     {'name': 'agus', 'point': data_rand()},
# ]
#
# print(User.insert_many(data).execute())

# update data
# method 1
# users = User.select().where(User.name == 'juli').get()
# users.name = 'julianta'
# users.point = 99
# users.save()

# method 2
User.update(point=90).where(User.name == 'agus').execute()

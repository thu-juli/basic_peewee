from peewee import *
import datetime, random

sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()
    point = IntegerField()
    join_ad = DateTimeField(default=datetime.datetime.now())

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

# delete data
# delete single data
# user = User.get(User.name == 'agus')
# user.delete_instance()

# delete all data
User.delete().where(User.point < 100).execute()

from peewee import *

# koneksi ke database
sqlite_db = SqliteDatabase('user.db')


class User(Model):
    name = CharField()
    email = CharField()

    class Meta:
        # assignment ke database
        database = sqlite_db


# debug on sqlite
sqlite_db.connect()
sqlite_db.create_tables([User])

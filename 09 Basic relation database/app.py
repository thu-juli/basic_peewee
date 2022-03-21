from peewee import *
import datetime

sqlite_db = SqliteDatabase('tweet.db')


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class User(BaseModel):
    username = CharField(unique=True)


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    massage = TextField()
    join_at = DateTimeField(default=datetime.datetime.now())


sqlite_db.connect()
sqlite_db.create_tables([User, Tweet])

data = [
    ('hilman', ('ini tweet pertama saya', 'ini tweets kedua saya')),
    ('django', ('hallo dunia', 'iam django, framework python')),
    ('juli', ('hi', 'halo')),
]

for username, tweets in data:
    user = User.create(username=username)
    for tweet in tweets:
        Tweet.create(user=user, massage=tweet)

from peewee import *
import datetime

sqlite_db = SqliteDatabase('tweet.db')


class BaseModeL(Model):
    class Meta:
        database = sqlite_db


class User(BaseModeL):
    username = CharField(unique=True)


class Tweet(BaseModeL):
    user = ForeignKeyField(User, backref='tweets')
    massage = TextField()
    join_at = DateTimeField(default=datetime.datetime.now())


sqlite_db.connect()
sqlite_db.create_tables([User, Tweet])

# insert data
# data = [
#     ('putu', ('hallo', 'ini tweet kedua', 'ini lagi satu')),
#     ('agus', ('wibu', 'awas ada wibu')),
#     ('kadek', ('halo dunia', 'hati ini hancur')),
# ]
#
# for username, tweets in data:
#     user = User.create(username=username)
#     for tweet in tweets:
#         Tweet.create(user=user, massage=tweet)

# Memanggil data relasi
# method 1 (all tweets)
# tweets = Tweet.select().join(User)
# for tweet in tweets:
#     print(tweet.massage)
#
# method 2 (tweets filter by )
# tweets = Tweet.select().join(User).where(User.username == 'putu')
# for tweet in tweets:
#     print(tweet.massage)
# method 3 (use attribut backref)
agus_tweets = User.get(User.username == 'agus')
for tweet in agus_tweets.tweets:
    print(tweet.massage)

from peewee import *
import datetime

db = SqliteDatabase('highscore.db')

class HighscoreList(Model):
    name = TextField()
    score = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class Highscore():
    def __init__(self):
        db.connect()
        db.create_tables([HighscoreList])

    def append(self, name, score):
        HighscoreList(name=name, score=score).save()

    def get(self):
        return HighscoreList.select()


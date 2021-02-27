from peewee import *
from datetime import datetime

conn = SqliteDatabase('feedparser.sqlite', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0
})

class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше

class Sites(BaseModel):
    site_id = PrimaryKeyField(column_name='SitesId',null=False)
    site_name = CharField(column_name='SiteName')
    site_url = TextField(column_name='SiteUrl')

    class Meta:
        table_name = 'Sites'

class News(BaseModel):
    news_id = PrimaryKeyField(column_name='NewsId',null=False)
    site_id = IntegerField(column_name='SiteId',null=True)
    title = CharField(column_name='Title',null=True)
    summary = TextField(column_name='Summary',null=True)
    link = TextField(column_name='Link',null=True)
    publish_date = DateTimeField(column_name='PublishDate',null=True)

    class Meta:
        table_name = 'News'

class Users(BaseModel):
    user_id = PrimaryKeyField(column_name='UserId',null=False)
    user_name = CharField(column_name='UserName')

    class Meta:
        table_name = 'Users'


class Sended(BaseModel):
    send_id = PrimaryKeyField(column_name='SendId',null=False)
    send_user = IntegerField(column_name='user_id')
    send_news = IntegerField(column_name='news_id')
    send_dttm = DateTimeField(default=datetime.now())

    class Meta:
        table_name = 'Sended'

class UserFeeds(BaseModel):
    userfeeds_id = PrimaryKeyField(column_name='UserFeedsId',null=False)
    user_id = IntegerField(column_name='user_id')
    site_id = IntegerField(column_name='site_id')

    class Meta:
        table_name = 'UserFeeds'

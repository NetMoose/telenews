#!/usr/bin/env python3
import feedparser
from datetime import datetime
import time
from peewee import *
from models import *

# Init tables and static data
Sites.create_table()
News.create_table()
Users.create_table()
Sended.create_table()
UserFeeds.create_table()

Sites.get_or_create(site_name='E1',        site_url= 'https://www.e1.ru/news/rdf/full.xml')
Sites.get_or_create(site_name='StranNick', site_url= 'https://strannick-ru.livejournal.com/data/rss')

Users.get_or_create(user_name='User 1')
Users.get_or_create(user_name='User 2')

UserFeeds.get_or_create(user_id=1, site_id=1)
UserFeeds.get_or_create(user_id=1, site_id=2)
UserFeeds.get_or_create(user_id=2, site_id=1)
UserFeeds.get_or_create(user_id=2, site_id=2)

Sended.get_or_create(send_user=1,send_news=1,send_dttm=datetime.now())
Sended.get_or_create(send_user=1,send_news=2,send_dttm=datetime.now())

# Get news
while True:
    conn.connect(reuse_if_open=True)

    for site in Sites.select().dicts().execute():
        NewsFeed = feedparser.parse(site['site_url'])

        for feed in NewsFeed.entries:
            News.get_or_create(site_id=site['site_id'],title=feed.title,summary=feed.summary,link=feed.id,publish_date=time.mktime(feed.published_parsed))

    print('-'*30)

    conn.close()
    time.sleep(15)

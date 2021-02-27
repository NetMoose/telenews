#!/usr/bin/env python3
from peewee import *
from models import *


conn.connect(reuse_if_open=True)



for user in Users.select().dicts().execute():
    for site in UserFeeds.select(UserFeeds.site_id).where(UserFeeds.user_id==user['user_id']).dicts().execute():

        news = (News
        .select()
        .where(
            News.news_id
            .not_in(
                Sended
                .select(Sended.send_news)
                .where(Sended.send_user == user['user_id'])
            )
            & News.site_id == site['site_id']
        )
        .dicts()
        .execute())

        for n in news:
            print(n)


    print('-'*40)


conn.close()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

# 简书的全站用户信息
class JianshuSpiderItem(Item):
    # 用户id
    userId = Field()
    # 用户名称
    name = Field()
    # 用户个人介绍
    userDesc = Field()
    # 关注数
    followNumber = Field()
    # 粉丝数
    fansNumber = Field()
    # 文章数
    articleNumber = Field()
    # 字数
    wordCount = Field()
    # 收获喜欢数
    likeNumber = Field()

# -*- coding: utf-8 -*-
# 使用CrawlSpider、LinkExtractors、Rule 爬取简书全站用户数据
# 参考 https://www.jianshu.com/p/7c5d41c61ad2 https://www.jianshu.com/p/32aa01074268
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from jianshu_spider.items import JianshuSpiderItem

# 最重要的是继承 CrawlSpider
class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    # https://www.jianshu.com/u/b3b2c03354f3
    start_urls = ['https://www.jianshu.com/']

    # response中提取链接的匹配规则，得出符合条件的链接
    pattern = '.*jianshu.com/u/*.'
    pagelink = LinkExtractor(allow=pattern)

    # 可以写多个rule规则
    rules = [
        # 只要符合匹配规则，在rule中都会发送请求，同时调用回调函数处理响应。
        # rule就是批量处理请求。
        Rule(pagelink,callback='parse_page',follow=True)
    ]

    # 不能写parse方法，因为源码中已经有了，会覆盖导致程序不能跑
    def parse_page(self, response):
        print('======================================')
        for each in response.xpath("//div[@class='main-top']"):
            item = JianshuSpiderItem()
            # 用户id
            item['userId'] = each.xpath("./a[@class='avatar']/@href").extract()[0]
            item['userId'] = str(item.get('userId')).replace('/u/','')
            # 用户名称
            item['name'] = each.xpath("./div[@class='title']/a/text()").extract()[0]
            # 用户个人介绍
            item['userDesc'] = each.xpath("//div[@class='js-intro']/text()").extract()[0]
            # 关注数
            item['followNumber'] = each.xpath("./div[@class='info']/ul/li[1]//a/p/text()").extract()[0]
            # 粉丝数
            item['fansNumber'] = each.xpath("./div[@class='info']/ul/li[2]//a/p/text()").extract()[0]
            # 文章数
            item['articleNumber'] = each.xpath("./div[@class='info']/ul/li[3]//a/p/text()").extract()[0]
            # 字数
            item['wordCount'] = each.xpath("./div[@class='info']/ul/li[4]//p/text()").extract()[0]
            # 收获喜欢数
            item['likeNumber'] = each.xpath("./div[@class='info']/ul/li[5]//p/text()").extract()[0]

            # 把数据交给管道文件
            yield item
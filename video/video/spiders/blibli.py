# -*- coding: utf-8 -*-
import re
from video.items import VideoItem
import scrapy
import time
from scrapy.http import Request

class BlibliSpider(scrapy.Spider):
    name = 'blibli'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS":{
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Referer": "https://www.bilibili.com/v/life/daily/?spm_id_from=333.334.b_7072696d6172795f6d656e75.59"
        },
    }

    def start_requests(self):
        for i in range(1,136866):# 生活日常
            url = "https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_6284334898209947&rid=21&type=0&pn={0}&ps=20&jsonp=jsonp&_={1}".format(i,int(time.time()*1000))
            print(url)
            yield Request(url,meta={"page":i})

    def parse(self, response):
        print("这是第%s页:"%response.meta['page'],response.url)
        video_aid = set(re.findall('"aid":(\d+)', response.text))
        # print(video_aid)
        for id in video_aid:
            video_url = "https://www.bilibili.com/video/av%s" % (id)
            yield Request(video_url,callback=self.get_video_url)

    def get_video_url(self,response):
        item = VideoItem()
        url_video_url = re.findall('"baseUrl":"(.*?)"', response.text)[0]
        item['url'] = url_video_url
        yield item






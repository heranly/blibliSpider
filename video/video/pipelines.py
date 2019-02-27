# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from hashlib import md5
import os
class VideoPipeline(object):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Referer": "https://www.bilibili.com/v/life/daily/?spm_id_from=333.334.b_7072696d6172795f6d656e75.59"
    }
    path = "E:\项目\视频集"
    def process_item(self, item, spider):
        url = item['url']
        response = requests.get(url, headers=self.headers)
        video_path = "{0}\{1}.mp4".format(self.path,md5(url.encode()).hexdigest())
        if not os.path.exists(video_path):
            try:
                with open(video_path, "ab") as f:
                    f.write(response.content)
                print("Successful download",video_path)
            except Exception as e:
                print("哎呀，下载失败啦，错误类型:",e)
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ScrapyDemoPipeline(object):
#     def process_item(self, item, spider):
#         return item


import os
import json
import codecs
import requests


# 存储数据
class JsonboxPipeline(object):
    def process_item(self, item, spider):
        path_name = 'jsonbox'

        # 创建文件夹
        if not os.path.exists(path_name):
            os.makedirs(path_name)

        # 存储
        file_name = path_name + '/' + 'news.json'
        with codecs.open(file_name, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item


# 存储图片
class ImgboxPipeline(object):
    def process_item(self, item, spider):
        path_name = 'imgbox'

        # 创建文件夹
        if not os.path.exists(path_name):
            os.makedirs(path_name)

        # 尝试下载
        try:
            pic = requests.get(item['cover'], timeout=20)
        except:
            print("无法下载图片！")

        # 存储
        file_name = path_name + '/' + item['title'] + '.jpg'
        f = open(file_name, "wb")
        f.write(pic.content)
        f.close()

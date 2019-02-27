#_*_encoding:utf-8_*_
#Author:Heranly
#BuiltTime:2019/2/27 17:06
from scrapy.cmdline import execute
execute("scrapy crawl blibli".split())

#Run multiple programs simultaneously
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# process = CrawlerProcess(get_project_settings())
# process.crawl("blibli")











# -*- coding: utf-8 -*-
### Set up cookie

BOT_NAME = 'weibo-search'
SPIDER_MODULES = ['weibo-search.spiders']
NEWSPIDER_MODULE = 'weibo-search.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# The time to wait after visiting one page and then visiting the next one, the default is 10 seconds
DOWNLOAD_DELAY = 10
#the value we need to fill in，After obtaining it, replace "your cookie" with a real cookie.
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'your cookie'
}
ITEM_PIPELINES = {
    'weibo-search.pipelines.DuplicatesPipeline': 300,
    'weibo-search.pipelines.CsvPipeline': 301,
    # 'weibo-search.pipelines.MysqlPipeline': 302,
    # 'weibo-search.pipelines.MongoPipeline': 303,
    # 'weibo-search.pipelines.MyImagesPipeline': 304,
    # 'weibo-search.pipelines.MyVideoPipeline': 305
}
# The keyword list to be searched, can write multiple, the value can be a list composed of keywords or topics, or the path of a txt file containing keywords，
# For example, there is a line for each keyword in the keyword_list.txt',txt file.
KEYWORD_LIST = ['疫苗']  # or KEYWORD_LIST = 'keyword_list.txt'
# The type of Weibo to search, 0 means to search all Weibo, 1 means to search all original Weibo, 2 represents hot Weibo, 3 represents follower Weibo, 4 represents certified user Weibo, 5 represents media Weibo, 6 represents viewpoint Weibo
WEIBO_TYPE = 1
# The contents that must be included in the Weibo filter results. 0 means not to filter and get all Weibo. 1 represents the search for Weibo containing pictures, 2 represents Weibo containing videos, 3 represents Weibo containing music, and 4 represents Weibo containing short links.
CONTAIN_TYPE = 0
# Filter the posting area of ​​Weibo, accurate to the province or municipality directly under the Central Government, the value should not contain words such as "province" or "city", if you want to filter the Weibo of Beijing, please use "Beijing" instead of "Beijing", you want to filter Please use "Anhui" instead of "Anhui Province" for Weibo in Anhui Province. You can write multiple regions.
# For the specific supported place names, please see the region.py file. Note that only the names of provinces or municipalities directly under the Central Government are supported. The names of cities under the province and the districts and counties under the municipalities directly under the Central Government are not supported. If you do not screen them, please use "all."“
REGION = ['全部']
# The start date of the search, in the form yyyy-mm-dd, and the search results include this date
START_DATE = '2020-03-01'
# The end date of the search, in the form of yyyy-mm-dd, and the search result contains this date
END_DATE = '2020-03-01'
# Further subdivide the search threshold. If the number of result pages is greater than or equal to this value, it is considered that the results are not fully displayed, and the subdivided search criteria are searched again to obtain more Weibo. The larger the value, the faster the speed, and the more likely it is to miss Weibo; the smaller the value, the slower the speed, the more Weibo you get.
# It is recommended to set the value between 40 and 50.
FURTHER_THRESHOLD = 46
# Image file storage path
IMAGES_STORE = './'
# Video file storage path
FILES_STORE = './'

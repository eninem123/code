import redis
from urllib import parse

# Redis configuration
r = redis.Redis(host='127.0.0.1', port=6379)

# 改写keywords和page_count
keywords = input("请输入关键字:")
page_count = int(input("请输入爬取最大页数:"))

keywords = parse.quote(keywords)
current_page = 1
start_index = 1

url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt' \
      '=1&stop=1&vt=2&wq={1}&page={2}&s={3}&click=0'

for i in range(page_count):
    r.lpush('JDUrlsSpider:start_urls', url.format(keywords, keywords, current_page, start_index))
    print("第%s页输出完成" % (int(i)))
    current_page += 2
    start_index += 60
# Python 爬虫合集

多平台 Python 爬虫脚本集合，覆盖电商、社交、内容等多个领域，学习研究用。

## 功能特性

### 电商平台
- 京东爬虫 - 基于 Scrapy 框架，支持商品 URL 抓取、详情页解析、评论爬取

### 社交媒体
- 微信公众号爬虫 - 公众号文章与粉丝信息采集
- 微博爬虫 - 微博内容与用户数据抓取
- 知乎爬虫 - 知乎问答与用户信息采集
- 豆瓣爬虫 - 豆瓣图书/电影/评论数据爬取

### 工具组件
- IP 代理池 - 高匿代理 IP 池自动维护
- 词云生成 - 基于爬取数据生成词云可视化
- Excel 处理 - 爬虫数据 Excel 导入导出

## 技术栈

- Python 3.x
- Scrapy, requests, BeautifulSoup
- 浏览器自动化
- pandas, openpyxl
- wordcloud, matplotlib

## 项目结构

```
.
├── JDspider/          # 京东 Scrapy 爬虫
├── robot/             # 微信机器人
├── ippool.py          # IP 代理池
├── ciyun.py           # 词云生成
├── weibospider.py     # 微博爬虫
├── zhIhudemo.py       # 知乎爬虫
├── doubanspider.py    # 豆瓣爬虫
├── googlespider.py    # 谷歌爬虫
└── exceldemo.py       # Excel 处理
```

## 快速开始

```bash
pip install requests beautifulsoup4 scrapy pandas openpyxl wordcloud matplotlib
```

## 免责声明

- 本项目仅供学习研究使用，请勿用于商业用途
- 使用时请遵守各平台 robots.txt 协议和相关法律法规

## License

MIT License

## Django + Scrapy + Postgresql(爬虫demo)

#### env
python3.6

`pip install -r requirements.txt`

#### configure postgresql

配置django_demo/settings.py中DATABASES

`DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}`

#### run

项目根目录下

`python manage.py makemigrations`
`python manage.py migrate`

进入scrapy项目spiderbot目录

`cd ./bots/spiderbot/`

运行scrapyd

`scrapyd`

另起一个Terminal

`scrapyd-deploy`

运行爬虫

` curl http://localhost:6800/schedule.json -d project=spiderbot -d spider=tuhu_tire`

#### 新增功能

增加京东/天猫/途虎爬虫

运行京东爬虫

`curl http://localhost:6800/schedule.json -d project=spiderbot -d spider=jingdong`

运行天猫爬虫

`curl http://localhost:6800/schedule.json -d project=spiderbot -d spider=tmall`

运行途虎爬虫

`curl http://localhost:6800/schedule.json -d project=spiderbot -d spider=tuhu`

爬取数据自动存入指定数据库并生成table

数据库设置

`
DATABASES = {
    
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '***',
        'USER': '***',
        'PASSWORD': '***',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
`

table名称修改

`db_table = 'th_db'`

爬取数据项修改：取消对应注释项即可

    base_url = 'https://list.tmall.com/search_product.htm?q=轮胎&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=刹车片&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=雨刷&enc=utf-8'
    # base_url = 'https://list.tmall.com/search_product.htm?q=机油&enc=utf-8'


#### buglist

- HTML解析不稳定
- URL暂时不支持外部输入

##### -------------------------cmd  项目运行
1. cd bots\spiderbot

## 启动scrapy服务
2. scrapyd

## 部署爬虫
3. cd bots\spiderbot --> python C:\Users\chezhudianping\Anaconda3\Scripts\scrapyd-deploy target -p spiderbot

## curl 运行爬虫
4. curl http://localhost:6800/schedule.json -d project=spiderbot -d spider=jingdong



###### ------------------------数据结构变化迁移  make    (# models --> default)
项目名  python manage.py makemigrations    (# 1  -->  exit  -->  项目名python manage.py makemigrations )
项目名  python manage.py migrate



###### ------------------------scrapy shell 调试
 1. cd bots\spiderbot
 2. scrapy shell <url> 要爬取数据页面的网址
 3. In [1]: response.xpath('.//ul[@class="gl-warp clearfix"]//div[@class="p-name p-name-type-2"]/a/@href').extract()
    Out[1]: ````


###### ------------------------Excel数据导出
1. 打开一个Excel
2. 菜单栏 --> 数据 --> 获取数据 --> (右击)传统向导 --> 从文本 --> 下一步....
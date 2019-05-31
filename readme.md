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


#### buglist

- HTML解析不稳定
- URL暂时不支持外部输入
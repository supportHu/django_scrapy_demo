#!/usr/bin/env python
# encoding=utf8
import time

import requests
from lxml import etree
from threading import Timer


def main():
    # partsListx = ['轮胎', '轮毂', '刹车鼓', '刹车片', '刹车盘', '雨刷',
    # '机油', '火花塞', '电瓶', '玻璃水', '防冻液',
    # ]

    partsListx = ['轮胎']
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'
    }

    base_url = [
        'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&'
        'vt=2&stock=1&page={}&s=104&click=0'.format(keyword, str(page)) for keyword in partsListx for page in
        range(1, 4)
    ]

    for i in base_url:
        try:
            time.sleep(1)
            print(i)
            # r = urllib.request.Request(i, headers=header)   #伪装浏览器访问
            # products = urllib.request.urlopen(r)    ##读取网页
            # soup = BeautifulSoup(products, 'lxml')  # 解析
            # print(soup)

            # t = time.sleep(3)  # 60秒爬取一次
            # start()  # 开始爬取

            r = requests.get(i, headers=header)
            r.encoding = "utf-8"  # 中文编码字符
            products = etree.HTML(r.text)
            types = (str(products.xpath('/html/head/title/text()')).split('-')[0]).strip("['")
            print(types)

            product = products.xpath('.//ul[@class="gl-warp clearfix"]/li')

            part = {
                'type': [],
                'brand': [],
                'property': [],
                'price': [],
                'shop': [],
            }

            resultx = []
            for j in product:
                try:
                    barnd = j.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()')  # 定位获取em标签文本
                    part['brand'] = ''.join(barnd[0])  # 获取em第一个值:品牌
                    part['property'] = ''.join(barnd[-1])  # 获取em倒数第一个值:特性

                    price = j.xpath('.//div[@class="p-price"]/strong/*/text()')
                    pri = ""
                    for x in range(0, len(price)):
                        pri += price[x]
                    part['price'] = ''.join(pri)  # 获取价格 --> ￥ + 数字

                    part['type'] = ''.join(types)  # 获取-车配件类型

                    ss = ""
                    for k, v in part.items():
                        ss += k + ':' + str(v) + "-|-"

                    # print(ss)
                    resultx.append(ss.strip("|"))
                except Exception as ex:
                    print('exception : ' + ex)

            with open('D:\\info.txt', 'w', encoding='utf-8') as f:
                print(len(resultx))
                for re in resultx:
                    f.write(str(re) + "\n")
        except Exception as e:
            print('exception : ' + e)


if __name__ == '__main__':  # 需加上这句代码，这时是一种固定的写法
    # pool()有一个参数，processes，表示有多少个进程,比如processes=2
    # pool = ThreadPool()     # 网上大部分使用的是pool = Pool()，但是经过多次尝试总是失败，然后改成了这样的。
    #
    # pool.map(get_all_list_info, urlStr)     #两个参数，第一个为调用的方法，该方法有参数，但是后边不写形参，map的第二个参数为一个迭代器，就是集合形式，会按顺序取其中的数据，作为参数传递给方法。
    # pool.close()
    # pool.join()

    main()

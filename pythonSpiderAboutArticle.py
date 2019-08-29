"""
使用之前请按照 request和lxml模块
"""

import pymysql
import requests
from lxml import etree
from time import sleep


def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }

    response = requests.get(url,headers = headers)
    content = response.content.decode()

    html = etree.HTML(content)
    title, = html.xpath('//div[@class="title"]/h1/text()')
    date = html.xpath('//div[@class="info"]/text()')[0].split(" ")[0]
    author, = html.xpath('//div[@class="info"]/a/text()')
    content = "\n".join(html.xpath('//div[@class="content "]/p/text()')[1:])
    print(title)
    if not title:
        title = "位命名"
    if not  date:
        date = "1970-01-01"
    if not  author:
        author = 1
    if not content:
        content = "empty"
    description = content[:20]+"......"
    return title,description,date,content,"images/01.jpg",1

def saveData(datas):
    connect = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "111111",
        database = "articleblog"
    )

    cursor = connect.cursor()
    sql = """INSERT INTO article_article (title, description, public_time, content, picture, article_author_id )
    VALUES
    ('%s','%s','%s','%s','%s','%s')"""%datas

    cursor.execute(sql)

    connect.commit()
    cursor.close()
    connect.close()
    print("save is ok")

def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    for i in range(10):
        url = "https://www.jj59.com/gushi/zheligushi/list_127_%s.html"%i
        response = requests.get(url, headers=headers)
        content = response.content.decode()
        html = etree.HTML(content)
        href = html.xpath('//li[@class="bd"]/h3/a/@href')
        for h in href:
            article_url = "https://www.jj59.com"+h
            datas = get_data(article_url)
            saveData(datas)
        sleep(1)
if __name__ == "__main__":
    get_page()
    # url = "https://www.jj59.com/jjart/428923.html"
    # datas = get_dhata(url)
    # saveData(datas)


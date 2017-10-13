#-*-coding:utf-8 -*-
import sys
import requests
from fake_useragent import UserAgent
from lxml import etree
import urlparse
import os
reload(sys)
sys.setdefaultencoding("utf-8")

'''
        <创建一个下载, 一拳超人 漫画的python脚本>
        url = "http://www.1kkk.com/manhua10684/"
        1: 获取所有 卷 的 url地址
        2: 获取 卷名--作为文件夹名, 第几页名--作为图片名  页的url(下载图片) Referer: 破解防盗链
'''

def url_list(url):
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
    }
    response = requests.get(url, headers=headers).content
    response = etree.HTML(response)
    li_list = response.xpath("//ul[@class='sy_nr1 cplist_ullg'][2]/li")
    href_list = []
    for li in li_list:
        href = li.xpath("a/@href")[0]
        href = urlparse.urljoin(url, href)
        href_list.append(href)
    return href_list


def parse_datail(*args):
    href_list = args[0]
    print '-----', type(href_list),href_list
    for href in href_list:
        # 得到 response
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
        }
        response = requests.get(href, headers=headers).content
        response = etree.HTML(response)
        # 获取 卷名--作为文件夹名, 第几页名--作为图片名  页的url(下载图片) Referer: 破解防盗链
        fine_name = response.xpath("//div[@class='view_bt']/h1/text()")[0].strip()
        print fine_name
        images = response.xpath("//div[@class='view_bt']/h1/font/span/text()")[-1]
        print images
        # 获取当前 文件所在位置
        os.mkdir(fine_name)

        for i in xrange(1, int(images)):
            image_path = os.path.join(fine_name, "%s.jpg" % str(i))
            img_name = os.path.join(fine_name,"%s.jpg" % str(i))
            print "+"*10, img_name
            img_page_url = href + "#ipg%s" %i
            #解析 img_page_url, 得到 图片的 src
            src = get_src(img_page_url, href)
            print "img_page_url------------", img_page_url
            # href--Referer,   img_url--图片url
            save_img(href, src, img_name, i)
            print image_path
            raw_input("88888888*******")


def get_src(img_page_url, href):
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Referer": href,
    }
    response = requests.get(img_page_url, headers=headers).text
    # request = urllib2.Request(img_page_url, headers=headers)
    # response = urllib2.urlopen(request).read()
    print response
    print '*' * 20, len(response), type(response)
    response = etree.HTML(response)

    src = response.xpath("//img")[0]
    print src, '55555555555555555555555555555555555555555555'
    print type(str)
    return src

def save_img(href, src, img_name, i):
    ua = UserAgent()
    href = href + "-p%s/" % i
    print href
    headers = {
        "User-Agent": ua.random,
        "Referer": href,
    }
    response = requests.get(src, headers=headers).content
    with open(img_name, "wb")as f:
        f.write(response)


if __name__ == '__main__':
    url = "http://www.1kkk.com/manhua10684/"
    href_list = url_list(url)
    parse_datail(href_list)
import os
import random
import shutil
import time
from hashlib import md5

import requests;
import re;
from pyquery import PyQuery as pq;
import json;

from bs4 import BeautifulSoup;

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'ozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
    'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
]
headers = {
    'Connection':'keep-alive',
    'Host':'www.instagram.com',
    'Referer':'http://www.instagram.com/instagram/',
    'User-Agent': random.choice(my_headers),
    'X-Requested-With':'XMLHttpRequest',
    # 'cookie': 'csrftoken=ZhNZ1hAmf5xnCAXHf55qDeJ0Npm6HMxo; mid=XTxkOAALAAEaF-WyKLT-XyUPKHwo; rur=ATN; urlgen="{\"172.105.210.43\": 63949}:1hvzk0:XEnx0HnTbyZfQxoIPNJ4ryMxW74"'
};

download_headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Host':'scontent-nrt1-1.cdninstagram.com',
        'Proxy-Connection':'keep-alive',
        'User-Agent':random.choice(my_headers),
        'Upgrade-Insecure-Requests':'1'
          };

proxy = {
    'http': 'http:127.0.0.1:1080',
    'https': 'http:127.0.0.1:1080'
}


#Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36
# url = "https://www.v2ex.com/";
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
# soup = BeautifulSoup(requests.get(url,headers= headers).text,"html.parser");
# for span in soup.find_all('span',id_="TopicsHot"):
#     print(span.find('div').text,span.find('a')['href']);
# https://www.instagram.com/giuliogroebert/
url_base = "http://www.instagram.com/";
uri = "https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%22{user_id}%22%2C%22first%22%3A12%2C%22after%22%3A%22{cursor}%22%7D";
def get_html(url):
    try:
        response = requests.get(url,headers = headers,proxies = proxy); #verify=False
        if response.status_code==200:
            return response.text;
        else:
            print("请求网页源代码错误,错误状态码: ",response.status_code);
    except Exception as e:
        print(e);
        return None;
# print(html);

def get_content(url):
    try:
        response = requests.get(url,url,headers = download_headers,proxies = proxy,timeout =10); #headers = headers,proxies = proxy,
        if response.status_code == 200 or response.status_code == 304:
            return response.content;
        else:
            print("请求图片二进制流错误，错误状态码为:"+response.status_code);
    except Exception as e:
        print(e);
        return None;


def get_json(url):
    try:
        respone = requests.get(url,headers = headers,proxies = proxy,timeout =10);
        if respone.status_code == 200:
            return respone.json();
        else:
            print("请求页面json出错，错误状态码: ",respone.status_code);
    except Exception as e:
        print(e);
        time.sleep(60 + float(random.randint(1,4000))/100);
        return get_json(url);

def get_urls(html):
    urls=[];
    user_id = re.findall('"profilePage_([0-9]+)"', html, re.S)[0]
    doc = pq(html);
    items =doc('script[type="text/javascript"]').items();
    for item in items:
        if item.text().strip().startswith("window._sharedData"):
            jsdata = json.loads(item.text()[21:-1],encoding="utf-8");
            edges = jsdata["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"];
            pageInfo = jsdata["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"];
            flag = pageInfo["has_next_page"];
            cursor = pageInfo["end_cursor"];
            for edge in edges:
                img_url = edge["node"]["display_url"];
                print(img_url);
                urls.append(img_url);
            print(flag,cursor);
    while flag:
        url = uri.format(user_id=user_id,cursor = cursor);
        json_data = get_json(url);
        edges = json_data["data"]["user"]["edge_owner_to_timeline_media"]["edges"];
        flag =  json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"];
        cursor = json_data["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"];
        for edge in edges:
            if edge["node"]["is_video"]:
                vidieo_url = edge["node"]["display_url"];
                print(vidieo_url);
                urls.append(vidieo_url);
            else:
                img_url = edge["node"]["display_url"];
                print(img_url);
                urls.append(img_url);
        print(flag,cursor,"urls: "+len(urls));
        time.sleep(4 + float(random.randint(1,800))/200)
    return urls;

def main(user):
    url = url_base + user + "/";
    html = get_html(url);
    urls = get_urls(html);
    dispath = "D:\instagram_pic\{0}".format(user);
    if not os.path.exists(dispath):
        os.mkdir(dispath);
    else:
       shutil.rmtree(dispath);
       os.mkdir(dispath);
    for i in range(len(urls)):
        print('\n正在下载第{0}张： '.format(i) + urls[i], ' 还剩{0}张'.format(len(urls) - i - 1));
        try:
            content = get_content(urls[i]);
            endw = "mp4" if r'mp4?nc_ht=scontent-nrt1-1.cdninstagram.com' in urls[i] else "jpg";
            file_path = r"D:\instagram_pic\{0}\{1}.{2}".format(user, md5(content).hexdigest(), endw);
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    print("第{0}张下载完成: ".format(i) + urls[i]);
                    f.write(content);
            else:
                print("第{0}张图片已下载: ".format(i));
        except Exception as e:
            print(e);
            print("图片or视频下载失败!");
if __name__ == '__main__':
    # main("giuliogroebert");
    print(headers)
    main("giuliogroebert")
    # path = "D:\instagram_pic\giuliogroebert";
    # if os.path.exists(path):
    #     shutil.rmtree(path);
    # else:
    #     os.mkdir(path);
    # my = {
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'Accept-Encoding':'gzip, deflate',
    #     'Accept-Language':'zh-CN,zh;q=0.9',
    #     'Host':'scontent-nrt1-1.cdninstagram.com',
    #     'Proxy-Connection':'keep-alive',
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    #     'Upgrade-Insecure-Requests':'1'
    #       };
    # con = "";
    # try:
    #     l = "http://scontent-nrt1-1.cdninstagram.com/vp/bc57761f6f4ee9a449b69ed22901ec56/5DEA6A69/t51.2885-15/e35/67694610_2315508448712123_3046831863627037334_n.jpg?_nc_ht=scontent-nrt1-1.cdninstagram.com";
    #     response = requests.get(l,l,headers = my,proxies = proxy); #headers = headers,proxies = proxy,
    #
    #     if response.status_code == 200 or response.status_code == 304:
    #         con = response.content;
    #         print(con);
    #     else:
    #         print("请求图片二进制流错误，错误状态码为:"+response.status_code);
    # except Exception as e:
    #     print(e);
    #     print(None)
    #
    # file_path = r"D:\instagram_pic\{0}\{1}.{2}".format("giuliogroebert",md5(con).hexdigest(), "jpg");
    # if not os.path.exists(file_path):
    #     # os.mkdir(file_path);
    #     with open(file_path,'wb') as f:
    #         f.write(con);


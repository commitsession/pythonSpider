import requests
import urllib,urllib.parse
import json
from bs4 import BeautifulSoup
import time
import openpyxl
import random

header = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    'Cookie': 'bid=DIuSbFmd4Bc; gr_user_id=468b0254-0097-48d9-9509-f4051b94654b; _vwo_uuid_v2=DA2CBBE054B6FD78A3AFFFFCFD00166BE|5abfa9f217b791c41bd539f562fdb697; __utmc=30149280; viewed="4913064_26715115_27047716_3709579"; ll="108296"; __utmc=223695111; __utmz=223695111.1548147477.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=w5x514Fu0dWPMelpsRLCWmYT66wtierL; ct=y; douban-fav-remind=1; __utmz=30149280.1548148474.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.81298697.1548056652.1548148474.1548153828.5; __utma=223695111.710364214.1548147477.1548147477.1548153828.2; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1548209652%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=f4f89b9a00fa963e.1548147477.3.1548209652.1548154421.; _pk_ses.100001.4cf6=*',
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
menu = ''

#保存结果到excel
def save_as_Excel(movie_dicts):
    wb = openpyxl.Workbook()
    i = 0
    for sheet in movie_dicts.keys():
        wb.create_sheet(index=i, title=sheet)
        sheet_name = wb.get_sheet_by_name(sheet)
        cell_list = movie_dicts[sheet]
        j = 0
        for cell in cell_list:
            sheet_name['A' + str(j + 1)].value = cell['rate']
            sheet_name['B' + str(j + 1)].value = cell['title']
            sheet_name['C' + str(j + 1)].value = cell['comment']
            sheet_name['D' + str(j + 1)].value = cell['url']
            j += 1
        i += 1

    wb.save("豆瓣电影-" + menu + '.xlsx')

#单个电影爬虫 只查询评论人数
def movie_spider(id):
    r = requests.get('https://movie.douban.com/subject/' + str(id), headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    # 获取具体信息 TODO
    # movie_info_list = soup.find('div', {'id': 'info'})
    movie_info_list = soup.find('div', {'id': 'interest_sectl'}).find('span', {'property': 'v:votes'})
    return movie_info_list.string.strip()

#分类标签爬虫 爬取某分类数据
def main_spider(movie_tag, type):
    type = type
    tag = movie_tag
    sort = 'recommend'
    page_limit = 5
    page_start = 0
    movie_list = []
    count = 0
    while (count <= 1):#直接请求json格式数据
        # https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%BA%AA%E5%BD%95%E7%89%87&sort=recommend&page_limit=20&page_start=40
        url = "https://movie.douban.com/j/search_subjects?type=" + type + "&tag=" + tag + "&sort=" + sort + "&page_limit=" + str(
            page_limit) + "&page_start=" + str(page_start)
        r = requests.get(url=url, headers=header)
        subjects = json.loads(r.text)
        for t in subjects['subjects']:
            time.sleep(random.randint(0, 3))
            comment = movie_spider(t['id'])
            t['comment'] = comment
            movie_list.append(t)
        count += 1
        page_start = count * 5

    return movie_list

#爬虫处理方法 爬取所有分类信息
def do_spider(dmove_tag_dict, type):
    movie_dicts = {}
    for movie_tag in dmovie_tag_dict:
        time.sleep(random.randint(0, 3))
        movie_list = main_spider(dmovie_tag_dict[movie_tag], type)
        # sorted(move_list, key=lambda x: x[0], reverse=True)
        movie_dicts[movie_tag] = movie_list
    return movie_dicts


if __name__ == '__main__':
    dmovie_tag_dict = {}
    type = ''
    movie_tag_dict = {'电影': ['经典', '可播放', '豆瓣高分', '冷门佳片', '华语', '欧美', '韩国',
                             '日本', '动作', '喜剧', '爱情', '科幻', '悬疑', '恐怖', '动画'],
                      '电视剧': ['美剧', '英剧', '韩剧', '日剧', '国产剧', '港剧', '日本动画', '综艺', '纪录片']}
    while True:
        print("输入分类：电影|电视剧")
        menu = input(">>")
        if menu == '电影':
            type = 'movie'
            for tag in movie_tag_dict['电影']:#编码分类
                dmovie_tag_dict[tag] = urllib.parse.quote(tag)
            st = time.time()
            movie_dicts = do_spider(dmovie_tag_dict, type)
            save_as_Excel(movie_dicts)
            et = time.time()
            print(st - et)#计算爬虫所需时间
            break
        elif menu == '电视剧':
            type = 'tv'
            for tag in movie_tag_dict['电视剧']:
                dmovie_tag_dict[tag] = urllib.parse.quote(tag)
            st = time.time()
            movie_dicts = do_spider(dmovie_tag_dict, type)
            save_as_Excel(movie_dicts)
            et = time.time()
            print(st - et)
            break
        else:
            continue

import urllib.request
from bs4 import BeautifulSoup

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'iuqxldmzr_=32; _ntes_nnid=b29adb7f8878b1c2f9345f90bfb4791f,1548315670341; _ntes_nuid=b29adb7f8878b1c2f9345f90bfb4791f; WM_NI=lhxgUf72pReNG3quFYJih5bo%2FnE3EsQmQdyAmVWQzHoSmeqQO%2F7kAyXy9Q17NF4xOPCFvWc%2FxM%2F667Y%2FuHvdoOrQL2bkR9BiQL5%2F8llx0ZP8Xh3pWksA5iI6VG%2Bw0I%2FTUGU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccae5b89bc8788b2409c928fa3c54f868f8b84b8688cf5fbdae839abf588d1cc2af0fea7c3b92ab0b8b888d86ef5eec0b3e84685edbf96c5538ab7a8d6e165edb28bd4c87993b39f85fc4baf8a99b2f944ad8da386f45b8df1f98cc4739ca7f7b2b43d8e9afc99ce5c819abab8e225bc93e1d7b53d9bf1bba9f570ad91beb2cf3aa2b59edac1639394fbd0bb68b0a800bbd3349cb8fd91d661b19ffb8acc3e9699e598b343ed8c9ba8d837e2a3; WM_TID=1m4m51V2vNNBVUBQEUd8lSr58fiz%2BX0M; JSESSIONID-WYYY=fAGqCAKOPXfkZ4jyHrEVP%2Fhp9nB6w%5CiyyK2qbXUeWCqHPj3fGof5h%5CZKMNky8QWDwCmVQdSOCZWqIAX2IjeJxzCR%2FWqq0NnIr%2B%2B%2B5dGB3hhxrq8cixY9DBqp9Pfcr6jNzMORA3kdZMWJF9NmXwkeSmmAQvmlCiZfjdzhrv0BbMUJFyEX%3A1548336290773',
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# https://music.163.com/#/artist/album?id=2116
url = 'https://music.163.com/artist/album'

'''
IN:
artist_id 歌手id
OUT:
album_infos = [{'album_id': '36875566', 'album_title': 'G.ream', 'album_time': '2017.12.07'},{}]

'''


def main_spider(artist_id='8888'):
    request = urllib.request.Request(url + '?id=' + artist_id, headers=header)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
    albums = soup.find('ul', {'class': 'm-cvrlst m-cvrlst-alb4 f-cb'})
    album_infos = []

    album_basic_infos = albums.find_all('p', {'class': 'dec dec-1 f-thide2 f-pre'})
    for album_basic_info in album_basic_infos:
        album_infod = {}
        album_info = []
        # print(album_basic_info.find_next_sibling())
        album_infod['album_id'] = album_basic_info.find_next()['href'].replace('/album?id=', '').strip()
        album_infod['album_title'] = album_basic_info['title']
        album_infod['album_time'] = album_basic_info.find_next_sibling().text
        album_info.append(album_basic_info.find_next()['href'].replace('/album?id=', '').strip())
        album_info.append(album_basic_info['title'])
        album_info.append(album_basic_info.find_next_sibling().text)
        album_infos.append(album_info)

    return album_infos

#main_spider()

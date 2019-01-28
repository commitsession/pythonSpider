import urllib.request
from bs4 import BeautifulSoup
import pymysql

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'iuqxldmzr_=32; _ntes_nnid=b29adb7f8878b1c2f9345f90bfb4791f,1548315670341; _ntes_nuid=b29adb7f8878b1c2f9345f90bfb4791f; WM_NI=lhxgUf72pReNG3quFYJih5bo%2FnE3EsQmQdyAmVWQzHoSmeqQO%2F7kAyXy9Q17NF4xOPCFvWc%2FxM%2F667Y%2FuHvdoOrQL2bkR9BiQL5%2F8llx0ZP8Xh3pWksA5iI6VG%2Bw0I%2FTUGU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccae5b89bc8788b2409c928fa3c54f868f8b84b8688cf5fbdae839abf588d1cc2af0fea7c3b92ab0b8b888d86ef5eec0b3e84685edbf96c5538ab7a8d6e165edb28bd4c87993b39f85fc4baf8a99b2f944ad8da386f45b8df1f98cc4739ca7f7b2b43d8e9afc99ce5c819abab8e225bc93e1d7b53d9bf1bba9f570ad91beb2cf3aa2b59edac1639394fbd0bb68b0a800bbd3349cb8fd91d661b19ffb8acc3e9699e598b343ed8c9ba8d837e2a3; WM_TID=1m4m51V2vNNBVUBQEUd8lSr58fiz%2BX0M; JSESSIONID-WYYY=6N6vMrNRl8bh9Q%5CckgY7h6HJAPUhrJOcbRupq%5CpZ5kugmT1pjSKM2SiH2ZaNDyHsJ0H1wRnRuBX7AY%5CScpGE3wK%2F1GXiC1ycAU2T12l%2Byks80Vx57v0w5YZOx8BOPHmztRdGYMfrnq2YFGpI6uMe6%2F6%2B5DAH53tf%5CAmrVedoypQTxsWJ%3A1548320951875',
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# https://music.163.com/#/discover/artist/cat?id=1002&initial=-1
url = 'https://music.163.com/discover/artist/cat'

'''
IN:
id 歌曲分类
initial 歌手分类
OUT:
artist_infos=[{'artist_id': '1087200', 'artist_name': 'AThree-Arslan', 'artist_extend_id': '60279611'},{}]
'''


def main_spider(id='1001', initial='-1'):
    request = urllib.request.Request(url + '?id=' + id + '&initial=' + initial, headers=header)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
    artists = soup.find('ul', {'id': 'm-artist-box'})
    artist_infos = []

    artist_basic_infos = artists.find_all('a', {'class': 'nm nm-icn f-thide s-fc0'})
    for artist_basic_info in artist_basic_infos:
        artist_infod = {}
        artist_info = []
        if artist_basic_info.find_next_sibling() is None:
            artist_extend_info = '-1'
        else:
            artist_extend_info = artist_basic_info.find_next_sibling()['href'].replace('/user/home?id=', '').strip()
        artist_infod['artist_id'] = artist_basic_info['href'].replace('/artist?id=', '').strip()
        artist_infod['artist_name'] = artist_basic_info.text[0:25]
        artist_infod['artist_extend_id'] = artist_extend_info
        artist_info.append(artist_basic_info['href'].replace('/artist?id=', '').strip())
        artist_info.append(artist_basic_info.text[0:25])
        artist_info.append(artist_extend_info)

        artist_infos.append(artist_info)
    return artist_infos

#print(main_spider('1001', '65'))

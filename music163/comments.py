import requests
import json

header = {
    'Accept': '*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'eep-alive',
    'Content-Length': '482',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=b29adb7f8878b1c2f9345f90bfb4791f,1548315670341; _ntes_nuid=b29adb7f8878b1c2f9345f90bfb4791f; WM_NI=lhxgUf72pReNG3quFYJih5bo%2FnE3EsQmQdyAmVWQzHoSmeqQO%2F7kAyXy9Q17NF4xOPCFvWc%2FxM%2F667Y%2FuHvdoOrQL2bkR9BiQL5%2F8llx0ZP8Xh3pWksA5iI6VG%2Bw0I%2FTUGU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccae5b89bc8788b2409c928fa3c54f868f8b84b8688cf5fbdae839abf588d1cc2af0fea7c3b92ab0b8b888d86ef5eec0b3e84685edbf96c5538ab7a8d6e165edb28bd4c87993b39f85fc4baf8a99b2f944ad8da386f45b8df1f98cc4739ca7f7b2b43d8e9afc99ce5c819abab8e225bc93e1d7b53d9bf1bba9f570ad91beb2cf3aa2b59edac1639394fbd0bb68b0a800bbd3349cb8fd91d661b19ffb8acc3e9699e598b343ed8c9ba8d837e2a3; WM_TID=1m4m51V2vNNBVUBQEUd8lSr58fiz%2BX0M; JSESSIONID-WYYY=KKAMcROJV%2FY9PpfqyU4oNP33SH2AQDHU3Cjgn5wgrv%5CbehnXf3YMmcFkbYATH4f%2FVU%2FA4l2JxKCu13pAOawgg2qvbGE4xyXXU%2Fb1mvVM8%5C0xb92%2BITQEqUe9JYB5tkPrv%2FE2d6aiAeJMHsVnk4OPKwXm1TipzGecDmwWZWaKw6XX8f04%3A1548386431316',
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    # 'Referer': 'https://music.163.com/song?id=553543014',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# https://music.163.com/weapi/v1/resource/comments/R_SO_4_553543014?csrf_token=
url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_'

comments_data1 = {
    'params': 'eqSNVubK8LzslW1GdwylSRFFs/Zvuc0PxtcLWe5PgOikTHIpHZJwmP49Z3qhF9IPjxAMnkZyXhb74aKju6ZuCOdygbuUlWjitAxQjCRRAXNyjAMgvnHV3Us2M1ZVMn7qT7PbEeOch0pqwr+upjPT/hSSR3YxfHTWwQzYANOtGGyTg7FQe3Mm8sAlidDeRU15',
    'encSecKey': '2f3ef2bbf63f9ce76959e7e7a4b9d5e86ac7de5cc5ba88af056ff67b15ceaec65339922cc5301bd0854b55e82923038fb04c172e2336489e8b5e5130cd3eb7dcd480564a678c37c839460822a090ccfdcccb1ebbe824b162eb10547ccc81011f4a907a0c28a65d3d8336a489df21b09992c62a410d6063013e2a6091b96a916a'
}
comments_data2 = {
    'params': 'jWxj5ktJucskI4xRBUf1me8+DvotwaMor5h2YKVng84U43eTrrrxz3aZ6PwYgKesNSul/nwo+uvo4UUkQkzQCS/eEtWTdE+08z9nAYBzPZHAJk1G53AG0kl0mL4rluInXU6lAZKR+UbMjDJV7XDiUr2Vc8SNl8pw9S7pTFR8QoaJ7fzS8w2oTIJM1FAOXziS',
    'encSecKey': '215124a935899e57dbb1d335728221166e82cfe059e771c8e47028442b8bbbdda96bc7ff79154aadca4a0d50fab436c3ef09d7cd06efcdb8d625cad8a3f9be95de9cda090b1979207f8f3dd2cf3d7aaab99506c28aec7151753e14c8ed59a7c71d58dc045318631dc4e71c83a4739b2a8a8656ed773399a0205f75b5ac4f2308'
}
'''
IN:
music_id 歌曲id
OUT:
comment_infos=[{'comment_id': 1089239895, 'user_id': 302637341, 'user_nickname': '咩--咩--', 'liked_count': 101477, 'content': '少年爱哀乐过于人','is_hot':True},
         {'comment_id': 1366400459, 'user_id': 298404462, 'user_nickname': '一枕黄粱一场梦', 'liked_count': 2, 'content': '我经常这样…多抱抱自己', 'is_hot': False}
'''


def main_spider(music_id='553543014'):
    header['Referer'] = 'https://music.163.com/song?id=' + music_id
    # request = urllib.request.Request(url + music_id + '?csrf_token=', data=data, headers=header)
    # response = urllib.request.urlopen(request)
    # print(response.read().decode('utf-8'))
    comment_infos = []
    r = requests.post(url=url + music_id + '?csrf_token=', data=comments_data1, headers=header)
    if r.text is None:
        return comment_infos
    comments_obj = json.loads(r.text)

    for comment_obj in comments_obj['hotComments']:
        hot_commentd = {}
        hot_comment = []
        hot_commentd['comment_id'] = comment_obj['commentId']
        hot_commentd['user_id'] = comment_obj['user']['userId']
        hot_commentd['user_nickname'] = comment_obj['user']['nickname']
        hot_commentd['liked_count'] = str(comment_obj['likedCount'])
        hot_commentd['content'] = comment_obj['content']
        hot_commentd['is_hot'] = 'True'
        hot_comment.append(str(comment_obj['commentId']))
        hot_comment.append(str(comment_obj['user']['userId']))
        hot_comment.append(comment_obj['user']['nickname'])
        hot_comment.append(str(comment_obj['likedCount']))
        hot_comment.append(comment_obj['content'].replace('💗', ''))
        hot_comment.append('True')
        hot_comment.append(music_id)
        comment_infos.append(hot_comment)

    for comment_obj in comments_obj['comments']:
        recent_commentd = {}
        recent_comment = []
        recent_commentd['comment_id'] = comment_obj['commentId']
        recent_commentd['user_id'] = comment_obj['user']['userId']
        recent_commentd['user_nickname'] = comment_obj['user']['nickname']
        recent_commentd['liked_count'] = comment_obj['likedCount']
        recent_commentd['content'] = comment_obj['content']
        recent_commentd['is_hot'] = 'False'
        recent_comment.append(str(comment_obj['commentId']))
        recent_comment.append(str(comment_obj['user']['userId']))
        recent_comment.append(comment_obj['user']['nickname'])
        recent_comment.append(str(comment_obj['likedCount']))
        recent_comment.append(comment_obj['content'].replace('💗', ''))
        recent_comment.append('False')
        recent_comment.append(music_id)
        comment_infos.append(recent_comment)

    return comment_infos

#print(main_spider('574921549'))

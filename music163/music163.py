from chapter2 import artists, albums, musics, comments, mysql
import datetime

u_ids_dict = {'华语': ['华语男歌手', '华语女歌手', '华语组合/乐队'], '欧美': ['欧美男歌手', '欧美女歌手', '欧美组合/乐队'],
              '日本': ['日本男歌手', '日本女歌手', '日本组合/乐队'], '韩国': ['韩国男歌手', '韩国女歌手', '韩国组合/乐队'],
              '其他': ['其他男歌手', '其他女歌手', '其他组合/乐队']}
u_initials_dict = ['热门', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z', '其他']
ids = ['1001', '1002', '1003', '2001', '2002', '2003', '6001', '6002', '6003', '7001', '7002', '7003', '4001', '4002',
       '4003']
initials = ['-1', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81',
            '82', '83', '84',
            '85', '86', '87', '88', '89', '90', '0']


def query_all_artists():
    v_artist_infos = []
    for id in ids:
        for initial in initials:
            t = artists.main_spider(id, initial)
            print(t)
            v_artist_infos += t
            mysql.insert_record('artist_infos', t, 'many')
    # print(v_artist_infos)
    return v_artist_infos


def query_all_albums(v_artist_infos):
    v_album_infos = []
    for v_artist_info in v_artist_infos:
        t = albums.main_spider(v_artist_info[0])
        if t is None or t == []:
            continue
        print(t)
        v_album_infos += t
        mysql.insert_record('album_infos', t, 'many')
    # print(v_album_infos)
    return v_album_infos


def query_all_musics(v_album_infos):
    v_music_infos = []
    for v_album_info in v_album_infos:
        t = musics.main_spider(v_album_info[0])
        if t is None or t == []:
            continue
        print(t)
        v_music_infos += t
        mysql.insert_record('music_infos', t, 'many')
    # print(v_music_infos)
    return v_music_infos


def query_all_comments(v_music_infos):
    v_comment_infos = []
    for v_music_info in v_music_infos:
        t = comments.main_spider(v_music_info[0])
        if t is None or t == []:
            continue
        print(t)
        v_comment_infos += t
        mysql.insert_record('comment_infos', t, 'many')
    # print(v_comment_infos)
    return v_comment_infos


if __name__ == '__main__':
    print('>>重新创建表 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    mysql.drop_tables('all')
    mysql.create_tables('all')

    print('>>查询所有歌手信息 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    artist_infos = query_all_artists()

    print('>>查询所有专辑信息 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    album_infos = query_all_albums(artist_infos)

    print('>>查询所有歌曲信息 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    music_infos = query_all_musics(album_infos)

    print('>>查询所有评论信息 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
    comment_infos = query_all_comments(music_infos)

    mysql.close()
    print('>>处理结束 ' + datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

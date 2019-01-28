# pythonSpider（![](https://img.shields.io/badge/Python-3.6.7-blue.svg)）
note on spider learning project

# /[doubanmovie](doubanmovie):
## （/[doubanMovieSpider.py](doubanmovie/doubanMovieSpider.py)）
1. movie_tag_dict() 存入爬虫字典-标签
2. do_spider() 爬虫处理方法
3. main_spider() 根据标签进行抓取数据
4. movie_spider() 根据电影的id获取电影详细信息
5. save_as_Excel() 保存结果到excel

# /[music163](music163):
1. /[music163.py](music163/music163.py)入口文件
2. /[artists.py](music163/artists.py)根据根据歌曲分类、歌手分类 查询所有歌手信息-artist_id
3. /[albums.py](music163/albums.py)根据歌手id查询专辑信息-album_id
4. /[musics.py](music163/musics.py)根据专辑中的专辑id查询歌曲信息-music_id
5. /[comments.py](music163/comments.py)根据歌曲id查询评论信息
6. /[mysql.py](music163/mysql.py) 用户pymysql（pip install pymysql）连接数据库

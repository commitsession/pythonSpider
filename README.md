# pythonSpider（![](https://img.shields.io/badge/Python-3.6.7-blue.svg)）
note on spider learning project

# 一、/[doubanmovie](doubanmovie):爬取豆瓣上电影相关信息
## （/[doubanMovieSpider.py](doubanmovie/doubanMovieSpider.py)）
1. movie_tag_dict() 存入爬虫字典-标签
2. do_spider() 爬虫处理方法
3. main_spider() 根据标签进行抓取数据
4. movie_spider() 根据电影的id获取电影详细信息
5. save_as_Excel() 保存结果到excel

# 二、/[music163](music163):爬取网易云音乐相关信息
1. /[music163.py](music163/music163.py)入口文件 一个目录下的一个分类爬取大约需要1hour 整个大约需要15*28hour
2. /[artists.py](music163/artists.py)根据根据歌曲分类、歌手分类 查询所有歌手信息-artist_id
3. /[albums.py](music163/albums.py)根据歌手id查询专辑信息-album_id
4. /[musics.py](music163/musics.py)根据专辑中的专辑id查询歌曲信息-music_id
5. /[comments.py](music163/comments.py)根据歌曲id查询评论信息
6. /[mysql.py](music163/mysql.py) 用户pymysql（pip install pymysql）连接数据库

# 三、/[chunsheng](chunsheng):智能日程提醒和聊天工具
程序的主要思想来自网友的开源项目：shengqiangzhang/examples-of-web-crawlers/4.每天不同时间段通过微信发消息提醒女友/
然后经过改造，在早安提醒中加入天气、当前周几、早安问候，排班信息（她的上班周期为四天）等内容；设置特定时间智能聊天机器人（主要使用的是图灵免费机器人）
使用方法：安装依赖包，Windows下当前目录运行[chunsheng.exe](chunsheng/chunsheng.exe)，微信扫码登录即可。
也可以在当前目录使用 pyinstaller -F chunsheng.py 打包此程序

## （/[chunsheng.py](chunsheng/chunsheng.py)）
1. get_message() 获取每日励志精句英文
2. get_week_day(date) 获取当前是周几
3. get_weather(py_name="china") 获取当前城市的天气默认是上海
4. remind_schedule(now_week, scheduling_message) 周几提醒 now_week 排班提醒 scheduling_message 天气提醒 get_weather() 早安问候语 choice(str_list_good_jitang)
5. holiday_greetings(now_time) 节日问候语
6. time_reminder(now_time, now_week, scheduling_message) 每日早中晚睡前随机提醒语
7. scheduling_reminder(delta_time) 设置上班开始日期 如：2019-5-19，则2019-5-20为白班，2019-5-21为夜班，2019-5-22、2019-5-23为休息日，四天一个轮回，设置为2099时取消设置
8. start_care() 线程调用的主程序
9. print_others(msg) 设置每天0点到6点智能聊天机器人

## （/[weatherapi.py](chunsheng/weatherapi.py)）
1. get_content(py_name="china") 获取中国所有省份的天气数据 xml
2. get_data(xml_data, flag=True) 获取中国所有省份及市区的天气数据

## （/[remind_sentence](chunsheng/remind_sentence)）
里面都是一些问候语

## （/[config.ini](chunsheng/config.ini)）
程序的主要配置

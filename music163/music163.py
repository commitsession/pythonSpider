from chapter2 import artists, albums, musics, comments, mysql

#mysql.drop_tables('artist_infos')
#mysql.create_tables('artists')
print(artists.main_spider())
#mysql.insert_record('artist_infos', artists.main_spider(), 'many')
print(mysql.query_record('comment_infos'))
mysql.close()

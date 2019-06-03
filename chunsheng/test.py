# coding: utf-8
import re,datetime,time

msg = '乏善可陈 : 春生我未生 (Text)'

if int(msg.find('春生')) != -1:
    msg= msg[0:msg.find('春生') - 1] + msg[msg.find('春生') + 2:]
    print(msg)
    with open("./current_messages.txt", "a", encoding='UTF-8') as f:
        str_msg = f.write(msg+'\n')

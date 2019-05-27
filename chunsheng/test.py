# coding: utf-8
import re,datetime,time

msg = '乏善可陈 : 春我未生 (Text)'
t0 = int(datetime.datetime.fromtimestamp(time.time()).strftime('%H'))
t1 = int(datetime.datetime.strptime('00', '%H').hour)
t2 = int(datetime.datetime.strptime('06', '%H').hour)

if int(msg.find('春生')) != -1:
    msg= msg[0:msg.find('春生') - 1] + msg[msg.find('春生') + 2:]
    print(msg)
elif ((t0 - t1) >= 0) & ((t0 - t2) <= 0):
    print(t0)
else:
    print(t0)
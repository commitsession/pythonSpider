# coding: utf-8
import socket
from bs4 import BeautifulSoup
import requests, random, time, http


def get_content(py_name="china"):
    url = 'http://flash.weather.com.cn/wmaps/xml/' + py_name + '.xml'
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            req.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))
        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    return req.text


def get_data(xml_data, flag=True):
    bs = BeautifulSoup(xml_data, "xml")
    citys = bs.find_all("city")
    big_weather = {}
    for city in citys:
        small_weather = {}
        if flag:
            small_weather['quName'] = city['quName']
            small_weather['pyName'] = city['pyName']
            small_weather['cityname'] = city['cityname']
            small_weather['state1'] = city['state1']
            small_weather['state2'] = city['state2']
            small_weather['stateDetailed'] = city['stateDetailed']
            small_weather['tem1'] = city['tem1']
            small_weather['tem2'] = city['tem2']
            small_weather['windState'] = city['windState']
        else:
            small_weather['cityname'] = city['cityname']
            small_weather['centername'] = city['centername']
            small_weather['pyName'] = city['pyName']
            small_weather['state1'] = city['state1']
            small_weather['state2'] = city['state2']
            small_weather['stateDetailed'] = city['stateDetailed']
            small_weather['tem1'] = city['tem1']
            small_weather['tem2'] = city['tem2']
            small_weather['temNow'] = city['temNow']
            small_weather['windState'] = city['windState']
            small_weather['windDir'] = city['windDir']
            small_weather['windPower'] = city['windPower']
            small_weather['humidity'] = city['humidity']
            small_weather['time'] = city['time']
            small_weather['url'] = city['url']

        big_weather[city['cityname']] = small_weather
    return big_weather


if __name__ == "__main__":
    xml_province = get_content(py_name="china")
    city_weather = get_data(xml_province, flag=True)
    print('上海今天'+city_weather['上海']['stateDetailed']+'，'+city_weather['上海']['windState']+'，最高温度'+city_weather['上海']['tem1']+'度、最低温度'+city_weather['上海']['tem2']+'度。')

    xml_city = get_content(py_name="shanghai")
    city_weather = get_data(xml_city, flag=False)
    # city_weather['市中心']['windState']
    print(city_weather)
    # 上海今天city_weather['上海']['stateDetailed']，city_weather['上海']['windState']，
    # 最高温度city_weather['上海']['tem1']度、最低温度city_weather['上海']['tem2']度。

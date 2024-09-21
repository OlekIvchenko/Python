# from time import sleep
# import time
# t1 = time.time()
# print(t1)
# time.sleep(5)
# t2 = time.time()
# print(t2)

# from datetime import datetime, timedelta
# print(datetime.now())
# print(datetime(2024, 9, 17, 19, 30, 36, 182005))
# print((datetime.now() - datetime(1970, 1,1)).days / 365)
# print(timedelta(days=19000, seconds=33, microseconds=973921))
# print(datetime.now() - timedelta(days=7))
# print(datetime.now().strftime('%d/%m/%Y'))
# print(datetime.now().strftime('%d/%m/%y %H:%M %A'))
# print(datetime.now().strptime('17/12/2003', '%d/%m/%Y'))

# import time
# import sys
# from datetime import datetime
# sys.set_int_max_str_digits(100000)
# def step_2(n):
#     return 2**n
#
# t1 = time.time()
# dt1 = datetime.now()
# print(step_2(100000))
# t2 = time.time()
# dt2 = datetime.now()
# print(t2 - t1)
# print((dt2 - dt1).microseconds)

# d = {'one': [1, 2, 3], "two" : {2,2,4}, 3 : "three"}
# d1 = dict(one = 1)
# print(d)
# print(d.get('one'))
# print(d['one'])
# print(d[3])
# print(d1)

# data_base = {
#     'FIO': ['FIO1', 'FIO2'],
#     'AVG': [95, 85]
# }
#
# data_base_csv = [
#     ['FIO1', 'FIO2'],
#     [95, 85]
# ]

# dict1 = {"coord":{"lon":30.5167,"lat":50.4333},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations","main":{"temp":294.26,"feels_like":293.71,"temp_min":294.11,"temp_max":295.74,"pressure":1024,"humidity":49,"sea_level":1024,"grnd_level":1008},"visibility":10000,"wind":{"speed":0.45,"deg":304,"gust":0.45},"clouds":{"all":79},"dt":1726593936,"sys":{"type":2,"id":2003742,"country":"UA","sunrise":1726544217,"sunset":1726589278},"timezone":10800,"id":703448,"name":"Kyiv","cod":200}
# print(dict1.get('coord').get('lon'))
# print(dict1.get('weather')[0].get('description'))

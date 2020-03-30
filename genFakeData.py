from faker import Faker
import numpy as np
from province_city import province_city
import random
import datetime
import hashlib
from multiprocessing import Process

file_dir = "fakeData/"
user_num = 10000
# user_id_domain_map是一个user有的domain数量
user_id_domain_map = 20
platforms = ["pc", "mobile", "sdk", "weixin", "weibo", "toutiao"]
separtor = '|'


def generate_fakedata_file(start_number, end_number, fakedata_file_path, user_number):

    fh = open(fakedata_file_path, 'a')
    for i in range(start_number, end_number):
        primary_id = i
        # user_id是一个lambda=user_number/2的柏松分布随机数
        user_id = str(np.random.poisson(lam=user_number // 2))
        f = Faker('zh_CN')
        uri_path = f.uri_path(deep=None)
        date = f.date_time_between(start_date=datetime.datetime(2018, 1, 1, 0, 0, 0),
                                   end_date=datetime.datetime(2019, 1, 1, 0, 0, 0), tzinfo=None)
        # hour是2018-01-01 00:00:00至2019-01-01 00:00:00中的随机整小时数。
        hour = str(date)[0:-5]+"00:00"
        # domain 的组成为www.domain{user_id}[1-20].com，从[1-20]中随机取一个
        domain = "www.domain"+user_id+str(random.randint(1, user_id_domain_map))+".com"
        # 对domain进行md5哈希
        hl_hash = hashlib.md5()
        hl_hash.update(domain.encode(encoding='utf-8'))
        domain_hash = hl_hash.hexdigest()
        platform = random.choice(platforms)
        country = "中国"
        # 随机生成省份
        province_random_index = random.randint(0, 33)
        province_dict = province_city[province_random_index]
        province = list(province_dict.keys())[0]
        # 随机生成城市
        city_list = list(province_dict.values())[0]
        city = random.choice(city_list)
        cloumn_1 = random.randint(1, 1000)
        cloumn_2 = random.randint(1, 10000)
        cloumn_3 = random.randint(1, 10000)
        cloumn_4 = random.randint(1, 100)
        cloumn_5 = random.randint(1, 100000)
        cloumn_6 = random.randint(1, 1000)
        cloumn_7 = random.randint(1, 100000)
        cloumn_8 = random.randint(1, 1000000)
        cloumn_9 = random.randint(1, 100000)
        cloumn_10 = random.randint(1, 1000)

        created_at = f.date_time_between(start_date=datetime.datetime(2018, 1, 1, 0, 0, 0),
                                         end_date=datetime.datetime(2019, 1, 1, 0, 0, 0), tzinfo=None)
        updated_at = f.date_time_between(start_date=datetime.datetime(2018, 1, 1, 0, 0, 0),
                                         end_date=datetime.datetime(2019, 1, 1, 0, 0, 0), tzinfo=None)
        row_list = [primary_id, user_id, hour, domain_hash, platform,
                    country, province, city, domain, uri_path,
                    cloumn_1, cloumn_2, cloumn_3, cloumn_4, cloumn_5, cloumn_6, cloumn_7,
                    cloumn_8, cloumn_9, cloumn_10, created_at, updated_at]
        row = separtor.join([str(j) for j in row_list])
        fh.write(row)
        fh.write('\n')
    fh.close()
    print("Generation finished")


if __name__ == "__main__":

    process_num = 70
    rows_per_file = 1000000
    row_start_id = 1
    file_seq_start = 1

    for k in range(0, process_num):
        file_path = file_dir+"fakedata"+str(k+file_seq_start)+".csv"
        start_number_per_file = k*rows_per_file+row_start_id
        end_number_per_file = (k+1)*rows_per_file+row_start_id
        p = Process(target=generate_fakedata_file,
                    args=(start_number_per_file, end_number_per_file,
                          file_path, user_num))
        p.start()

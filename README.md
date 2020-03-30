# Readme

genFakeData.py为核心代码脚本，用于生成模拟数据文件。

province_city.py保存了中国34个省份和对应城市的数据。
genFakeData.py脚本中使用了以下 Python 包：


```
from faker import Faker
import numpy as np
from province_city import province_city
import random
import datetime
import hashlib
from multiprocessing import Process
```

其中 faker 和 numpy 需要额外安装。
[Faker](https://github.com/joke2k/faker)是一个可以让你生成模拟数据的 Python 包。使用方法可以参见 Faker 的[文档](https://faker.readthedocs.io).


```
f = Faker('zh_CN')
uri_path = f.uri_path(deep=None)
date = f.date_time_between(start_date=datetime.datetime(2018, 1, 1, 0, 0, 0),
end_date=datetime.datetime(2019, 1, 1, 0, 0, 0), tzinfo=None)
```

[numpy](https://github.com/numpy/numpy) 支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。我们使用numpy来生成柏松分布随机数。


```
user_id = str(np.random.poisson(lam=user_number // 2))
```

另外我们使用 random 包来生成随机数和从列表中进行随机选择。


```
city = random.choice(city_list)
cloumn_1 = random.randint(1, 1000)
```

脚本核心函数 **generate_fakedata_file **，生成一个 csv 文件，文件中的每一行是以 | 作为分隔符的数据，如下图中的两行数据。


```
1|5047|2018-10-11 10:00:00|831434149d5331728f375128f72037f3|mobile|中国|新疆维吾尔自治区|乌鲁木齐市|www.domain504710.com|blog|935|7978|2850|42|69006|379|78194|151075|93950|729|2018-02-10 14:55:32|2018-01-13 05:28:282|5022|2018-05-08 17:00:00|f139787cc74a93b6b415e7df4caabe93|sdk|中国|上海市|上海市|www.domain50224.com|list|437|7386|3512|24|48836|980|98419|933130|13144|237|2018-06-23 18:49:27|2018-11-28 06:16:49`
```

__main__ 函数使用 multiprocessing，启动 N 个 Process 进程运行 generate_fakedata_file 函数，同时生成 N 个文件。


```
p = Process(target=generate_fakedata_file,
args=(start_number_per_file, end_number_per_file,
file_path, user_num))
p.start()
```



import os

# 获取项目根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# 设置测试环境的URL
BASE_URL = "http://ihrm-test.itheima.net"

# 设置headers_data
headers_data = {
    # "Authorization": "Bearer 22d8d9d9-e4cf-41aa-83fd-1aa31cdeea50"
}

# 导包
import unittest
from api.login import LoginAPI
import app


# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self) -> None:
        self.login_api = LoginAPI()

    # 后置处理
    def tearDown(self) -> None:
        pass

    # 登录成功
    def test_login(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"})
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 提取token
        app.headers_data["Authorization"] = "Bearer " + response.json().get("data")
        print(app.headers_data["Authorization"])

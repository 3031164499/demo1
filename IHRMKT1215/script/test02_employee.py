# 导包
import unittest
from api.employee import EmployeeAPI
from lib.dbutil import DBUtil


# 创建测试类
class TestEmployee(unittest.TestCase):
    # 员工ID
    employee_id = None

    # 前置处理
    def setUp(self) -> None:
        self.employee_api = EmployeeAPI()

    # 后置处理
    def tearDown(self) -> None:
        pass

    # 添加员工
    def test01_insert_employee(self):
        # 添加员工
        insert_data = {
            "username": "jack121606",
            "mobile": "13212121606",
            "timeOfEntry": "2020-07-09",
            "formOfEmployment": 1,
            "workNumber": "10086121606",
            "departmentName": "销售",
            "departmentId": "1266699057968001024",
            "correctionTime": "2020-07-30T16:00:00.000Z"
        }
        response = self.employee_api.insert_employee(insert_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

        # 保存员工ID
        TestEmployee.employee_id = response.json().get("data").get("id")

    # 查询员工
    def test02_select_employee(self):
        response = self.employee_api.select_employee(TestEmployee.employee_id)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 修改员工
    def test03_update_employee(self):
        response = self.employee_api.update_employee(TestEmployee.employee_id, {"username":"rose0709"})
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 删除员工
    def test04_delete_employee(self):
        response = self.employee_api.delete_employee(TestEmployee.employee_id)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

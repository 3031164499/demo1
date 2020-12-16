# 导包
import requests
import app


# 创建接口类
class EmployeeAPI:
    # 初始化
    def __init__(self):
        self.url_insert = app.BASE_URL + "/api/sys/user"
        self.url_other = app.BASE_URL + "/api/sys/user/{}"

    # 添加员工
    def insert_employee(self, insert_data):
        return requests.post(url=self.url_insert, json=insert_data, headers=app.headers_data)

    # 查询员工
    def select_employee(self, employee_id):
        url = self.url_other.format(employee_id)
        return requests.get(url=url, headers=app.headers_data)

    # 修改员工
    def update_employee(self, employee_id, update_data):
        url = self.url_other.format(employee_id)
        return requests.put(url=url, json=update_data, headers=app.headers_data)

    # 删除员工
    def delete_employee(self, employee_id):
        url = self.url_other.format(employee_id)
        return requests.delete(url=url, headers=app.headers_data)

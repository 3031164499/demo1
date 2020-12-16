import pymysql


class DBUtil:
    # 初始化
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="localhost",
                                         port=3306,
                                         user="root",
                                         password="root",
                                         database="books")
        return cls.__conn

    # 创建游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_conn().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exe_sql(cls, sql):
        try:
            cursor = cls.__get_cursor()
            cursor.execute(sql)
            if sql.split()[0].lower() == "select":
                return cursor.fetchall()
            else:
                cls.__conn.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            cls.__conn.rollback()
        finally:
            cls.__close_cursor()
            cls.__close_conn()

    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn:
            cls.__conn.close()
            cls.__conn = None

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 4:51 下午
# @Author  : JiangYanQun
# @File    : sql_utils.py


import pymysql

from utils.util import get_config, config_path


class Cur_db(object):
    def __init__(self, db_name):
        self.config = get_config(config_path)
        self.db_name = db_name

    def pymysql_cur(self, reback=5):
        """
        连接数据库
        """
        try:
            self.conn = pymysql.connect(host=self.config['mysql']['HOST'], user=self.config['mysql']['USER'],
                                        password=self.config['mysql']['PWD'], db=self.db_name,
                                        port=int(self.config['mysql']['PORT']),
                                        charset='utf8')
        except Exception as e:
            if reback == 0:
                print(str(e))
                return
            else:
                print(str(e))
                reback -= 1
                return self.pymysql_cur(reback)

    def select(self, sql, reback=2):
        """
        使用sql语句进行查询
        """
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            res = cur.fetchone()
            cur.close()
            if res:
                return res[0]
            return
        except Exception as e:
            print(str(e))
            if reback > 0:
                reback -= 1
                return self.select(sql, reback)
            else:
                print('*' * 100)
                return

    def select_many(self, sql, reback=2):
        """
        多个查询
        """
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            cur.close()
            if res:
                return res
            print(sql)
            return
        except Exception as e:
            print(str(e))
            if reback > 0:
                reback -= 1
                return self.select_many(sql, reback)
            else:
                print('*' * 100)
                return

    def insert(self, sql, params):
        """
        数据插入操作
        """
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return

    def _insert(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def update(self, sql, params):
        """
        数据修改更新操作
        """
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return

    def _update(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(str(e))

    def close(self):
        """
        关闭数据库连接
        """
        self.conn.close()
        pass


if __name__ == '__main__':
    db_name = 'hh'
    Cur_db = Cur_db(db_name)
    print(Cur_db.config['mysql']['HOST'])

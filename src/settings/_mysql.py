# -*- coding: utf-8 -*-
import MySQLdb
import DBUtils.PooledDB
import MySQLdb.cursors

from ._settings import SETTINGS


__author__ = 'Mohanson'

mysql_config = {
    'host': SETTINGS['mysql']['host'],
    'port': SETTINGS['mysql']['port'],
    'user': SETTINGS['mysql']['user'],
    'passwd': SETTINGS['mysql']['password'],
    'db': SETTINGS['mysql']['database']
}

pool = DBUtils.PooledDB.PooledDB(creator=MySQLdb, mincached=1, maxcached=100,
                                 use_unicode=False, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor,
                                 **mysql_config)

MYSQL_CONNECTION = lambda: pool.connection()


def fetchall(sql, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchall() if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result


def fetchone(sql, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchone() if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result


def fetchmany(sql, num, params=None):
    conn = MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        count = cursor.execute(sql, params) if params else cursor.execute(sql)
        result = cursor.fetchmany(num) if count else []
    except MySQLdb.Error as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    return result
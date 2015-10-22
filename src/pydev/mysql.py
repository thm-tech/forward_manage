# -*- coding: utf-8 -*-
import MySQLdb
import DBUtils.PooledDB
import MySQLdb.cursors

import src.pydev.config


__author__ = 'Mohanson'

core_config = src.pydev.config.read_ini('core.ini')
mysql_config = {
    'host': core_config.get('mysql', 'host'),
    'port': core_config.getint('mysql', 'port'),
    'user': core_config.get('mysql', 'user'),
    'passwd': core_config.get('mysql', 'password'),
    'db': core_config.get('mysql', 'database')
}

pool = DBUtils.PooledDB.PooledDB(creator=MySQLdb, mincached=1, maxcached=100,
                                 use_unicode=False, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor,
                                 **mysql_config)

connection = lambda: pool.connection()


def fetchall(sql, params=None):
    conn = connection()
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
    conn = connection()
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
    conn = connection()
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
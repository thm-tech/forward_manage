# -*- coding: utf-8 -*-
import datetime

import src.pydev.config
import src.pydev.logger
import src.pydev.mysql


conf = src.pydev.config.read_ini('core.ini')
logger = src.pydev.logger.create('dao')


def get_user_feedbacks(cursor, offset, limit):
    sql = 'select * from fd_t_feedback where direction = 1 ORDER BY time desc LIMIT %s OFFSET %s'
    params = (limit, offset)
    row_counts = cursor.execute(sql, params)

    return_list = []
    if row_counts:
        rows = cursor.fetchall()
        for row in rows:
            feedback_info = {
                'content': row['content'],
                'user_id': row['user_id'],
                'time': row['time'].strftime('%Y-%m-%d %H:%M:%S')
            }
            return_list.append(feedback_info)
    return return_list


def get_platform_feedbacks(cursor, user_id):
    sql = 'select * from fd_t_feedback where direction = 2 and user_id = %s ORDER BY time desc'
    params = (user_id, )
    row_counts = cursor.execute(sql, params)

    return_list = []
    if row_counts:
        rows = cursor.fetchall()
        for row in rows:
            feedback_info = {
                'content': row['content'],
                'user_id': row['user_id'],
                'time': row['time'].strftime('%Y-%m-%d %H:%M:%S')
            }
            return_list.append(feedback_info)
    return return_list


def get_platform_and_user_feedbacks(cursor, user_id):
    """ 返回平台和用户的聊天记录 """
    sql = 'select * from fd_t_feedback where user_id = %s ORDER BY time desc'
    params = (user_id, )
    row_counts = cursor.execute(sql, params)

    return_list = []
    if row_counts:
        rows = cursor.fetchall()
        for row in rows:
            feedback_info = {
                'content': row['content'],
                'user_id': row['user_id'],
                'time': row['time'].strftime('%Y-%m-%d %H:%M:%S'),
                'direction': row['direction']
            }
            return_list.append(feedback_info)
    return return_list


def insert_platform_return_feedback(cursor, user_id, content):
    sql = 'insert into fd_t_feedback (direction, user_id, content, time) values (2, %s, %s, %s)'
    params = (user_id, content, datetime.datetime.now())
    row_counts = cursor.execute(sql, params)
    return row_counts


def main(cursor):
    count = cursor.execute('select goods_id, basic_info from fd_t_goods where basic_info is not null')
    for i in cursor.fetchall():
        binfo = eval(i['basic_info'])
        if binfo:
            a = filter(lambda _: _['paramsName'] == "\xe5\xa4\x87\xe6\xb3\xa8", binfo)[0]['paramsValue']
            cursor.execute('update fd_t_goods set detail = %s', (a,))
            print(a)


if __name__ == '__main__':
    conn = src.pydev.mysql.connection()
    cursor = conn.cursor()
    main(cursor)
    cursor.close()
    conn.commit()
    conn.close()
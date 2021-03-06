# -*- coding: utf-8 -*-
import src.dao.feedback
import src.settings._mysql

from src.settings import LOGGER_ROOT


def get_user_feedbacks(offset, limit):
    conn = src.settings._mysql.MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        feedback_infos = src.dao.feedback.get_user_feedbacks(cursor, offset, limit)
        return_info = {
            'is_success': True,
            'feedback_infos': feedback_infos
        }
    except Exception as e:
        LOGGER_ROOT.exception(e)
        return_info = {
            'is_success': False,
            'des': str(e)
        }
    cursor.close()
    conn.close()
    return return_info


def get_platform_feedbacks(user_id):
    conn = src.settings._mysql.MYSQL_CONNECTION()
    cursor = conn.cursor()

    try:
        feedback_infos = src.dao.feedback.get_platform_feedbacks(cursor, user_id)
        return_info = {
            'is_success': True,
            'feedback_infos': feedback_infos
        }
    except Exception as e:
        LOGGER_ROOT.exception(e)
        return_info = {
            'is_success': False,
            'des': str(e)
        }
    cursor.close()
    conn.close()
    return return_info


def feedback_to_user(user_id, content):
    conn = src.settings._mysql.MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        rows_count = src.dao.feedback.insert_platform_return_feedback(cursor, user_id, content)
    except Exception as e:
        LOGGER_ROOT.exception(e)
        return {
            'is_success': False,
            'des': str(e)
        }
    else:
        cursor.close()
        conn.commit()
        conn.close()
        if rows_count:
            return {
                'is_success': True,
                'user_id': user_id,
                'content': content
            }
        else:
            return {
                'is_success': False
            }


def get_platform_and_user_feedbacks(user_id):
    conn = src.settings._mysql.MYSQL_CONNECTION()
    cursor = conn.cursor()
    try:
        response = src.dao.feedback.get_platform_and_user_feedbacks(cursor, user_id)
        num = len(response)
    except Exception as e:
        LOGGER_ROOT.exception(e)
        return {
            'is_success': False,
            'des': str(e)
        }
    else:
        return {
            'is_success': True,
            'feedback_infos': response,
            'total_num': num
        }
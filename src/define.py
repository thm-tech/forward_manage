# -*- coding: utf-8 -*-

from ndict import ndict

# shopaccount service status
# 1-等待审核，2-正常使用，3-欠费停用，4-审核未通过，5-服务到期（续年费)
SERVICE_STATUS = ndict()
SERVICE_STATUS.WAIT_AUDIT = 1
SERVICE_STATUS.NORMAL = 2
SERVICE_STATUS.TUITION = 3
SERVICE_STATUS.AUDIT_NOT_PASS = 4
SERVICE_STATUS.EXPIRATION_DATA = 5
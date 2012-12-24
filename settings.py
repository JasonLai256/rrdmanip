# -*- coding: utf-8 -*-


DATA_PATH = '/home/data/rrd-storage/'

STEP = 300

# data source 的相关设置
DataSource = {
    'dsName': '',
    'dsType': 'GAUGE',
    'heartbeat': 600
}

# rra 的相关设置
MAX_5M_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 1,    # 5 min, 12 * 24 * 365 ~ 1 year
    'rows': 105120
}

MAX_30M_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 6,    # 30 min, 2 * 24 * 365 ~ 1 year 
    'rows': 17520
}

MAX_2H_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 24,    # 2 hour, 12 * 365 ~ 1 year
    'rows': 4380
}

MAX_1D_3Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 288,    # 1 day, 365 * 3 ~ 3 year
    'rows': 1100
}

MAX_RRA = [MAX_5M_1Y_RRA, MAX_30M_1Y_RRA, MAX_2H_1Y_RRA, MAX_1D_3Y_RRA]
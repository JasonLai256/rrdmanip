# -*- coding: utf-8 -*-


DATA_PATH = '/home/data/rrd-storage/'

STEP = 60

# data source 的相关设置
DataSource = {
    'dsName': '',
    'dsType': 'GAUGE',
    'heartbeat': 120
}

# rra 的相关设置
MAX_1M_1M_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 1,    # 1 min, 60 * 24 * 30 ~ 1 month
    'rows': 43200
}

MAX_5M_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 5,    # 5 min, 12 * 24 * 365 ~ 1 year
    'rows': 105120
}

MAX_30M_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 30,    # 30 min, 2 * 24 * 365 ~ 1 year 
    'rows': 17520
}

MAX_2H_1Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 120,    # 2 hour, 12 * 365 ~ 1 year
    'rows': 4380
}

MAX_1D_3Y_RRA = {
    'cf': 'MAX',
    'xff': 0.5,
    'steps': 1440,    # 1 day, 365 * 3 ~ 3 year
    'rows': 1100
}


AVERAGE_1M_1M_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 1,    # 1 min, 60 * 24 * 30 ~ 1 month
    'rows': 43200
}

AVERAGE_5M_3M_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 5,    # 5 min, 12 * 24 * 92 ~ 3 month
    'rows': 26496
}

AVERAGE_5M_1Y_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 5,    # 5 min, 12 * 24 * 365 ~ 1 year
    'rows': 105120
}

AVERAGE_30M_6M_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 30,    # 30 min, 2 * 24 * 184 ~ 6 month 
    'rows': 8832
}

AVERAGE_30M_1Y_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 30,    # 30 min, 2 * 24 * 365 ~ 1 year 
    'rows': 17520
}

AVERAGE_2H_1Y_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 120,    # 2 hour, 12 * 365 ~ 1 year
    'rows': 4380
}

AVERAGE_1D_3Y_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 1440,    # 1 day, 365 * 3 ~ 3 year
    'rows': 1100
}

MAX_RRA = [MAX_5M_1Y_RRA, MAX_30M_1Y_RRA, MAX_2H_1Y_RRA, MAX_1D_3Y_RRA]
AVERAGE_RRA = [AVERAGE_5M_1Y_RRA, AVERAGE_30M_1Y_RRA, AVERAGE_2H_1Y_RRA, AVERAGE_1D_3Y_RRA]

PRECISE_MAX_RRA = [MAX_2H_1Y_RRA, MAX_1D_3Y_RRA]
PRECISE_AVERAGE_RRA = [AVERAGE_1M_1M_RRA, AVERAGE_5M_3M_RRA, AVERAGE_30M_6M_RRA, AVERAGE_2H_1Y_RRA, AVERAGE_1D_3Y_RRA]


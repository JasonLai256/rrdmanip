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
MIN_5M_1Y_RRA = {
    'cf': 'MIN',
    'xff': 0.5,
    'steps': 5,    # 5 min, 12 * 24 * 365 ~ 1 year
    'rows': 105120
}

MIN_30M_1Y_RRA = {
    'cf': 'MIN',
    'xff': 0.5,
    'steps': 30,    # 30 min, 2 * 24 * 365 ~ 1 year 
    'rows': 17520
}

MIN_2H_1Y_RRA = {
    'cf': 'MIN',
    'xff': 0.5,
    'steps': 120,    # 2 hour, 12 * 365 ~ 1 year
    'rows': 4380
}

MIN_1D_3Y_RRA = {
    'cf': 'MIN',
    'xff': 0.5,
    'steps': 1440,    # 1 day, 365 * 3 ~ 3 year
    'rows': 1100
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

AVERAGE_5M_1Y_RRA = {
    'cf': 'AVERAGE',
    'xff': 0.5,
    'steps': 5,    # 5 min, 12 * 24 * 365 ~ 1 year
    'rows': 105120
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

MIN_RRA = [MIN_5M_1Y_RRA, MIN_30M_1Y_RRA, MIN_2H_1Y_RRA, MIN_1D_3Y_RRA]
MAX_RRA = [MAX_5M_1Y_RRA, MAX_30M_1Y_RRA, MAX_2H_1Y_RRA, MAX_1D_3Y_RRA]
AVERAGE_RRA = [AVERAGE_5M_1Y_RRA, AVERAGE_30M_1Y_RRA, AVERAGE_2H_1Y_RRA, AVERAGE_1D_3Y_RRA]

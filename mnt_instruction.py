# -*- coding: utf-8 -*-

import settings
from manipRRD import RRDManip, RRDGraph
from instruction import figure_path


_rrds = {}


def register_mnt_rrd(target, dsNames, dsType='GAUGE'):
    """Register a RRDManip.

    :param target: 用于构造 rrd 文件名以及做为内部rrd对象缓存的 key
    :param dsName: 用于指定 data source 的命名
    :param dsType: 用于指定 data source 类型
    """
    global _rrds
    if (target not in _rrds) or (_rrds[target] is None):
        filepath = figure_path(target)
        roundRobinArchives = settings.PRECISE_MAX_RRA + \
                             settings.PRECISE_AVERAGE_RRA
        dataSources = []
        for dsname in dsNames:
            datasource = settings.DataSource.copy()
            datasource['dsName'] = dsname
            datasource['dsType'] = dsType
            dataSources.append(datasource)
        _rrds[target] = RRDManip(filepath, settings.STEP,
                                 dataSources, roundRobinArchives)
        _rrds[target].ensure_rrd()


def get_mnt_rrd(target):
    global _rrds
    if target not in _rrds:
        _rrds[target] = None
    return _rrds[target]

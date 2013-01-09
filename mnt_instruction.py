# -*- coding: utf-8 -*-

import settings
from manipRRD import RRDManip, RRDGraph
from instruction import figure_path


_rrds = {}
_graphs = {}


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
                                 datasource, roundRobinArchives)
        _rrds[target].ensure_rrd()


def register_mnt_graph(target, init_args, prep_args):
    """
    Register a RRDGraph.

    :param init_args: 初始化 RRDGraph 的所需参数，应该为 dict 类型
    :param prep_args: 确定设置 RRDGraph 的所需参数，应该为 dict 类型
    """
    global _graphs
    if (target not in _graphs) or (_graphs[target] is None):
        _graphs[target] = RRDGraph(**init_args)
        _graphs[target].prepare(**prep_args)


def get_mnt_rrd(target):
    global _rrds
    if target not in _rrds:
        _rrds[target] = None
    return _rrds[target]

def get_mnt_graph(target):
    global _graphs
    if target not in _graphs:
        _graphs[target] = None
    return _graphs[target]


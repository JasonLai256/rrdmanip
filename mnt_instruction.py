# -*- coding: utf-8 -*-

import settings
from manipRRD import RRDManip, RRDGraph
from instruction import figure_path


PREP_ARGS = {
    'defs': None,
    'cdefs': None,
    'vdefs': None,
    'lines': None,
    'areas': None,
    'gprints': None,
    'gcomments': None,
}

_rrds = {}
_graph_args = {}


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
    """
    获取 rrd 控制类，根据 target 缓存该对象。
    """
    global _rrds
    if target not in _rrds:
        _rrds[target] = None
    return _rrds[target]


def load_mnt_rrd(target):
    """
    类似于 get_mnt_rrd，获取 rrd 控制对象，根据 target 缓存该对象。不同的是，
    get_mnt_rrd 发现 target 不存在缓存中时，会直接返回 None，而 load_mnt_rrd
    会创建 rrd 再返回控制对象。

    :note: 使用 load_mnt_rrd 的默认前提是 target 对应的 rrd 控制对象是已经创建了。
    """
    global _rrds
    if target not in _rrds:
        _rrds[target] = RRDManip(filepath, None, None, None)
        _rrds[target].ensure_rrd()
    return _rrds[target]


def register_graph_args(target, prep_args):
    """Register the RRDGraph preparing arguments.

    :param target: 用于构造 rrd 文件名以及做为内部rrd对象缓存的 key
    :param prep_args: 确定设置 RRDGraph 的所需参数，为 dict 类型
    """
    global _graph_args
    if (target not in _graph_args) or (_graph_args[target] is None):
        _graph_args[target] = prep_args


def get_graph_args(target):
    global _graph_args
    if target not in _graph_args:
        _graph_args[target] = None
    return _graph_args[target]

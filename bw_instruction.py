# -*- coding: utf-8 -*-

import settings
from manipRRD import RRDManip

import os
import hashlib


_rrds = {}


def figure_path(domain):
    """
    通过 domain 构建出相应的路径，并在构建的过程中监测目录是否存在，若不存在则创建
    
    figure method:   a.myzaker.com -> DATAPATH/3/e5/a.myzaker.com.rrd
    """
    join = os.path.join

    md5 = hashlib.md5()
    md5.update(domain)
    hashstr = md5.hexdigest()
    parts = [settings.DATA_PATH, hashstr[0], hashstr[1:3], '%s.rrd' % domain]

    # 监测各级目录是否已经存在或需要创建
    for index in range(2, 4):
        path = os.path.join(*parts[:index])
        if not os.path.exists(path):
            os.mkdir(path)
    return os.path.join(*parts)
    

def register_rrd(domain):
    """Add a RRDManip."""
    if domain not in _rrds:
        filepath = figure_path(domain)
        roundRobinArchives = settings.MAX_RRA + settings.AVERAGE_RRA
        datasource = settings.DataSource.copy()
        # 取 domain 的右起第二段为 dsName，即 a.myzaker.com -> myzaker
        dsname = domain.rsplit('.', 2)[-2]
        datasource['dsName'] = dsname
        _rrds[domain] = RRDManip(filepath, settings.STEP,
                                 datasource, roundRobinArchives)
        _rrds[domain].ensure_rrd()


def get_bw_rrd(domain):
    if domain not in _rrds:
        register_rrd(domain)
    return _rrds[domain]

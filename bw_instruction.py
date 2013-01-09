# -*- coding: utf-8 -*-

import settings
from manipRRD import RRDManip
from instruction import figure_path


_rrds = {}


def figure_bw_dsname(domain):
    """
    取 domain 的右起第二段为 dsName，即 a.google.com -> google
    """
    return domain.rsplit('.', 2)[-2]
    

def register_rrd(domain):
    """Register a RRDManip."""
    global _rrds
    if domain not in _rrds:
        filepath = figure_path(domain)
        roundRobinArchives = settings.MAX_RRA + settings.AVERAGE_RRA
        datasource = settings.DataSource.copy()
        dsname = figure_bw_dsname(domain)
        datasource['dsName'] = dsname
        _rrds[domain] = RRDManip(filepath, settings.STEP,
                                 datasource, roundRobinArchives)
        _rrds[domain].ensure_rrd()


def get_bw_rrd(domain):
    global _rrds
    if domain not in _rrds:
        register_rrd(domain)
    return _rrds[domain]

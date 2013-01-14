# -*- coding: utf-8 -*-

"""
Project Created at 2012-12-20
"""

__version__ = 0.1
__author__ = 'jason lai'


PREP_ARGS = {
    'defs': None,
    'cdefs': None,
    'vdefs': None,
    'lines': None,
    'areas': None,
    'gprints': None,
    'gcomments': None,
}


from bw_instruction import get_bw_rrd, figure_bw_dsname
from mnt_instruction import register_mnt_rrd, get_mnt_rrd



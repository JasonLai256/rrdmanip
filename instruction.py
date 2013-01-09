# -*- coding: utf-8 -*-

import settings

import os
import hashlib


def figure_path(target):
    """
    通过 target 构建出相应的路径，并在构建的过程中监测目录是否存在，若不存在则创建
    
    figure method:   google.com -> DATAPATH/3/e5/google.com.rrd
    """
    md5 = hashlib.md5()
    md5.update(target)
    hashstr = md5.hexdigest()
    parts = [settings.DATA_PATH, hashstr[0], hashstr[1:3], '%s.rrd' % target]

    # 监测各级目录是否已经存在或需要创建
    for index in range(2, 4):
        path = os.path.join(*parts[:index])
        if not os.path.exists(path):
            os.mkdir(path)
    return os.path.join(*parts)


# -*- coding: utf-8 -*-

from pyrrd.rrd import DataSource, RRA, RRD

import time
import os


class RRDManip(object):

    def __init__(self, filename, step, dataSources, roundRobinArchives):
        """
        实例化 RRDManip 类对象。
        
        :param filename: the name of the RRD you to manipulative
        :param dataSources: 相关的 data Source 队列
        :param roundRobinArchives: 相关的 rra 队列
        """
        if not isinstance(dataSources, list):
            dataSources = [dataSources]
        if not isinstance(roundRobinArchives, list):
            roundRobinArchives = [roundRobinArchives]

        self.dataSources = dataSources
        self.roundRobinArchives = roundRobinArchives
        self.filename = filename
        self.step = step
        self.rrd = None

    def ensure_rrd(self):
        """
        Ensures that an RRD file is created.
        """
        if os.path.isfile(self.filename):
            # the rrd file alread exist
            self.rrd = RRD(self.filename)
        else:
            self.create_rrd()

    def create_rrd(self):
        """
        Creates an RRD file.
        """
        dataSources = [DataSource(**ds) for ds in self.dataSources]
        roundRobinArchives = [RRA(**rra) for rra in self.roundRobinArchives]
        now = int(time.time())
        self.rrd = RRD(self.filename, start=now, step=self.step,
                       ds=dataSources, rra=roundRobinArchives, )
        self.rrd.create()

    def update(self, timestamp, values):
        """
        Feeds data values into an RRD.
        """
        timestamp = int(timestamp)
        if not isinstance(values, list):
            values = [values]
        self.rrd.bufferValue(timestamp, *values)
        self.rrd.update()

    def fetch(self, cf='AVERAGE', resolution=None, start=None, end=None, returnStyle="ds"):
        """
        Fetch data values from an RRD.

        :param returnStyle: 指定返回的数据格式，包括有'ds' 和 'time'
        """
        return self.rrd.fetch(cf, resolution, start, end, returnStyle)

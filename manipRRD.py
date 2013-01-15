# -*- coding: utf-8 -*-

from pyrrd.rrd import DataSource, RRA, RRD
from pyrrd.graph import Graph

import time
import os


class RRDManip(object):

    def __init__(self, filename, step=None,
                 dataSources=None, roundRobinArchives=None):
        """
        实例化 RRDManip 类对象。
        
        :param filename: the name of the RRD you to manipulative
        :param dataSources: 相关的 data Source 队列
        :param roundRobinArchives: 相关的 rra 队列
        """
        if not isinstance(dataSources, list) and \
                not isinstance(dataSources, tuple):
            dataSources = [dataSources]
        if not isinstance(roundRobinArchives, list) and \
                not isinstance(roundRobinArchives, tuple):
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
        # start 时间设定为当前时间的一天前，86400 即一天内包含的秒数
        past_one_day = int(time.time()) - 86400
        self.rrd = RRD(self.filename, start=past_one_day, step=self.step,
                       ds=dataSources, rra=roundRobinArchives)
        self.rrd.create()

    def update(self, timestamp, values):
        """
        Feeds data values into an RRD.
        """
        timestamp = int(timestamp)
        if not isinstance(values, list) and not isinstance(values, tuple):
            values = [values]
        self.rrd.bufferValue(timestamp, *values)
        self.rrd.update()

    def fetch(self, cf='AVERAGE', resolution=None, start=None, end=None, returnStyle="ds"):
        """
        Fetch data values from an RRD.

        :param returnStyle: 指定返回的数据格式，包括有'ds' 和 'time'
        """
        return self.rrd.fetch(cf, resolution, start, end, returnStyle)


class RRDGraph(object):

    def __init__(self, filename, start=None, end=None, step=None, title='',
                 vertical_label='', width=600, height=180, color=None):
        self.filename = filename
        self.start = start
        self.end = end
        self.step = step
        self.height = height
        self.width = width
        self.title = title
        self.vertical_label = vertical_label
        self.color = color
        self.graph = None        

    def prepare(self, defs, cdefs, vdefs, lines, areas, gprints, gcomments):
        # check None variable
        if not defs:
            defs = []
        if not cdefs:
            cdefs = []
        if not vdefs:
            vdefs = []
        if not lines:
            lines = []
        if not areas:
            areas = []
        if not gprints:
            gprints = []
        if not gcomments:
            gcomments = []
        
        # check instance
        if not isinstance(defs, list) and \
                not isinstance(defs, tuple):
            defs = [defs]
        if not isinstance(cdefs, list) and \
                not isinstance(cdefs, tuple):
            cdefs = [cdefs]
        if not isinstance(vdefs, list) and \
                not isinstance(vdefs, tuple):
            vdefs = [vdefs]
        if not isinstance(lines, list) and \
                not isinstance(lines, tuple):
            lines = [lines]
        if not isinstance(areas, list) and \
                not isinstance(areas, tuple):
            areas = [areas]
        if not isinstance(gprints, list) and \
                not isinstance(gprints, tuple):
            gprints = [gprints]
        if not isinstance(gcomments, list) and \
                not isinstance(gcomments, tuple):
            gcomments = [gcomments]

        args = defs + cdefs + vdefs + lines + areas + gprints + gcomments
        self.graph = Graph(self.filename, start=self.start, end=self.end,
                           step=self.step, height=self.height, width=self.width,
                           title=self.title, vertical_label=self.vertical_label,
                           color=self.color)
        self.graph.data.extend(args)

    def plot(self):
        self.graph.write()

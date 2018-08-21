#!/usr/bin/python
# -*- coding: utf-8 -*-
import Conf
from FileMgr.FileMgr import CopyMove


class Compile(object):
    def __init__(self):
        self.copy = CopyMove()
        pass

    def compile(self, file_type):
        if file_type == 'lt':
            pass
        elif file_type == 'pt':
            pass
        elif file_type == 'pd':
            pass


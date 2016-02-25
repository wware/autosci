#!/usr/bin/env python

import os
import sys

from parser import Link, Parser


class Tangle(Parser):
    def __init__(self):
        self.last_chunk_name = None

    def define_chunk(self, line, name):
        self.last_chunk_name = name
        self[name] = []

    def finish_chunk(self):
        pass

    def line_in_chunk(self, line):
        self[self.last_chunk_name].append(line)

    def line_outside_chunk(self, line):
        pass

    def link_chunk(self, line, subname):
        self[self.last_chunk_name].append(Link(subname))

    def tangle(self, key):
        for line in self[key]:
            if isinstance(line, Link):
                self.tangle(line)
            else:
                print line


t = Tangle()
root = sys.argv[1]
t.read(open(sys.argv[2]))
t.tangle(root)

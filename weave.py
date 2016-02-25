#!/usr/bin/env python

import os
import re
import sys

from parser import Link, Parser


class Weave(Parser):
    def __init__(self, ext):
        self.ext = ext
        self.links = []

    def define_chunk(self, line, name):
        if self.ext == 'md':
            print "<a name=\"" + name + "\"></a>"
            print "```"
            print line
        elif self.ext == "tex":
            print "\\phantomsection\\label{" + name + "}\\vspace{5mm}\\begin{verbatim}"
            print line
        else:
            raise NotImplementedError

    def finish_chunk(self):
        if self.ext == "md":
            print "```"
            if self.links:
                s = "*Refers to: "
                for num, link in enumerate(self.links, 1):
                    comma = (num < len(self.links)) and ", " or ""
                    s += "[" + link + "](#" + link + ")" + comma
                print s + "*"
                self.links = []
        elif self.ext == "tex":
            print "\\end{verbatim}"
            if self.links:
                print "\\textit{Refers to: "
                for num, link in enumerate(self.links, 1):
                    comma = (num < len(self.links)) and "," or ""
                    print "\\hyperref[" + link + "]{" + link + "}" + comma
                print "}"
                self.links = []
            print "\\vspace{5mm}"
        else:
            raise NotImplementedError

    def line_in_chunk(self, line):
        print line

    def line_outside_chunk(self, line):
        print line

    def link_chunk(self, line, subname):
        self.links.append(subname)
        print line


fname = sys.argv[1]
ext = re.compile('.*\.([^\.]+)').match(fname).group(1)
w = Weave(ext)
w.read(open(fname))

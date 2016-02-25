#!/usr/bin/env python

import os
import pprint
from rdflib import Graph


def main():
    os.system("rm -f foo.n3; make foo.n3")
    graph = Graph()
    graph.parse("foo.n3", format="n3")
    pprint.pprint(sorted(graph))

if __name__ == '__main__':
    main()

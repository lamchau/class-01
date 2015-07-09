#!/usr/bin/env python
import os
import logging
import sys
sys.path.append("../shared/")
import utils
log = utils.create_logger(__file__)
# #log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)

import copy
import random

def min_cuts(graph, iterations):
    min_cuts = sys.maxint
    for i in xrange(iterations):
        g = copy.deepcopy(graph)
        #results = contract(g)
        # find minimum edge count
        cut = contract(g)
        if cut < min_cuts:
            min_cuts = cut
    log.debug("Minimum cuts: %d\n" % min_cuts)
    return min_cuts

def contract(graph):
    if len(graph) < 3:
        return min([len(x) for x in graph.itervalues()])
    # find random edge
    edges = []
    for v1, vertices in graph.iteritems():
        for v2 in vertices:
            # allow dupes (uniform distribution while sampling)
            # non-directional graph
            edge = (v1, v2)
            edges.append(edge)
    u, v = edges[random.randint(0, len(edges) - 1)]
    log.debug("Using random edge: (%d, %d)" % (u, v))

    # merge vertices on random edge
    graph[u] = graph.get(v) + graph.get(u)
    # remove merged
    del graph[v]

    for vertex, adjacent in graph.iteritems():
        # update with merged
        adjacent = [u if x == v else x for x in adjacent]
        # remove self loops (e.g. (2, 2))
        adjacent = [x for x in adjacent if x != vertex]
        graph[vertex] = adjacent
    return contract(graph)

def graph2str(graph):
    message = []
    for vertex, adjacent in graph.iteritems():
        message.append("%4d : %s" % (vertex, str(adjacent)))
    return "\n".join(message)

def process(path):
    graph = {}
    if not os.path.isfile(path):
        raise IOError("Invalid file: %s" % path)
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("#") or not len(line):
                continue
            line = " ".join(line.split())
            values = [int(x.strip()) for x in line.split()]
            graph.setdefault(values[0], values[1:])
    n = len(graph)
    iterations = (n * (n - 1))/2
    log_message = [
        "Calculating minimum cuts",
        "filename=%s" % os.path.basename(path),
        "graph_size=%d" % n,
        "iterations=%d" % iterations]
    log.debug("\n  ".join(log_message))
    log.debug("graph\n%s" % graph2str(graph))
    return min_cuts(graph, iterations)

if __name__== "__main__":
    print file_karger("input/kargerAdj.txt")
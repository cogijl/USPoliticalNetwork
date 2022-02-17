# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:47:08 2022

@author: jelane
"""

import json
import networkx as nx


tarfile = '2016ElectionNetwork_09May2015.json'


def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return nx.json_graph.node_link_graph(js_graph)


G = read_json_file(tarfile)

# now save output

nx.write_gexf(G, "output.gexf")

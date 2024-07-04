import requests
from app import node_registry

class Node:
    def __init__(self, name : str):
        self._edges = []
        self._name = name;
        self._input = {}
        self._output = {}
        self._expired = False

    def add_edge(self, edge : 'Edge'):
        self._edges.append(edge)

    def run(self, input):
        if(self._expired):
            raise Exception(f'Node {self._name} is already expired!')
        response = requests.post(node_registry[self._name], json=input)
        response.raise_for_status()
        self._output = response.json()
        self._expired = True;

    @property
    def edges(self):
        """The edges property."""
        return self._edges

    @property
    def input(self):
        """The input property."""
        return self._input

    @property
    def output(self):
        """The output property."""
        return self._output

###

class Edge:
    def __init__(self, start: Node, end: Node, mapping):
        self._start = start;
        self._end = end;

    def run(self):
        self._end.run(self._start._output)

###

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id : str, node: Node):
        self.nodes[id] = node;

    def get_node(self, id : str) -> Node: 
        return self.nodes[id]

    def add_edge(self, start: str, end: str, mapping):
        self.nodes[start].add_edge(self.nodes[end])

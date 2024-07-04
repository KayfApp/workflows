from flask import Flask
from action.node import ActionNode, NodeData, NodeDataInputProperty, NodeDataOutputProperty, NodeDataProperties

app = Flask(__name__)

node_registry = {}
def register_node(node : ActionNode):
    data = node.data

    if data.name in node_registry:
        return

    path = f'/action/{data.name}'
    node_registry[data.name] = path
    # Create actual route
    @app.route(path, methods=['POST'])
    def endpoint():
        from flask import request, jsonify
        req_data = request.json
        result = node.execute(req_data)
        return jsonify(result)

class ExampleNode(ActionNode):
    @property
    def data(self):
        input = NodeDataInputProperty('name', 'Name of user', 'string', 'User')
        output = NodeDataOutputProperty('text', 'Some text', 'string')

        return NodeData('Example', 'Ankush Ahuja', 'demo', 'Prints message', NodeDataProperties([input], output))

    def execute(self, data):
        data = self.transform_request_data(data)
        text = f'Hello {data['name']}'
        print(text)
        return text

register_node(ExampleNode())

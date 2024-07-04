# Nodes

A node is a callable action in a workflow and is responsible for exactly one task. There a two types of nodes:

- Action nodes: Action nodes are standalone applications and implemented as microservices. They are also callable on their own.
- Control nodes: Control nodes are sort of bridges to other nodes and influence the flow of the application. A control node is applied for every node it is called uppon. Examples are 'if' & 'barrier'

## Definition

```ts
{
  name: string;
  author: string;
  version: string;
  description: string;
  properties: {
    input: {
      name: string;
      description: string;
      value_type: string;
      default_value: type;
    }[];
    output: {
      name: string;
      description: string;
      value_type: string;
    };
  }
  execute: function(param) : output; // output referring to the output object consisting of key-value-pairs, where each output-name defined in the properties is a key
}
```

from abc import ABC, abstractmethod
from typing_extensions import Any

class NodeDataInputProperty:
    def __init__(self, name, description, value_type, default_value):
        self._name = name;
        self._description = description
        self._value_type = value_type
        self._default_value = default_value

    @property
    def name(self):
        """The name property."""
        return self._name

    @property
    def description(self):
        """The description property."""
        return self._description

    @property
    def value_type(self):
        """The value_type property."""
        return self._value_type

    @property
    def default_value(self):
        """The default_value property."""
        return self._default_value

class NodeDataOutputProperty:
    def __init__(self, name, description, value_type):
        self._name = name;
        self._description = description
        self._value_type = value_type

    @property
    def name(self):
        """The name property."""
        return self._name

    @property
    def description(self):
        """The description property."""
        return self._description

    @property
    def value_type(self):
        """The value_type property."""
        return self._value_type

###

class NodeDataProperties:
    def __init__(self, inputProperties : list[NodeDataInputProperty], outputProperties : NodeDataOutputProperty):
        self._inputProperties = inputProperties
        self._outputProperties = outputProperties

    @property
    def inputProperties(self):
        """The inputProperties property."""
        return self._inputProperties

    @property
    def outputProperties(self):
        """The outputProperties property."""
        return self._outputProperties

###

class NodeData:
    def __init__(self, name : str, author : str, version : str, description : str, properties : NodeDataProperties):
        self._name = name;
        self._author = author;
        self._version = version;
        self._description = description;
        self._properties = properties;

    @property
    def name(self):
        """The name property."""
        return self._name
    
    @property
    def author(self):
        """The author property."""
        return self._author

    @property
    def version(self):
        """The version property."""
        return self._version
    
    @property
    def description(self):
        """The description property."""
        return self._description

    @property
    def properties(self):
        """The properties property."""
        return self._properties

###
  
class ActionNode(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, data) -> Any:
        pass;

    def transform_request_data(self, data) -> Any:
        res = {}

        for prop in self.data.properties.inputProperties:
            if(prop.name in data):
                res[prop.name] = data[prop.name]
            else:
                res[prop.name] = prop.default_value

        return res

    @property
    @abstractmethod
    def data(self) -> NodeData:
        pass

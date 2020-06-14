import xmltodict
import json
from xml.etree import ElementTree
from math import ceil


def batches(data, batch_size=100):
    return [
        data[i * batch_size:(i + 1) * batch_size]
        for i in range(0, ceil(len(data) / batch_size))
    ]


def xml_element_to_json(element: ElementTree.Element):
    return json.loads(json.dumps(
        xmltodict.parse(
            ElementTree.tostring(
                element
            )
        )
    ))

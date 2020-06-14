import xmltodict
import json
from xml.etree import ElementTree


def xml_element_to_json(element: ElementTree.Element):
    return json.loads(json.dumps(
        xmltodict.parse(
            ElementTree.tostring(
                element
            )
        )
    ))

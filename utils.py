import xmltodict
import json
from xml.etree import ElementTree
from display_xml import XML


def xml_element_to_json(element: ElementTree.Element):
    return json.loads(json.dumps(
        xmltodict.parse(
            ElementTree.tostring(
                element
            )
        )
    ))


def display_xml(element):
    return XML(ElementTree.tostring(element))

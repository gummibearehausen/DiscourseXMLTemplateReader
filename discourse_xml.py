"""
Each root is a node:
<node_tag node_attrib_1 = 'value_1' node_attrib_2 = 'value_2'>node_text </node_tag>
Node.tag = node_tag
Node.text = node_text
Node.attrib = {'node_attrib_1':'value_1', 'node_attrib_2':'value_2'}
"""
import xml.etree.ElementTree as ET

# read all the tags from the file:


def read_all_nodes(roots):
    for node in roots.iter():
        print("node tag: "+node.tag)
        print("node attributes: ",node.attrib)
        print("node text: "+node.text + '\n')


def read_block_by_block(roots):
    # you will need to know the tags at a leaf level
    for parent_node in roots.iter('p'):
        print("parent node id: "+parent_node.attrib['id'])
        for child_node in parent_node.iter():
            print("child node tag: " + child_node.tag)
            print("child node attributes: ", child_node.attrib)
            print("child node text: " + child_node.text)
        print('\n'*2)

if __name__ == '__main__':
    file_name = 'discourse.xml'
    # parse the xml.file
    parsed_file = ET.parse(file_name)

    # get root nodes from XML file.
    roots = parsed_file.getroot()
    read_all_nodes(roots)

    read_block_by_block(roots)






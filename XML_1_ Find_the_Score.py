import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    return sum([len(elem.items()) for elem in tree.iter()])


if __name__ == '__main__':
    # sys.stdin.readline()
    # xml = sys.stdin.read()
    n = int(input())
    xml = ''
    for _ in range(n):
        xml += input().strip()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

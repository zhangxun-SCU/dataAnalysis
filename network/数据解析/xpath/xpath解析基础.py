from lxml import etree


if __name__ == '__main__':
    tree = etree.parse('test.html')
    title = tree.xpath('/html/head/title/text()')
    print(title)
    a = tree.xpath('//header//a/@href')
    print(a)

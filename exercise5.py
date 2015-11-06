# import lxml Element Tree
from lxml import etree as ElementTree
tree = ElementTree.parse("xml/liefde-tsa.xml")
root = tree.getroot()
# opvangen van actie:
firstPage = root.find(".//div[@type='page']")
# query firstPage met lxml
elements = firstPage.xpath("//text()")
for element in elements:
    print(element)




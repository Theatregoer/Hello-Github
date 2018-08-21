import xml.etree.ElementTree as ET


class ParseXml(object):
    def __init__(self, targetDir):
        self.targetDir = targetDir

    def parsexml(self):
        tree = ET.parse(r'D:\test\test.xml')
        root = tree.getroot()

        for child in root:
            print(child.tag, child.attrib)

for elem in tree.iter():
    print(elem.tag, elem.attrib)


updateTree = ET.parse(r'D:\test\test.xml')
root = updateTree.getroot()
newEle = ET.Element("file")
newEle.attrib = {"md5":"asdsdas","path":"123456"}
Config = root.finda('Config')
File = Config.find('Files')
File.append(newEle)
updateTree.write(r'D:\test\test.xml')
'''
print(root.tag)
for i in root:
    print(i.tag)


    def update_file_info_in_xml(xml_path, path, md5):
        if xml_path == "" or not os.path.isfile(xml_path):
            return 0

        with open(xml_path, "r", encoding="utf-8") as f:
            xml_str = f.read()

        xml_str = re.sub(u"&", u"x1x", xml_str)
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(xml_str)
        tree = ET.parse(xml_path)
        root = tree.getroot()
        need_new = 1
        files = root.findall(conf.file_node_name_in_list_file)
        for itr_dom in files:
            if path != itr_dom.get("path"):
                continue
            need_new = 0
            itr_dom.set("md5", md5)
            break
        if need_new == 1:
            new_dom = ET.Element("file")
            new_dom.attrib = {"path": path, "md5": md5}
            Files = root.find(conf.files_node_name_in_list_file)
            Files.append(new_dom)
        tree.write(xml_path)

        with open(xml_path, "r", encoding="utf-8") as f:
            xml_str = f.read()

        xml_str = re.sub(u"x1x", u"&", xml_str)
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(xml_str)
            '''
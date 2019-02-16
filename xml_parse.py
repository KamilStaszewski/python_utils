import xml.etree.ElementTree as ET
tree = ET.parse('sitemap.xml')
root = tree.getroot()

def write_xml_data_to_file():
  file_to_write_to = open('output.txt', 'a')
  for item in root.findall('url'):
    location = item.find('loc').text
    file_to_write_to.write(location + '\n')

write_xml_data_to_file()



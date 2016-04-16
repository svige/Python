from xml.dom import minidom

def prettyXml(f):
    doc = minidom.parse(f)
    xmlStr = doc.toprettyxml(indent = '',newl = '',encoding = 'utf-8')
    xmlStr = xmlStr.replace('    ', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)
    xmlStr = doc.toprettyxml(indent = '    ', newl = '\n', encoding = 'utf-8')
    
    try:
        fp = open(f,'w')
        fp.write(xmlStr)
        fp.close()
    except:
        pass
    finally:
        if not fp is None:
            fp.close()

prettyXml("test.xml")

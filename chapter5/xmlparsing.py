#
# Example file for parsing and processing XML
#
import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")

    # use the parse() function to load and parse an XML file
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # print out the document node and the name of the first child tag
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    print("-----------------")
    # get a list of XML tags from the document and print each one
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    # print out the document node and the name of the first child tag
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


    # create a new XML tag and add it into the document


if __name__ == "__main__":
    main();


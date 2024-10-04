import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
   global maxdepth
   level = level + 1
   for i in elem:
      depth(i, level)
   if(level > maxdepth):
      maxdepth = level

if __name__ == '__main__':
   # Number of lines of XML input
   n = int(input("Enter the number of lines in the XML: "))
   
   # Collecting the input lines to form an XML string
   xml = ""
   for i in range(n):
      xml += input() + "\n"
   
   # Parsing the XML string into an ElementTree
   tree = etree.ElementTree(etree.fromstring(xml))
   
   # Calculate the depth, starting at level -1 to account for the root being level 0
   depth(tree.getroot(), -1)
   
   # Output the maximum depth
   print("Max depth:", maxdepth)

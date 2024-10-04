from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
   def handle_starttag(self, tag, attrs):
      print (tag)
      for attr in attrs:
         print(f'-> {attr[0]} > {attr[1]}')


   # def handle_endtag(self, tag):
   #    print (tag)

   def handle_startendtag(self, tag, attrs):
      print (tag)

   def handle_startendtag(self,tag,attrs):
      print(f'{tag}')
      for attr in attrs:
         print(f'-> {attr[0]} > {attr[1]}')


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

html_l = []

for _ in range(int(input(""))):
   html_l.append(input())

html = "".join(html_l)

parser.feed(html)
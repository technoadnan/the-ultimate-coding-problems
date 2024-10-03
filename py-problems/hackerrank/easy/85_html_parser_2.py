from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
   def handle_comment(self, data: str) -> None:
      if '\n' in data:
            print(">>> Multi-line Comment")
      else:
         print(">>> Single-line Comment")
      print(data)
   
   def handle_data(self, data: str) -> None:
      if data != "\n":
         print(f">>> Data")
         print(f"{data}")
  
html = ""       
for i in range(int(input())):
   html += input().rstrip()
   html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
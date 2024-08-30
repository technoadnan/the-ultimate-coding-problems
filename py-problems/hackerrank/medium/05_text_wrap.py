import textwrap

def wrap(string, max_width):
   upt_str = ""
   for j in textwrap.wrap(string,max_width):
      upt_str += j + "\n"
   return upt_str
   # return textwrap.wrap(string,max_width)

if __name__ == '__main__':
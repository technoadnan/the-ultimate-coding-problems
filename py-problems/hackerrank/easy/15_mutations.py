def mutate_string(string, position, character):
   l_str = list(string)
   l_str[position] = character
   a = ''.join(l_str)
   return a


if __name__ == '__main__':
   s = input()
   i, c = input().split()
   s_new = mutate_string(s, int(i), c)
   print(s_new) 
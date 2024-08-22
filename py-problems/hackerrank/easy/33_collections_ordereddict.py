from collections import OrderedDict

items = int(input(""))
ordered_dict = OrderedDict()
for _ in range(items):
   item = [item for item in input("").split(" ")]
   item_name = " ".join(item[:-1])
   net_price = int("".join(item[len(item)-1:]))
   if item_name in ordered_dict:
      ordered_dict[item_name] += (net_price)
   else:
      ordered_dict[item_name] = net_price

for k,v in ordered_dict.items():
   print(f"{k} {v}")

num_of_shoe = int(input(""))

l = [int(x) for x in input("").split()]
print(l)

num_of_customer = int(input(""))

profit = 0
for i in range(num_of_customer):
   customer_shoe_size,price = map(int, input("").split())
   if customer_shoe_size in l:
      l.remove(customer_shoe_size) # once it bought it can't be sell again
      profit += price

print(profit)
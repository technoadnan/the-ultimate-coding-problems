design_pattern = input("").split()
first_num = int(design_pattern[0])
second_num = int(design_pattern[1])

sym1 = "-"
sym2 = ".|."

# Initialize k to 1 to handle the increasing number of .|. symbols
k = 1

for a in range(1, first_num + 1):  # Loop for the number of rows
   num_dashes = (second_num - k * len(sym2)) // 2  # Calculate the number of dashes on each side
   if num_dashes < 3:
      break
   print(sym1 * num_dashes + sym2 * k + sym1 * num_dashes)  # Print the pattern
   k += 2  # Increment the number of .|. symbols by 2

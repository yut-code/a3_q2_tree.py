# Teresa Yu
# Dec 7 2020
# a3_q2_tree.py
# This program prints a christmas tree pattern with asterisks

rowCounter = 2
valueCounter = 1

for i in range(3):
  for j in range(rowCounter):
    print(("*"*valueCounter).center(20))
    valueCounter += 2
  rowCounter += 1
  valueCounter = 1
print("\n") 

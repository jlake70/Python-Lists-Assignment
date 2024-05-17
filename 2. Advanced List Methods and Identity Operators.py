#Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both_lists = [x for x in attended if x in submitted]


print(both_lists)
#Can you suggests another way to do this

#Task 2

if  len(submitted) ==   len(attended):
    print("The lists are similar.")
else:
    print("These lists are not similar.")

#Task 3

attended.remove("Eve")
attended.remove("Frank")
print(attended)
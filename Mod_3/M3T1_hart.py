def selection_sort(numbers):
   # A variable to hold the number of item comparisons
   comparisons = 0

   for i in range(len(numbers)-1):
          
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
      
         comparisons = comparisons + 1
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
      
      # Swap numbers[i] and numbers[index_smallest]
      # temp = numbers[i]
      # numbers[i] = numbers[index_smallest]
      # numbers[index_smallest] = temp
      numbers[i], numbers[index_smallest] = numbers[index_smallest], numbers[i]
   return comparisons


# Main program to test the selection sort algorithm
counter = 0
numbers = []
print('please enter your numbers for the list')
while counter < 8:
  user_input = int(input())
  numbers.append(user_input)
  counter += 1

# Display the contents of the list
print('UNSORTED:', numbers)

# Call the selection_sort() function
comparisons = selection_sort(numbers)

# Display the (sorted) contents of the list
print('SORTED:', numbers)

print('Total comparisons: %d' % comparisons)
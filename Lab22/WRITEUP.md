Solution A:
Counter creates a list of the characters and how many times they appear. Counts is now a list. Index is the list of all the characters and how many there are. Top creates a heap queue that sorts them by largest first, and uses K to tell how big it is. Return statement returns the item and its count from the top list.

Solution B:
Counter creates the list, counts is now a list. Entries is a list of the variables and how many of them there are. Entries.sort sorts the list in high to low. The return statement returns the item and the count for K entries.

Solution C:
Seen_order is a list of the order they have been seen at. Seen is used to not add duplicates to seen_order. The next for loop, loops through the seen order and goes through the original items list and counts how many times that unique item is there, the pairs list is made which has the item and how many times it's been counted together. Pairs.sort, sorts pairs and the return statement returns up to K items in pairs.

Prediction 1:
I think solution C breaks first as the input size grows. This happens because in the second for loop it loops through the list for how many unique answers there are, which can be N answers, so it would be O(N^2)

Prediction 2:
I would trust solution A the most because it uses a heap queue that is reliable and fast to look through. It also doesnt sort the list which is o(N^2), yet creating the heap is O(N) and getting data from it is O(LogN)

Part 2:
Solution A
    Good: I liked solution a because it was easy to read with very few lines. I also liked how in line 26 it used a heap to create the list.

    Bad: I dont like line 27 the return line. I dont get why it didnt just return the heap it created because its size is K and has the top results anyway.

Solution B
    Good: Solution B was in my opionion the easiest to read. I think for smaller lists it would work good. 
    Bad: Line 20 adds a large time complexity to the problem by sorting the full size N list. 

Solution C:
    Good: The creation of the seen, and seen order from lines 13 and 14 allow for more data and the potenital to use more and update the code to give more then just what it can. Line 29 was a simple return line that made sense and was the most clean out of the other return lines.
    Bad: In lines 21 - 24, that whole process makes the time complexity incredibly high, looping through the whole list multiple times can be incredibly draining on resources. 
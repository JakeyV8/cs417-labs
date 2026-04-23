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
Part 0:
1. Allowing for this function to take in any file and create this will be hard to change.
2. Changing categories to allow for more or different items.
3. Creating a better expense report that can be more fluid.

Part 4:
1. My first thing that I wrote down wasn't that hard to do, it messed me up for a second because I was trying to read the csv not just take in a text box shaped in a csv. Categories was easier then I expceted, it helps having a json file dedicated to that. The report was the hardest to do in my opinion.

2. Part 1 showed single responsibility, instead of having one function that choses between json or csv we have two functions one for each. 
part 2 was strategy/pluggable parts. We used the catagory dictonary and read from there.
part 3 was seperation of i/o by making the function return just the catagory and amount.

3. For me the build report,  was the hardest. For all of them I would try and take the given code and work around that, but I found this to be the hardest to work around.

4. I would change how the name of the file is taken in. I would have the test/user give it then have csv importated, and the user would have to chose between CSV opener or json opener, and they would open the correct API and work similar to how this one works after. 
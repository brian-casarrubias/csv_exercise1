'''
date,temperature(F)
Jan 1,27
Jan 2,31
Jan 3,23
Jan 4,34
Jan 5,37
Jan 6,38
Jan 7,29
Jan 8,30
Jan 9,35
Jan 10,30
'''
'''

 (a) What was the average temperature in first week of Jan

  (b) What was the maximum temperature in first 10 days of Jan

  Figure out data structure that is best for this problem



A)
This exercise opens the csv file, reads it, and appends to a list I named 'weather_week'
Before iterating, i used next(csv_reader) to skip the header because I dont need that info
Then I  used a for loop to iterate through the csv_reader, and appended the second row which displays the temperatures only(all values after the comma)
Next I extracted the values from index 0, to 7 because the question was to get the average temp for the first 7 days...
Next i used another for loop to add all the values to my 'average_temp' variable, then divided by the length to get the average.. also I had to
use the int() because weather_week was a str and average temp was an int.



B) For b I did the same thing for reading, and skipping the header as above..
again I appended the second row which gave me the termperture values..
This time though I created a method called 'sort_it' which was more of a practice type to use bubble sort algorithm, and what it did was
sort the values in the list from least to greatest, that way I could easily calculate the biggest number by just printing out [-1] which will extrtact the last element 
However an easier way to do this was to just use the built in method provided by python which is called 'sort' but like i said, I just wanted more practice.


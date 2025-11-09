#Create a tuple containing the names of five cities. Use the max() function to find the city with the longest name, and then use the min() function to find the city with the shortest name.
tuple1=("coimbatore","mumbai","hosur","chennai","salem")
maximum=max((tuple1),key=len)
minimum=min((tuple1),key=len)
print(maximum)
print(minimum)

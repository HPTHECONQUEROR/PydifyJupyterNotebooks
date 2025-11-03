class_list = [5,7,222,11,3,10]
#in a string or list if we need to access a particular element we need to use []
tall = 0 

start,end,step = 0,len(class_list),1  #0,5,1

while start < end:
	if class_list[start] > tall:
		tall = class_list[start]
	start = start + step
	
print(tall)
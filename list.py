marks=[45,23,24,37,90]
print(marks)
marks.append(22)#add the new value in list 
marks[2]=34 #chnage the value of list
marks.remove(90)#remove the value list  method 
print(marks[0:])#sliceing the list
marks.sort()#sort to ascending order 
print(marks)
print(marks.sort())# this modife the list but not return the value  none
marks.sort(reverse=True)#sort to descending order 
print(marks )      
marks.reverse()
print(marks )
marks.insert(1,20)#index insert which element are insert the value 
print(marks)
marks.pop(5)#delete the list in index value in the index   
print(marks)
marks ={
    "harry":100,"shubham":200,"teman":728

}
print(marks,type(marks))
print(marks["teman"])#this use search value of and lsit are not item in value the they are give the  error 
print(marks.items())#method of dictionary item
print(marks.keys())#second method of python  this means show the variable name of the list like list key teman shubham
print(marks.values())#third method of dictionary this show the value of key
print(marks.update({"teman":623}))# this type use method show the none value 
marks.update({"teman":623,"vinay":800})#this is method they are modify value and new add value 
print(marks.get("teman"))#this method given value of search key this is show none not a error of code 
#print(marks.clear())#thismethod clear the value in list
marks2=marks.copy()#this
print(marks2)
print(marks.pop("vinay"))
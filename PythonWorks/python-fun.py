#enumerate to iterate over two lists and their indices.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
print("\n===========================\n#enumerate function.\n===========================")    
print("list: ",alist)
for i, a in enumerate(alist):
    print (i, a)
    
    
#zip function
print("\n===========================\n#zip function.\n===========================")    
print("list1:",alist)
print("list2:",blist)
for a, b in zip(alist, blist):
    print (a, b)


#enumerate with zip function
print("\n===========================\n#enumerate with zip function.\n===========================")    
print("list1:",alist)
print("list2:",blist)   

for i, (a, b) in enumerate(zip(alist, blist)):
    print (i, a, b)
    


# A list of the largest values    
print("\n===========================\n#max and append function.\n===========================")    
a = [1, 2, 3, 4, 5]
b = [2, 2, 9, 0, 9]
print("list1:",a)
print("list2:",b)
result = []
list_length = len(a)

for i in range(list_length):
	result.append(max(a[i], b[i]))
print("max  :",result)


# A list of the largest values    
print("\n===========================\n#convert tuple in a list function.\n===========================") 
aTuple = (123, 'xyz', 'zara', 'abc')
print ("tuple:", aTuple)
aList = list(aTuple)
print ("list: ", aList)



#this fun is a not working python3 it a give error base64.
#encode to decode.
print("\n===========================\n#encode and decode function.\n===========================") 
print("#encode and decode functions is a give error in python3 \n#if you have use it then remove comment and \n#run with python only.")
'''
Str = "this is string example....wow!!!";
Str = Str.encode('base64','strict');

print ("Encoded String: " + Str)
print ("Decoded String: " + Str.decode('base64','strict'))
'''

#working with dict
print("\n===========================\n#dict function.\n===========================") 

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print("dict = {}:",dict)
print("tinydict:",tinydict)

print ("dict all keys:",tinydict.keys()) 


#unichr, ord, char, hex, oct
print("\n===========================\n#unichr, ord, char, hex and oct function.\n===========================") 

print("#unichar function give a error in python3 \n#if you have use it then remove comment and \n#run with python only.")
#print("unichr(65):",unichr(65))
print("chr(65):",chr(65))
print("ord('A'):",ord('A'))
print("hex(65):",hex(65))
print("oct(65):",oct(65))


#pop
print("\n===========================\n#pop function.\n===========================")
print("alist:",alist)
print ("alist.pop(0): ", alist.pop(0))
print("alist:",alist)
print ("alist.pop(1): ", alist.pop(1))
print ("alist:",alist)

#pop
print("\n===========================\n#sort function.\n===========================")
print("#sort function give a error in python3 \n#if you have use it then remove comment and \n#run with python only.")
'''
alist = [123, 'a3', 'a1', 'a0', 'a4'];
print("alist:",alist)
alist.sort();
print ("alist:",alist)
'''





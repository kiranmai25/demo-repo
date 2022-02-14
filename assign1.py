"""
str1 = " this is the first assignment"
print(str1[::-1])
"""

#reverding the words of a string
str1= "this is reverse words in python example"
print(str1)
words = str1.split(" ")     #splits the string based on the delimeter 'space'
print(words)
words = words[-1::-1]      # x[startAt:endBefore:skip]
print(words)
res = " ".join(words)      #join-str func,allows u to join multiple ele using specific stringin this case [space]
print(res)

str1= "this is reverse words in python example"
print(str1)
words = str1.split(" ")
print(words)
words.reverse()
print(words)
print(" ".join(words))

#interchainging the first and last element in the list
numlist = [35, 24, 9, 56, 12]
first, *other , last = numlist
print( last , other , first )



num = [35, 24, 9, 56, 12]
print(num)
a= num.pop(0)
b=num.pop(-1)
num.insert(0,b)
num.append(a)
print(num)










